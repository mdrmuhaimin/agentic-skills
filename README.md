# Agentic Skills

A portable, skills-first plugin for Claude Code, Codex, and Cursor. One maintained copy of each skill lives in `skills/`; the small host manifests package those same folders. Plugin version: **0.1.0**.

| Skill | Purpose | Activation |
|---|---|---|
| `ai-dev-workflow` | Approved understanding → spec → plan → sequential build and review | Explicit request |
| `code-walkthrough` | Cited explanations, source-excerpt checks, and a prose claim audit | Explicit request |
| `online-tutor` | Turn dense material into readable explanations and lessons | Automatic discovery or explicit request |
| `mobile-ui-ux-designer` | Mobile research, interaction design, accessibility, and implementation handoffs | Automatic discovery or explicit request |

The development workflow does not depend on the other skills, a ticket tracker, provider-specific models, or a second plugin. Where native agents are available and permitted, it uses them; otherwise it performs the same roles sequentially and discloses that review lacked independent context. The workflow and walkthrough remain manual in both plugin and standalone installations.

## Install the plugin

Clone this repository first. The local routes below work with this checkout, including changes that have not been published. Use one installation route per skill: combining plugin and standalone copies can produce duplicate discovery.

### Claude Code

From the repository root:

```sh
claude plugin marketplace add .
claude plugin install agentic-skills@agentic-skills-marketplace --scope user
```

For a shared project installation, add the marketplace using the absolute checkout path, then run the install command with `--scope project` from the target project. For a session-only development preview, run `claude --plugin-dir /absolute/path/to/agentic-skills` from the project you want to work on.

After this version is published to the Git repository, current Claude Code also supports this one-step in-chat installation:

```text
/plugin install agentic-skills --marketplace mdrmuhaimin/agentic-skills
```

