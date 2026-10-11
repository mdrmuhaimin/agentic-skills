#!/usr/bin/env python3
"""Verify source excerpts and citations, not the explanatory claims around them.

Adapted from Simplexico's PR #319, commit 62e07a50ccfb002ca359495dbaf49bf44c8f3ab0,
tools/mm-workflow/scripts/check_walkthrough.py. Python 3.10+, standard library only.
Usage: check_walkthrough.py <walkthrough.md> <commit-or-WORKTREE>
"""

import pathlib
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

FENCE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
QUOTE = re.compile(r"^[ \t]{0,3}>[ \t]?")
LIST_FENCE = re.compile(r"^\s*(?:[-+*]|\d+[.)])[ \t]+(?:`{3,}|~{3,})")
LINK = re.compile(
    r"\[(?P<path>[^\]\n]+?):(?P<start>\d+)(?:-(?P<end>\d+))?\]"
    r"\((?P<target>[^)\n]+)\)(?:[ \t]+at[ \t]+(?P<revision>WORKTREE|[0-9a-fA-F]{7,64}))?"
)
# Recognize attempted source links even when their range, target, or revision is malformed.
SOURCE_LABEL = re.compile(r"\[[^\]\n]+?:-?\d[^\]\n]*\]")
CANDIDATE = re.compile(
    SOURCE_LABEL.pattern + r"\([^\)\n]*\)"
    r"(?:[ \t]+at(?:[ \t]+[^\s.,;!?)]+)?)?"
)
ELISION = re.compile(r"^\s*(?:(?:#|//|--|;)\s*\.\.\.|/\*\s*\.\.\.\s*\*/|<!--\s*\.\.\.\s*-->)\s*$")
ANCHOR = re.compile(r"L(\d+)(?:-L?(\d+))?\Z")
PERMALINK = re.compile(r"^/(.+?)/(?:-/)?blob/([0-9a-fA-F]{7,64})/(.+)$")


def git(root, *args):
    result = subprocess.run(["git", "-C", str(root), *args], capture_output=True, encoding="utf-8")
    if result.returncode:
        raise ValueError(result.stderr.strip() or "Git command failed")
    return result.stdout


def repository_root():
    try:
        return pathlib.Path(git(pathlib.Path.cwd(), "rev-parse", "--show-toplevel").strip()).resolve()
    except (OSError, ValueError):
        return pathlib.Path.cwd().resolve()


def origin_identity(root):
    try:
        origin = git(root, "remote", "get-url", "origin").strip()
    except (OSError, ValueError):
        return None
    ssh = re.fullmatch(r"[^@]+@([^:]+):(.+)", origin) if "://" not in origin else None
    if ssh:
        host, repo = ssh.groups()
    else:
        parsed = urlsplit(origin)
        if not parsed.hostname:
            return None
        host, repo = parsed.hostname, parsed.path.lstrip("/")
    return host.lower(), unquote(repo).rstrip("/").removesuffix(".git")


class Sources:
    def __init__(self, root, walkthrough, default):
        self.root = root
        self.walkthrough = walkthrough
        self.revisions = {}
        self.files = {}
        self.default = self.resolve(default)
        self.origin = origin_identity(root)

    def resolve(self, revision):
        if revision == "WORKTREE":
            return revision
        if revision not in self.revisions:
            try:
                resolved = git(self.root, "rev-parse", "--verify", "--end-of-options", f"{revision}^{{commit}}").strip()
            except (OSError, ValueError) as error:
                raise ValueError(f"Unknown commit {revision!r}: {error}") from error
            self.revisions[revision] = resolved
        return self.revisions[revision]

    def lines(self, revision, path, start, end):
        key = revision, path
        if key not in self.files:
            if revision == "WORKTREE":
                file = (self.root / path).resolve()
                if not file.is_relative_to(self.root):
                    raise ValueError("Source escapes the repository")
                try:
                    content = file.read_text(encoding="utf-8")
                except OSError as error:
                    raise ValueError(f"{path} does not exist or cannot be read in WORKTREE") from error
            else:
                try:
                    content = git(self.root, "show", f"{revision}:{path}")
                except ValueError as error:
                    raise ValueError(f"{path} does not exist at {revision[:12]}") from error
            self.files[key] = content.splitlines()
        lines = self.files[key]
        if start < 1 or end < start:
            raise ValueError("Invalid line range")
        if end > len(lines):
            raise ValueError(f"Range runs past the end of {path} ({len(lines)} lines)")
        return lines[start - 1:end]

    def citation(self, match):
        path = match.group("path")
        posix = pathlib.PurePosixPath(path)
        if posix.is_absolute() or ".." in posix.parts or "\\" in path:
            raise ValueError("Source path must be repository-relative")
        start = int(match.group("start"))
        end = int(match.group("end") or start)
        target = urlsplit(match.group("target"))
        named = match.group("revision")
        explicit = self.resolve(named) if named else None
        revision = explicit or self.default
        if target.query:
            raise ValueError("Citation target must not contain a query")
        if target.fragment:
            anchor = ANCHOR.fullmatch(target.fragment)
            if not anchor or (int(anchor[1]), int(anchor[2] or anchor[1])) != (start, end):
                raise ValueError("Citation target range does not match its label")

        if target.scheme or target.netloc:
            remote = PERMALINK.fullmatch(unquote(target.path))
            if target.scheme != "https" or not remote:
                raise ValueError("Remote citation must be a GitHub/GitLab commit permalink")
            repo, commit, remote_path = remote.groups()
            identity = (target.hostname, repo)
            if self.origin:
                if identity != self.origin:
                    raise ValueError("Citation repository does not match origin")
            elif target.hostname not in {"github.com", "gitlab.com"}:
                raise ValueError("Unknown permalink host; use a local citation")
            if remote_path != path or not target.fragment:
                raise ValueError("Citation target path/range does not match its label")
            linked = self.resolve(commit)
            if explicit and explicit != linked:
                raise ValueError("Citation revision disagrees with the permalink")
            revision = linked
        else:
            linked = (self.walkthrough.parent / unquote(target.path)).resolve()
            wanted = (self.root / path).resolve()
            if not linked.is_relative_to(self.root) or not wanted.is_relative_to(self.root):
                raise ValueError("Citation target escapes the repository")
            if linked != wanted:
                raise ValueError("Citation target path does not match its label")
        return self.lines(revision, path, start, end)


