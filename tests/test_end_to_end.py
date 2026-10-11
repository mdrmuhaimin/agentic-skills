"""Exercise installed resources and their checker in isolated Git projects."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
NAMES = ('ai-dev-workflow', 'code-walkthrough', 'online-tutor', 'mobile-ui-ux-designer')


class EndToEndTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        spec = importlib.util.spec_from_file_location('e2e_installer', ROOT / 'scripts/install_skills.py')
        self.installer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.installer)

    def run_command(self, command, project):
        result = subprocess.run(command, cwd=project, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return result.stdout.strip()

    def make_project(self, name):
        project = self.root / name
        (project / 'src').mkdir(parents=True)
        (project / 'docs').mkdir()
        source = project / 'src/totals.py'
        source.write_text('def total(items):\n    return sum(items)\n', encoding='utf-8')
        self.run_command(['git', 'init', '-q'], project)
        self.run_command(['git', 'add', 'src/totals.py'], project)
        self.run_command(['git', '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid',
                          'commit', '-qm', 'Record baseline'], project)
        base = self.run_command(['git', 'rev-parse', 'HEAD'], project)
        source.write_text('def total(items):\n    return round(sum(items), 2)\n', encoding='utf-8')
        walkthrough = project / 'docs/walkthrough.md'
        walkthrough.write_text(
            '# Completed, uncommitted work\n\n'
            'Before:\n\n```python\ndef total(items):\n    return sum(items)\n```\n'
            f'Source: [src/totals.py:1-2](../src/totals.py#L1-L2) at {base}\n\n'
            'After:\n\n```python\ndef total(items):\n    return round(sum(items), 2)\n```\n'
            'Source: [src/totals.py:1-2](../src/totals.py#L1-L2) at WORKTREE\n', encoding='utf-8')
        return project, source, walkthrough, base

    def test_installed_bundle_and_checker_for_each_host_and_scope(self):
        for tool, directory in self.installer.TOOL_DIRECTORIES.items():
            for scope in ('project', 'user'):
                with self.subTest(tool=tool, scope=scope):
                    project, source, walkthrough, base = self.make_project(f'{tool}-{scope}')
                    personal = self.root / f'{tool}-personal'
                    args = ['--tool', tool]
                    args += ['--project', str(project)] if scope == 'project' else ['--user']
                    for name in NAMES:
                        args += ['--skill', name]
                    install_root = project if scope == 'project' else personal
                    target = install_root / directory / 'skills'
                    with mock.patch.object(Path, 'home', return_value=personal), mock.patch('sys.stdout'):
                        self.assertEqual(self.installer.main(args + ['--dry-run']), 0)
                        self.assertFalse(target.exists())
                        self.assertEqual(self.installer.main(args), 0)
                        for name in NAMES:
                            self.assertEqual(self.installer.inventory(target / name),
                                             self.installer.inventory(ROOT / 'skills' / name))
                        marker = target / 'ai-dev-workflow/references/engineering.md'
                        before = marker.stat().st_mtime_ns
                        self.assertEqual(self.installer.main(args), 0)
                        self.assertEqual(marker.stat().st_mtime_ns, before)
                    checker = target / 'code-walkthrough/scripts/check_walkthrough.py'
                    source_before = source.read_bytes()
                    index_before = self.run_command(['git', 'diff', '--cached'], project)
                    self.run_command([sys.executable, str(checker), str(walkthrough), base], project)
                    walkthrough.write_text(walkthrough.read_text().replace('return round(sum(items), 2)',
                                                                         'return round(sum(items), 3)'),
                                           encoding='utf-8')
                    result = subprocess.run([sys.executable, str(checker), str(walkthrough), base],
                                            cwd=project, capture_output=True, text=True)
                    self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                    self.assertEqual(source.read_bytes(), source_before)
                    self.assertEqual(self.run_command(['git', 'rev-parse', 'HEAD'], project), base)
                    self.assertEqual(self.run_command(['git', 'diff', '--cached'], project), index_before)
                    for config in ('.claude/settings.json', '.cursor/settings.json', '.codex/config.toml'):
                        self.assertFalse((install_root / config).exists())

    def test_conflict_blocks_missing_skill_without_altering_existing_bundle(self):
        project = self.root / 'conflict'
        with mock.patch('sys.stdout'):
            self.assertEqual(self.installer.main(['--tool', 'codex', '--project', str(project),
                                                 '--skill', 'online-tutor']), 0)
        target = project / '.agents/skills'
        existing = target / 'online-tutor/references/teaching.md'
        existing.write_text('Keep the developer edits.\n', encoding='utf-8')
        before = self.installer.inventory(target)
        with mock.patch('sys.stdout'), mock.patch('sys.stderr'):
            result = self.installer.main(['--tool', 'codex', '--project', str(project),
                                          '--skill', 'ai-dev-workflow', '--skill', 'online-tutor'])
        self.assertEqual(result, 1)
        self.assertEqual(self.installer.inventory(target), before)
        self.assertFalse((target / 'ai-dev-workflow').exists())


if __name__ == '__main__':
    unittest.main()