Select the skill from the `/` menu; the plugin-qualified commands include `/agentic-skills:ai-dev-workflow` and `/agentic-skills:code-walkthrough`. [Claude Code plugin documentation](https://code.claude.com/docs/en/plugins-reference).

### Codex

From the repository root, on a CLI version supporting plugin commands:

```sh
codex plugin marketplace add .
codex plugin add agentic-skills@agentic-skills-marketplace
```

In the desktop app, add this checkout as a local marketplace source, then install **agentic-skills** from **agentic-skills-marketplace**. The catalog makes the plugin available; it does not install it by itself. Restart or refresh discovery if needed. Use the skill selector or `$` menu to select the installed skill. [Codex plugin packaging](https://developers.openai.com/plugins/build/plugins).

### Cursor

For local plugin development, copy the plugin into `~/.cursor/plugins/local/agentic-skills`. From this checkout, the following command copies just the manifests and canonical skills and refuses an existing destination:

```sh
python3 - <<'PY'
from pathlib import Path
import shutil

source = Path.cwd()
target = Path.home() / ".cursor/plugins/local/agentic-skills"
target.mkdir(parents=True, exist_ok=False)
shutil.copy2(source / "plugin.json", target / "plugin.json")
shutil.copytree(source / ".cursor-plugin", target / ".cursor-plugin")
shutil.copytree(source / "skills", target / "skills", ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"))
PY
```

Reload Cursor and inspect **Customize → Skills**. Local plugin imports must be allowed; do not symlink to a checkout outside the local-plugin folder. Team administrators can instead import the published repository through **Dashboard → Plugins & MCPs → Team Marketplaces**, leaving the plugin **Default Off** for explicit installation. This checkout is not submitted to the public marketplace. [Cursor plugin installation and local testing](https://cursor.com/docs/plugins).

## Install selected skills instead

Python 3.10+ is sufficient; the installer uses only the standard library. From this repository:

```sh
python3 scripts/install_skills.py --tool codex --project /absolute/path/to/project \
  --skill ai-dev-workflow --skill code-walkthrough --dry-run

python3 scripts/install_skills.py --tool codex --project /absolute/path/to/project \
  --skill ai-dev-workflow --skill code-walkthrough
```

Choose `--tool claude` or `--tool cursor` for those editors. Replace `--project PATH` with `--user` for a personal installation. Repeat `--skill NAME` to select multiple skills; there is no implicit install-all. All references, scripts, and invocation metadata travel with each selected skill.

| Tool | Project destination | User destination |
|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Codex | `.agents/skills/` | `~/.agents/skills/` |
| Cursor | `.cursor/skills/` | `~/.cursor/skills/` |

Every selection is checked before copying. Identical copies are left unchanged. Conflicting files or extra resources cause a failure; explicitly move the old installation aside before replacing it. Symlink resources/destinations are refused. No settings, permission rules, or marketplace catalogs are edited. Disk/permission failures during copying can leave a partial new folder; the error is reported and existing installations are never overwritten.

## Use the workflow

For standalone skills, examples are:

```text
Claude Code / Cursor:
/ai-dev-workflow Prevent duplicate uploads; keep the current API compatible.
/code-walkthrough Explain the upload-to-storage flow for a new backend developer.

Codex:
Use $ai-dev-workflow to prevent duplicate uploads; keep the current API compatible.
Use $code-walkthrough to explain the upload-to-storage flow for a new backend developer.
```

Plugin installations may namespace these names; use the host's skill menu rather than assuming the standalone spelling. A ticket ID or URL is optional. The workflow stops for approval of understanding, the spec, and the build plan. It offers local per-task commits at the plan gate, defaulting to uncommitted changes. Build checkpoints and designated high-risk tasks also pause for the agreed decision. Build approval does not authorize pushes, deployment, or external posts.

Artifacts follow the target project's existing conventions. Otherwise they live under `docs/workflow/{specs,plans,walkthroughs}/`. Approvals, build base, task evidence, and commit policy are written into the artifacts so another session or editor can resume. Existing files are not treated as proof of approval. Skipping a stage requires an explicit developer instruction.

Walkthroughs work before, during, and after implementation, including uncommitted completion. They distinguish facts from inference and suspicion. The deterministic checker verifies source agreement; a separate claim audit checks what the explanation says about the code. Neither check proves the other.

```sh
# Run inside the project being explained. Use the installed skill's actual path.
python3 /absolute/path/to/code-walkthrough/scripts/check_walkthrough.py \
  docs/workflow/walkthroughs/upload.md WORKTREE
```

See the skill's [citation format](skills/code-walkthrough/references/citations.md) for committed sources, mixed revisions, illustrative blocks, and exit codes. Git is needed for committed sources. Working-tree mode also works outside Git, with citations labelled as mutable.

## Update and troubleshoot

- **Plugin updates:** pull the checkout, then use the host's marketplace refresh/update controls. Claude provides `claude plugin update agentic-skills@agentic-skills-marketplace`; Codex can refresh its marketplace and reinstall using its plugin controls. Cursor local copies need explicit replacement and a reload. Keep all four manifest versions and the Claude catalog version aligned when releasing.
- **Standalone updates:** rerunning is a no-op for identical content. Changed installations are refused; move the previous folder aside, install again, then remove the backup when satisfied.
- **Skill missing:** check for uppercase `SKILL.md`, the correct destination, host trust/import settings, and refresh/restart discovery. Installing this authoring repository alone does not automatically enable its skills in another project.
- **Missing tracker or subagents:** supply the description; the workflow proceeds with disclosed limitations. Review is not independent when performed in the same session.
- **Checker fails:** correct the excerpt, Source label, target, range, or revision; don't relabel copied code as illustrative to suppress a finding. Unavailable checks remain unverified.
- **Mobile design:** the preserved skill contains a project-specific addendum; fill it with real project conventions before using it for implementation.

## Maintain and validate

```sh
python3 -m unittest discover -s tests -v
claude plugin validate .
claude plugin validate .claude-plugin/plugin.json
claude plugin validate skills
```

Validation evidence and compatibility limits are recorded in [docs/validation.md](docs/validation.md). The helpers have no runtime dependencies. Host manifests and skill frontmatter require their own validation: a validator for the common skill fields may not recognize a documented host-specific invocation flag.

The previous paths map as follows; both existing skill bodies are preserved:

| Previous path | Canonical path |
|---|---|
| `codex/agentic-learning-coach/skill.md` | `skills/online-tutor/SKILL.md` |
| `codex/mobile-ui-ux-designer/skill.md` | `skills/mobile-ui-ux-designer/SKILL.md` |

Read [the PR analysis and attribution](docs/pr-319-analysis.md) for the import source and adaptation decisions, and [the complete file-by-file comparison](docs/pr-319-comparison.md) for the follow-up audit and corrections. Existing per-skill license declarations are retained; this package does not claim a repository-wide license for all imported material.
