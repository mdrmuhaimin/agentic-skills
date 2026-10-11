#!/usr/bin/env python3
"""Copy explicitly selected skills without overwriting local installations.

Python 3.10+, standard library only. Does not install the plugin or edit settings.
"""

import argparse
import pathlib
import re
import shutil
import sys

SKILLS = pathlib.Path(__file__).resolve().parents[1] / "skills"
TOOL_DIRECTORIES = {"claude": ".claude", "codex": ".agents", "cursor": ".cursor"}
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def ignored(name):
    return name in {"__pycache__", ".DS_Store"} or name.endswith((".pyc", ".pyo"))


def inventory(folder):
    """Compare all resources, including empty directories, ignoring local caches."""
    if folder.is_symlink() or not folder.is_dir():
        raise ValueError(f"Not a regular skill directory: {folder}")
    entries = {}
    for path in sorted(folder.rglob("*")):
        relative = path.relative_to(folder)
        if any(ignored(part) for part in relative.parts):
            continue
        if path.is_symlink():
            raise ValueError(f"Symlink resource is not supported: {path}")
        if path.is_dir():
            entries[str(relative)] = None
        elif path.is_file():
            entries[str(relative)] = path.read_bytes()
        else:
            raise ValueError(f"Not a regular resource: {path}")
    return entries


def destination(tool, project):
    scope = (pathlib.Path(project).expanduser() if project is not None else pathlib.Path.home()).resolve()
    target = scope / TOOL_DIRECTORIES[tool] / "skills"
    if not target.resolve().is_relative_to(scope):
        raise ValueError(f"Skills directory escapes the selected scope: {target}")
    return target


def install(source, target, names, *, dry_run=False):
    """Preflight every selection before making any changes."""
    actions = []
    for name in dict.fromkeys(names):
        if not NAME.fullmatch(name):
            raise ValueError(f"Invalid skill name: {name!r}")
        folder = source / name
        if not (folder / "SKILL.md").is_file():
            raise ValueError(f"Skill not found: {name}")
        contents = inventory(folder)
        installed = target / name
        if installed.is_symlink():
            raise ValueError(f"Refusing symlink destination: {installed}")
        if installed.exists():
            if inventory(installed) != contents:
                raise ValueError(f"Conflicting installation: {installed}; move it aside explicitly before retrying")
            actions.append((folder, installed, False))
        else:
            actions.append((folder, installed, True))

    for folder, installed, copy in actions:
        if not copy:
            print(f"Unchanged: {installed}")
        elif dry_run:
            print(f"Would install: {folder.name} -> {installed}")
        else:
            installed.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(folder, installed, ignore=lambda _folder, entries: [entry for entry in entries if ignored(entry)])
            print(f"Installed: {installed}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tool", required=True, choices=TOOL_DIRECTORIES)
    scope = parser.add_mutually_exclusive_group(required=True)
    scope.add_argument("--project", type=pathlib.Path, metavar="PATH")
    scope.add_argument("--user", action="store_true")
    parser.add_argument("--skill", action="append", required=True, metavar="NAME")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    try:
        target = destination(args.tool, args.project)
        install(SKILLS, target, args.skill, dry_run=args.dry_run)
    except (OSError, ValueError) as error:
        print(f"install_skills: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
