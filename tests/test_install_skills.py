import importlib.util
import pathlib
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/install_skills.py"


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = pathlib.Path(self.temp.name).resolve()
        self.source = self.root / "source"
        for name in ("first", "second"):
            folder = self.source / name
            (folder / "references").mkdir(parents=True)
            (folder / "SKILL.md").write_text(f"---\nname: {name}\ndescription: test\n---\n")
            (folder / "references/note.md").write_text("resource")
        spec = importlib.util.spec_from_file_location("installer", SCRIPT)
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)
        self.destination = self.root / "project/.agents/skills"

    def install(self, names=("first",), dry_run=False):
        with mock.patch("sys.stdout"):
            return self.module.install(self.source, self.destination, names, dry_run=dry_run)

    def test_selection_copies_all_resources_only_for_selected_skill(self):
        self.install()
        self.assertEqual((self.destination / "first/references/note.md").read_text(), "resource")
        self.assertFalse((self.destination / "second").exists())

    def test_dry_run_creates_nothing(self):
        self.install(dry_run=True)
        self.assertFalse(self.destination.parent.exists())

    def test_identical_install_is_noop(self):
        self.install()
        entry = self.destination / "first/SKILL.md"
        before = entry.stat().st_mtime_ns
        self.install()
        self.assertEqual(entry.stat().st_mtime_ns, before)

    def test_conflict_is_preflighted_before_any_skill_is_copied(self):
        self.install(("second",))
        entry = self.destination / "second/SKILL.md"
        entry.write_text("local changes")
        with self.assertRaises(ValueError):
            self.install(("first", "second"))
        self.assertFalse((self.destination / "first").exists())
        self.assertEqual(entry.read_text(), "local changes")

    def test_missing_skill_prevents_partial_install(self):
        with self.assertRaises(ValueError):
            self.install(("first", "missing"))
        self.assertFalse(self.destination.exists())

    def test_extra_destination_resource_counts_as_conflict(self):
        self.install()
        (self.destination / "first/extra.md").write_text("keep me")
        with self.assertRaises(ValueError):
            self.install()

    def test_traversal_is_rejected(self):
        for name in ("../source/first", "/tmp/first", "first/second"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                self.install((name,))

    def test_symlink_destination_is_never_written_through(self):
        self.destination.mkdir(parents=True)
        outside = self.root / "outside"
        outside.mkdir()
        (self.destination / "first").symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ValueError):
            self.install()
        self.assertEqual(list(outside.iterdir()), [])

    def test_symlink_resource_is_not_copied(self):
        (self.source / "first/link").symlink_to(self.source / "second/SKILL.md")
        with self.assertRaises(ValueError):
            self.install()
        self.assertFalse(self.destination.exists())

    def test_caches_are_not_installed_or_treated_as_conflicts(self):
        cache = self.source / "first/__pycache__"
        cache.mkdir()
        (cache / "temp.pyc").write_bytes(b"cache")
        self.install()
        self.assertFalse((self.destination / "first/__pycache__").exists())
        cache = self.destination / "first/__pycache__"
        cache.mkdir()
        (cache / "temp.pyc").write_bytes(b"cache")
        self.install()

    def test_tool_scope_paths_and_user_scope(self):
        for tool, directory in (("claude", ".claude"), ("codex", ".agents"), ("cursor", ".cursor")):
            with self.subTest(tool=tool):
                project = self.root / tool
                self.assertEqual(self.module.destination(tool, project), project / directory / "skills")
                with mock.patch.object(pathlib.Path, "home", return_value=self.root / "personal"):
                    self.assertEqual(self.module.destination(tool, None), self.root / "personal" / directory / "skills")

    def test_user_install_and_dry_run_copy_only_to_selected_host(self):
        personal = self.root / "isolated-user"
        for tool, directory in self.module.TOOL_DIRECTORIES.items():
            with self.subTest(tool=tool), mock.patch.object(pathlib.Path, "home", return_value=personal), \
                    mock.patch.object(self.module, "SKILLS", self.source), mock.patch("sys.stdout"):
                arguments = ["--tool", tool, "--user", "--skill", "first"]
                target = personal / directory / "skills/first"
                self.assertEqual(self.module.main(arguments + ["--dry-run"]), 0)
                self.assertFalse(target.exists())
                self.assertEqual(self.module.main(arguments), 0)
                self.assertEqual((target / "references/note.md").read_text(), "resource")
                self.assertFalse((target.parent / "second").exists())

    def test_scope_directory_symlink_cannot_escape_project(self):
        project = self.root / "escape"
        project.mkdir()
        (project / ".agents").symlink_to(self.root / "outside", target_is_directory=True)
        with self.assertRaises(ValueError):
            self.module.destination("codex", project)

    def test_cli_requires_scope_and_selection(self):
        for arguments in (("--tool", "codex", "--skill", "online-tutor"),
                          ("--tool", "codex", "--project", str(self.root))):
            result = subprocess.run([sys.executable, str(SCRIPT), *arguments], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)

    def test_cli_installs_actual_skill_with_policy_and_checker(self):
        project = self.root / "actual"
        result = subprocess.run([sys.executable, str(SCRIPT), "--tool", "cursor", "--project", str(project),
                                 "--skill", "code-walkthrough"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        copied = project / ".cursor/skills/code-walkthrough"
        self.assertEqual((copied / "SKILL.md").read_bytes(), (ROOT / "skills/code-walkthrough/SKILL.md").read_bytes())
        self.assertTrue((copied / "scripts/check_walkthrough.py").is_file())
        self.assertIn("allow_implicit_invocation: false", (copied / "agents/openai.yaml").read_text())


if __name__ == "__main__":
    unittest.main()
