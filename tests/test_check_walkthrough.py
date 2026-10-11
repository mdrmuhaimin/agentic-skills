import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/code-walkthrough/scripts/check_walkthrough.py"
FLOW = "def ingest(document):\n    text = extract(document)\n    if not text:\n        return None\n    parts = split(text)\n    return store(parts)\n"


class WalkthroughTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = pathlib.Path(self.temp.name).resolve()
        self.git("init", "-q")
        (self.repo / "app").mkdir()
        (self.repo / "app/flow.py").write_text(FLOW)
        self.git("add", "app")
        self.git("-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "-qm", "seed")
        self.base = self.git("rev-parse", "HEAD")
        self.page = self.repo / "docs/walkthrough.md"
        self.page.parent.mkdir()

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.repo, check=True, capture_output=True, text=True).stdout.strip()

    def check(self, text, source=None, cwd=None):
        self.page.write_text(text)
        return subprocess.run([sys.executable, str(SCRIPT), str(self.page), source or self.base],
                              cwd=cwd or self.repo, capture_output=True, text=True)

    def excerpt(self, code="    text = extract(document)\n    if not text:\n", source="app/flow.py:2-3",
                target="../app/flow.py#L2-L3", revision=""):
        return f"```python\n{code}```\nSource: [{source}]({target}){revision}\n"

    def assert_pass(self, result):
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def assert_problem(self, result, message=None):
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        if message:
            self.assertIn(message, result.stdout)

    def test_exact_excerpt_and_prose_citation_pass(self):
        self.assert_pass(self.check(self.excerpt() + "\nSee [app/flow.py:2](../app/flow.py#L2).\n"))

    def test_committed_utf8_source_under_ascii_locale(self):
        (self.repo / "app/unicode.py").write_text('message = "café"\n', encoding="utf-8")
        self.git("add", "app/unicode.py")
        self.git("-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "-qm", "unicode")
        self.page.write_text(self.excerpt('message = "café"\n', "app/unicode.py:1", "../app/unicode.py#L1"), encoding="utf-8")
        result = subprocess.run([sys.executable, str(SCRIPT), str(self.page), "HEAD"], cwd=self.repo,
                                capture_output=True, encoding="utf-8", env={**os.environ, "LC_ALL": "C",
                                "PYTHONUTF8": "0", "PYTHONCOERCECLOCALE": "0"})
        self.assert_pass(result)

    def test_ssh_origin_with_explicit_port(self):
        self.git("remote", "add", "origin", "ssh://git@github.com:22/org/repo.git")
        target = f"https://github.com/org/repo/blob/{self.base}/app/flow.py#L2-L3"
        self.assert_pass(self.check(self.excerpt(target=target)))

    def test_changed_character_and_indentation_fail(self):
        for code in ("    text = extract(documents)\n    if not text:\n", "text = extract(document)\n    if not text:\n"):
            with self.subTest(code=code):
                self.assert_problem(self.check(self.excerpt(code=code)), "does not match")

    def test_quoted_excerpts_are_checked_including_nested_quotes(self):
        for prefix in ("> ", "> > "):
            with self.subTest(prefix=prefix):
                quoted = "\n".join(prefix + line for line in self.excerpt().splitlines()) + "\n"
                result = self.check(quoted)
                self.assert_pass(result)
                self.assertIn("Checked 1 excerpts", result.stdout)
                self.assert_problem(self.check(quoted.replace("extract(document)", "extract(documents)")), "does not match")

    def test_list_marker_fences_are_not_silently_skipped(self):
        text = "- ```python\n  incorrect()\n  ```\n  Source: [app/flow.py:2](../app/flow.py#L2)\n"
        self.assert_problem(self.check(text), "separate line")

    def test_malformed_prose_citations_and_revision_suffixes_fail(self):
        for text in ("See [app/flow.py:-1](../app/flow.py#L1).\n",
                     "See [app/flow.py:2].\n",
                     "See [app/flow.py:2](../app/flow.py#L2\n",
                     "See [app/flow.py:2]().\n",
                     "See [app/flow.py:2-oops](../app/flow.py#L2).\n",
                     "See [app/flow.py:2](../app/flow.py#L2) at WORKTREEE.\n",
                     f"See [app/flow.py:2](../app/flow.py#L2) at {self.base}wrong.\n"):
            with self.subTest(text=text):
                self.assert_problem(self.check(text), "Malformed")

    def test_bare_executable_ellipsis_is_not_an_elision(self):
        self.assert_problem(self.check(self.excerpt("def ingest(document):\n...\n    return store(parts)\n",
                                                   "app/flow.py:1-6", "../app/flow.py#L1-L6")), "does not match")
        (self.repo / "app/ellipsis.py").write_text("...\n")
        self.assert_pass(self.check(self.excerpt("...\n", "app/ellipsis.py:1", "../app/ellipsis.py#L1"), "WORKTREE"))

    def test_elision_preserves_order(self):
        code = "def ingest(document):\n    # ...\n    parts = split(text)\n    return store(parts)\n"
        self.assert_pass(self.check(self.excerpt(code, "app/flow.py:1-6", "../app/flow.py#L1-L6")))
        code = "    parts = split(text)\n    # ...\n    text = extract(document)\n"
        self.assert_problem(self.check(self.excerpt(code, "app/flow.py:1-6", "../app/flow.py#L1-L6")))

    def test_entirely_elided_excerpt_fails(self):
        self.assert_problem(self.check(self.excerpt("# ...\n")), "no source lines")

    def test_trailing_whitespace_is_ignored(self):
        self.assert_pass(self.check(self.excerpt("    text = extract(document)   \n    if not text:\n")))

    def test_missing_and_malformed_source_fail(self):
        for text in ("```python\nx = 1\n```\n", "```python\nx = 1\n```\nSource: app/flow.py line 2\n"):
            self.assert_problem(self.check(text), "Source")

    def test_unclosed_fence_fails(self):
        self.assert_problem(self.check("```python\nx = 1\n"), "Unclosed")

    def test_closing_fence_must_not_have_trailing_text(self):
        self.assert_problem(self.check("```python\nx = 1\n``` still code\n"), "Unclosed")

    def test_example_and_diagram_exemptions_are_explicit(self):
        self.assert_pass(self.check("```sh\npython demo.py\n```\nExample: A command to illustrate usage.\n"))
        self.assert_pass(self.check("```mermaid\nflowchart LR\n  A --> B\n```\n"))
        self.assert_problem(self.check("```text\nfictional output\n```\n"), "Source")

    def test_missing_file_and_invalid_ranges_fail(self):
        self.assert_problem(self.check(self.excerpt(source="app/missing.py:2-3", target="../app/missing.py#L2-L3")), "does not exist")
        for label, fragment in (("0-1", "0-L1"), ("3-2", "3-L2"), ("2-99", "2-L99")):
            self.assert_problem(self.check(self.excerpt(source=f"app/flow.py:{label}", target=f"../app/flow.py#L{fragment}")))

    def test_wrong_excerpt_range_fails(self):
        self.assert_problem(self.check(self.excerpt("def ingest(document):\n", "app/flow.py:4-6", "../app/flow.py#L4-L6")))

    def test_wrong_local_target_or_fragment_fails(self):
        for target in ("../app/other.py#L2-L3", "../app/flow.py#L1-L3", "../app/flow.py#L2"):
            self.assert_problem(self.check(self.excerpt(target=target)), "target")

    def test_local_target_without_fragment_is_allowed(self):
        self.assert_pass(self.check(self.excerpt(target="../app/flow.py")))

    def test_prose_range_is_checked(self):
        self.assert_problem(self.check("See [app/flow.py:99](../app/flow.py#L99).\n"))

    def test_working_tree_new_file_and_dirty_file_pass(self):
        (self.repo / "app/flow.py").write_text(FLOW.replace("extract(document)", "extract_pages(document)"))
        code = "    text = extract_pages(document)\n    if not text:\n"
        self.assert_pass(self.check(self.excerpt(code), "WORKTREE"))
        self.assert_problem(self.check(self.excerpt(code)))
        (self.repo / "app/new.py").write_text("answer = 42\n")
        self.assert_pass(self.check(self.excerpt("answer = 42\n", "app/new.py:1", "../app/new.py#L1"), "WORKTREE"))

    def test_mixed_committed_and_uncommitted_excerpts(self):
        (self.repo / "app/flow.py").write_text(FLOW.replace("split(text)", "split_pages(text)"))
        before = self.excerpt("    parts = split(text)\n", "app/flow.py:5", "../app/flow.py#L5")
        after = self.excerpt("    parts = split_pages(text)\n", "app/flow.py:5", "../app/flow.py#L5", " at WORKTREE")
        self.assert_pass(self.check(before + "\n" + after))
        prose = f"Before: [app/flow.py:5](../app/flow.py#L5) at {self.base}.\n"
        self.assert_pass(self.check(prose + after, "WORKTREE"))

    def test_mixed_committed_revisions(self):
        (self.repo / "app/flow.py").write_text(FLOW + "\ndef extra():\n    return 1\n")
        self.git("-c", "user.name=Test", "-c", "user.email=test@example.invalid", "commit", "-qam", "grow")
        after = self.git("rev-parse", "HEAD")
        block = self.excerpt("def extra():\n    return 1\n", "app/flow.py:8-9", "../app/flow.py#L8-L9", f" at {after}")
        self.assert_pass(self.check(self.excerpt() + block))
        for revision in (after, after[:12], "WORKTREE"):
            changed = self.excerpt("def extra():\n    return 2\n", "app/flow.py:8-9", "../app/flow.py#L8-L9", f" at {revision}")
            self.assert_problem(self.check(self.excerpt() + changed), "does not match")
        link = f"https://github.com/o/r/blob/{after}/app/flow.py#L9"
        self.assert_pass(self.check(f"See [app/flow.py:9]({link}).\n"))

    def test_permalink_path_and_explicit_revision_must_agree(self):
        link = f"https://github.com/o/r/blob/{self.base}/app/other.py#L2-L3"
        self.assert_problem(self.check(self.excerpt(target=link)), "target")
        link = f"https://github.com/o/r/blob/{self.base}/app/flow.py#L2-L3"
        self.assert_problem(self.check(self.excerpt(target=link, revision=" at WORKTREE")), "revision")

    def test_permalink_repository_must_match_known_origin(self):
        self.git("remote", "add", "origin", "git@github.com:o/r.git")
        link = f"https://github.com/o/other/blob/{self.base}/app/flow.py#L2-L3"
        self.assert_problem(self.check(self.excerpt(target=link)), "origin")
        self.assert_pass(self.check(self.excerpt(target=link.replace("o/other", "o/r"))))

    def test_gitlab_permalink(self):
        link = f"https://gitlab.com/group/team/repo/-/blob/{self.base}/app/flow.py#L2-3"
        self.assert_pass(self.check(self.excerpt(target=link)))

    def test_non_commit_remote_link_is_not_a_permalink(self):
        link = "https://github.com/o/r/blob/main/app/flow.py#L2-L3"
        self.assert_problem(self.check(self.excerpt(target=link)), "permalink")

    def test_paths_with_spaces_are_supported(self):
        (self.repo / "app/a file.py").write_text("value = 1\n")
        self.assert_pass(self.check(self.excerpt("value = 1\n", "app/a file.py:1", "../app/a%20file.py#L1"), "WORKTREE"))

    def test_source_and_target_cannot_escape_repository(self):
        self.assert_problem(self.check(self.excerpt(source="../outside.py:2-3", target="../../outside.py#L2-L3")))
        self.assert_problem(self.check(self.excerpt(target="../../outside.py#L2-L3")))

    def test_working_tree_symlink_cannot_read_outside_repository(self):
        with tempfile.TemporaryDirectory() as other:
            external = pathlib.Path(other) / "outside.py"
            external.write_text(FLOW)
            (self.repo / "app/link.py").symlink_to(external)
            self.assert_problem(self.check(self.excerpt(source="app/link.py:2-3", target="../app/link.py#L2-L3"), "WORKTREE"))

    def test_subdirectory_invocation_uses_repository_root(self):
        self.assert_pass(self.check(self.excerpt(), cwd=self.repo / "app"))

    def test_no_git_working_tree_mode(self):
        with tempfile.TemporaryDirectory() as other:
            folder = pathlib.Path(other).resolve()
            (folder / "demo.py").write_text("x = 1\n")
            page = folder / "walkthrough.md"
            page.write_text("```python\nx = 1\n```\nSource: [demo.py:1](demo.py#L1)\n")
            result = subprocess.run([sys.executable, str(SCRIPT), str(page), "WORKTREE"], cwd=folder, capture_output=True, text=True)
            self.assert_pass(result)

    def test_invalid_input_returns_usage_error(self):
        result = self.check(self.excerpt(), "nonexistent-ref")
        self.assertEqual(result.returncode, 2)
        self.assertNotIn("Traceback", result.stderr)

    def test_narrative_without_excerpts_reports_no_source_claims(self):
        result = self.check("# A narrative\n\nNo code citations here.\n")
        self.assert_pass(result)
        self.assertIn("No source claims", result.stdout)


if __name__ == "__main__":
    unittest.main()
