# Understand & Build

**Agentic Skills** is a portable skill plugin for Claude Code, Codex, and Cursor. Version: **0.1.0**. Each skill has one maintained copy under `skills/`.

| Skill | Purpose | Invocation |
|---|---|---|
| `ai-dev-workflow` | Approved understanding, specification, plan, implementation, and review | Explicit request |
| `code-walkthrough` | Cited code explanations with excerpt checks and a claim audit | Explicit request |
| `online-tutor` | Clear explanations, tutorials, and lessons from dense material | Normal discovery or explicit request |
| `mobile-ui-ux-designer` | Mobile design, accessibility, responsive layouts, and implementation handoffs | Normal discovery or explicit request |

The skills stay independent. The workflow does not require a tracker, a particular model, or the other skills.

## Install from GitHub

The packaged version is on branch `codex/portable-agentic-skills`. Clone that branch:

```sh
git clone --branch codex/portable-agentic-skills https://github.com/mdrmuhaimin/agentic-skills.git
cd agentic-skills
```

Choose plugin installation or standalone installation for each skill. Duplicate copies can cause duplicate discovery.

### Claude Code plugin

Run these commands from the checkout:

```sh
claude plugin marketplace add .
claude plugin install agentic-skills@agentic-skills-marketplace --scope user
```

For project scope, add the marketplace with the absolute checkout path. Run the install command with `--scope project` from the target project.

For a session-only preview, start Claude with `--plugin-dir /absolute/path/to/agentic-skills` from the target project.

After the package reaches the default GitHub branch, direct marketplace installation can use:

```sh
claude plugin marketplace add mdrmuhaimin/agentic-skills
claude plugin install agentic-skills@agentic-skills-marketplace --scope user
```

Select a skill from the `/` menu. Plugin commands include `/agentic-skills:ai-dev-workflow` and `/agentic-skills:code-walkthrough`.

