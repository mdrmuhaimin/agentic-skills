"""Catch packaging drift without adding dependencies to the helper test suite."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
NAMES = {'ai-dev-workflow', 'code-walkthrough', 'online-tutor', 'mobile-ui-ux-designer'}
MANUAL = {'ai-dev-workflow', 'code-walkthrough'}


class PackageTests(unittest.TestCase):
    def read_json(self, path):
        return json.loads((ROOT / path).read_text(encoding='utf-8'))

    def test_manifest_identity_version_and_shared_skill_paths(self):
        portable = self.read_json('plugin.json')
        self.assertEqual(portable['name'], 'makewell')
        self.assertEqual(portable['version'], '0.1.0')
        self.assertEqual(portable['extensions']['com.openai']['interface']['displayName'], 'Makewell')
        self.assertEqual(portable['extensions']['com.openai']['interface']['shortDescription'], 'Plan, build, review, and learn')
        openai_interface = portable['extensions']['com.openai']['interface']
        self.assertEqual(openai_interface['logo'], './assets/makewell-logo.svg')
        self.assertEqual(openai_interface['composerIcon'], './assets/makewell-logo.svg')
        codex = self.read_json('.codex-plugin/plugin.json')
        self.assertEqual(codex['interface']['displayName'], 'Makewell')
        self.assertEqual(codex['interface']['shortDescription'], 'Plan, build, review, and learn')
        self.assertEqual(codex['interface']['logo'], './assets/makewell-logo.svg')
        self.assertEqual(codex['interface']['composerIcon'], './assets/makewell-logo.svg')
        self.assertTrue((ROOT / 'assets/makewell-logo.svg').is_file())
        for host in ('claude', 'codex', 'cursor'):
            manifest = self.read_json(f'.{host}-plugin/plugin.json')
            self.assertEqual((manifest['name'], manifest['version']), (portable['name'], portable['version']))
            self.assertTrue(set(manifest).isdisjoint({'hooks', 'mcpServers', 'settings', 'agents'}))
            if 'skills' in manifest:
                self.assertEqual((ROOT / manifest['skills']).resolve(), (ROOT / 'skills').resolve())

    def test_marketplaces_expose_only_this_root_plugin(self):
        for path in ('.claude-plugin/marketplace.json', '.cursor-plugin/marketplace.json', '.agents/plugins/marketplace.json'):
            catalog = self.read_json(path)
            self.assertEqual(catalog['name'], 'makewell')
            self.assertEqual(len(catalog['plugins']), 1)
            plugin = catalog['plugins'][0]
            self.assertEqual(plugin['name'], 'makewell')
            source = plugin['source']
            if isinstance(source, dict):
                self.assertEqual(source['source'], 'local')
                source = source['path']
                self.assertEqual(plugin['policy']['installation'], 'AVAILABLE')
            self.assertEqual((ROOT / source).resolve(), ROOT)
            if 'version' in plugin:
                self.assertEqual(plugin['version'], self.read_json('plugin.json')['version'])

    def test_canonical_identities_and_invocation_policies(self):
        self.assertEqual({p.name for p in (ROOT / 'skills').iterdir() if p.is_dir()}, NAMES)
        for name in NAMES:
            skill = ROOT / 'skills' / name
            text = (skill / 'SKILL.md').read_text(encoding='utf-8')
            frontmatter = text.split('---', 2)[1]
            self.assertRegex(frontmatter, rf'(?m)^name: {re.escape(name)}$')
            self.assertRegex(frontmatter, r'(?m)^description: .+')
            self.assertEqual('disable-model-invocation: true' in frontmatter, name in MANUAL)
            if name in MANUAL:
                policy = (skill / 'agents/openai.yaml').read_text(encoding='utf-8')
                self.assertRegex(policy, r'(?m)^policy:\s*\n  allow_implicit_invocation: false$')

    def test_skill_supporting_links_exist_and_remain_within_skill(self):
        for name in NAMES:
            skill = ROOT / 'skills' / name
            for markdown in skill.rglob('*.md'):
                text = markdown.read_text(encoding='utf-8')
                text = re.sub(r'(?ms)^(`{3,}|~{3,}).*?^\1[ \t]*$', '', text)
                text = re.sub(r'`[^`\n]*`', '', text)
                for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
                    if '://' in target or target.startswith('#'):
                        continue
                    file = (markdown.parent / target.split('#', 1)[0]).resolve()
                    self.assertTrue(file.is_relative_to(skill), (markdown, target))
                    self.assertTrue(file.is_file(), (markdown, target))


if __name__ == '__main__':
    unittest.main()