def excerpt_problem(code, wanted):
    """Source's ordered-elision check, retaining indentation and ignoring trailing space."""
    runs, current, gaps = [], [], False
    for line in code:
        if ELISION.fullmatch(line):
            gaps = True
            if current:
                runs.append(current)
            current = []
        else:
            current.append(line.rstrip())
    if current:
        runs.append(current)
    if not runs:
        return "Excerpt contains no source lines"
    wanted = [line.rstrip() for line in wanted]
    if not gaps:
        return None if runs == [wanted] else "Excerpt does not match the cited lines"
    at = 0
    for run in runs:
        for offset in range(at, len(wanted) - len(run) + 1):
            if wanted[offset:offset + len(run)] == run:
                at = offset + len(run)
                break
        else:
            return "Excerpt lines do not appear in order within the cited range"
    return None


def quote_content(line, depth=None):
    """Remove only the Markdown quote container, preserving source indentation."""
    removed = 0
    while depth is None or removed < depth:
        marker = QUOTE.match(line)
        if not marker:
            break
        line = line[marker.end():]
        removed += 1
    return removed, line


def check(text, sources):
    problems = []
    lines = text.splitlines()
    excerpts = citations = 0
    index = 0
    while index < len(lines):
        depth, content = quote_content(lines[index])
        if LIST_FENCE.match(content):
            problems.append(f"{index + 1}: Put the opening code fence on a separate line from the list marker")
            index += 1
            continue
        fence = FENCE.match(content)
        if fence:
            marker, opening = fence[1], index
            language = fence[2].strip().split(maxsplit=1)
            language = language[0].lower() if language else ""
            close = re.compile(r"\s*" + re.escape(marker[0]) + "{" + str(len(marker)) + r",}\s*\Z")
            index += 1
            code = []
            while index < len(lines) and not close.fullmatch(quote_content(lines[index], depth)[1]):
                code.append(quote_content(lines[index], depth)[1])
                index += 1
            if index == len(lines):
                problems.append(f"{opening + 1}: Unclosed code fence")
                break
            after = quote_content(lines[index + 1], depth)[1] if index + 1 < len(lines) else ""
            if after.startswith("Source:"):
                source = LINK.fullmatch(after[len("Source:"):].strip())
                if not source:
                    problems.append(f"{index + 2}: Malformed Source citation")
                else:
                    try:
                        wanted = sources.citation(source)
                        problem = excerpt_problem(code, wanted)
                        if problem:
                            problems.append(f"{opening + 1}: {problem}")
                        excerpts += 1
                    except (OSError, ValueError, UnicodeError) as error:
                        problems.append(f"{index + 2}: {error}")
                index += 1
            elif re.fullmatch(r"Example:\s*\S.*", after):
                index += 1
            elif language != "mermaid":
                problems.append(f"{opening + 1}: Code fence needs a Source citation or an explicit Example label")
            index += 1
            continue

        for label in SOURCE_LABEL.finditer(content):
            candidate = CANDIDATE.match(content, label.start())
            link = LINK.fullmatch(candidate.group()) if candidate else None
            if not link:
                problems.append(f"{index + 1}: Malformed source citation or revision")
                continue
            try:
                sources.citation(link)
                citations += 1
            except (OSError, ValueError, UnicodeError) as error:
                problems.append(f"{index + 1}: {error}")
        index += 1
    return problems, excerpts, citations


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 2:
        print("usage: check_walkthrough.py <walkthrough.md> <commit-or-WORKTREE>", file=sys.stderr)
        return 2
    try:
        walkthrough = pathlib.Path(args[0]).resolve()
        sources = Sources(repository_root(), walkthrough, args[1])
        text = walkthrough.read_text(encoding="utf-8")
        problems, excerpts, citations = check(text, sources)
    except (OSError, ValueError, UnicodeError) as error:
        print(f"check_walkthrough: {error}", file=sys.stderr)
        return 2
    if problems:
        for problem in problems:
            print(problem)
        return 1
    if excerpts or citations:
        print(f"Checked {excerpts} excerpts and {citations} prose citations. Prose accuracy requires a claim audit.")
    else:
        print("No source claims to check. Prose accuracy requires a claim audit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