See [Claude Code marketplace documentation](https://code.claude.com/docs/en/plugin-marketplaces).

### Codex plugin

A CLI with plugin commands can install directly from GitHub:

```sh
codex plugin marketplace add mdrmuhaimin/agentic-skills --ref codex/portable-agentic-skills
codex plugin add agentic-skills@agentic-skills-marketplace
```

For a local checkout, replace the marketplace source with its path. In the desktop app, add the checkout as a local marketplace source.

Install **agentic-skills** from **agentic-skills-marketplace**. Adding the catalog alone does not install the plugin.

Refresh discovery or restart if needed. Select the skill from the skill selector or `$` menu.

See [Codex plugin packaging](https://developers.openai.com/plugins/build/plugins).

### Cursor plugin

For local plugin use, copy the canonical skills and manifests into Cursor's local plugin directory. This command refuses an existing destination:

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

Reload Cursor. Examine **Customize → Skills**. Local plugin imports must be allowed.

Do not use a symlink to an external checkout. Team administrators can instead import the repository through **Dashboard → Plugins & MCPs → Team Marketplaces**.

Use **Default Off** for explicit team installation. The repository has not been submitted to Cursor's public marketplace.

See [Cursor plugin documentation](https://cursor.com/docs/plugins).

## Install selected skills

The installer requires Python 3.10 or later. It uses only the standard library.

From the checkout, preview the selected installation:

```sh
python3 scripts/install_skills.py --tool codex --project /absolute/path/to/project \
  --skill ai-dev-workflow --skill code-walkthrough --dry-run
```

Remove `--dry-run` to copy the selected skills:

```sh
python3 scripts/install_skills.py --tool codex --project /absolute/path/to/project \
  --skill ai-dev-workflow --skill code-walkthrough
```

Use `--tool claude` or `--tool cursor` for those hosts. Replace `--project PATH` with `--user` for user scope.

Repeat `--skill NAME` for each skill. Scope and selection are mandatory. The installer copies all references, scripts, and invocation metadata.

| Host | Project destination | User destination |
|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Codex | `.agents/skills/` | `~/.agents/skills/` |
| Cursor | `.cursor/skills/` | `~/.cursor/skills/` |

The installer checks all destinations before copying. Identical copies stay unchanged. Conflicting content or extra resources cause failure without replacement.

Move an old installation aside explicitly before installing changed content. The installer refuses symlinks. It does not edit settings, permissions, or marketplace catalogs.

A disk or permission failure can leave a partial new folder. The installer reports the failure and keeps existing installations.

## Use the workflow

Standalone invocation examples are:

```text
Claude Code or Cursor:
/ai-dev-workflow Prevent duplicate uploads while preserving the current API.
/code-walkthrough Explain the upload flow for a new backend developer.

Codex:
Use $ai-dev-workflow to prevent duplicate uploads while preserving the current API.
Use $code-walkthrough to explain the upload flow for a new backend developer.
```

Plugin skills can have namespaced names. Select the installed skill from the host menu.

The workflow gets approval for understanding, the specification, and the plan. A specification records requirements. A plan records ordered tasks and checks.

At the plan decision, choose uncommitted changes or local commits after each task. Uncommitted changes are the default.

The workflow pauses at agreed checkpoints and designated high-risk tasks. It keeps existing authorization. A material scope change requires a new decision.

Records follow project conventions. Otherwise, they use `docs/workflow/{specs,plans,walkthroughs}/`. They keep approvals, the build base, check results, and the commit policy.

The build base is the source state before implementation. Existing files alone do not prove approval or successful checks.

Applicable engineering references cover interfaces, configuration, asynchronous work, migrations, dependencies, AI evaluations, and rendered UI checks. Unrelated guidance stays unloaded.

Native agents are optional. If review uses the same session, the workflow reports that limit. Pushes, merges, deployments, and external posts require separate authorization.

## Use the walkthrough checker

Walkthroughs support early, planned, ongoing, and completed work. They separate verified facts, inference, and suspected causes.

Use the installed checker inside the project being explained:

```sh
python3 /absolute/path/to/code-walkthrough/scripts/check_walkthrough.py \
  docs/workflow/walkthroughs/upload.md WORKTREE
```

WORKTREE means the current local source files. Use a commit for fixed sources. Git is required for committed sources.

The checker compares source excerpts and citations. A separate claim audit checks the explanation. Neither check proves the other's result.

See the [citation format](skills/code-walkthrough/references/citations.md) for revisions, excerpts, illustrative blocks, and exit codes.

## Update and troubleshoot

For a local plugin source, pull the checkout before refreshing the marketplace. Use the host's plugin update controls.

Claude supports `claude plugin update agentic-skills@agentic-skills-marketplace`. For Codex, refresh the marketplace and use its plugin controls.

Replace Cursor local copies explicitly, then reload. Standalone updates refuse changed destinations. Move the previous copy aside before installing again.

If a skill is missing, check uppercase `SKILL.md`, the destination, host trust settings, and discovery refresh.

If a connector is missing, supply the task description. If agents are unavailable, the workflow uses sequential roles and reports the review limit.

If the checker fails, correct the excerpt, citation, target, range, or revision. Do not relabel copied source as illustrative to hide a finding.

For mobile design, use actual project tokens and components. See the [project-context reference](skills/mobile-ui-ux-designer/references/project-context.md).

## Maintain and validate

Run the package tests and native Claude validators:

```sh
python3 -m unittest discover -s tests -v
claude plugin validate .
claude plugin validate .claude-plugin/plugin.json
claude plugin validate skills
```

See [validation.md](docs/validation.md) for observed results and compatibility limits. Test results do not establish interactive compatibility with every host.

Use the [project-instruction guide](skills/ai-dev-workflow/references/project-instructions.md) when maintaining repository instructions. It does not install global rules or mandatory hooks.

The skills use ASD-STE100 writing guidance. Technical terms and source excerpts need separate review. See the [language guide](skills/ai-dev-workflow/references/language.md).

| Previous path | Current path |
|---|---|
| `codex/agentic-learning-coach/skill.md` | `skills/online-tutor/SKILL.md` |
| `codex/mobile-ui-ux-designer/skill.md` | `skills/mobile-ui-ux-designer/SKILL.md` |

The existing skills retain their identities, normal discovery, and license declarations. Detailed teaching and design instructions now use supporting references.

Read the [PR analysis](docs/pr-319-analysis.md), [file comparison](docs/pr-319-comparison.md), and [best-practice review](docs/best-practices-review.md).

This package does not assign a repository-wide license to imported material. Source attribution and intentional adaptations appear in the review documents.
