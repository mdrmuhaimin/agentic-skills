# PR #319: source analysis and portable adaptation

Source: [Simplexico / NHOS AI Workbench PR #319](https://github.com/simplexico/nhos-ai-workbench/pull/319), **NHOS-448: Claude Code conventions and the prompt-story, git-learning and mm-workflow plugins**. Baseline commit: `62e07a50ccfb002ca359495dbaf49bf44c8f3ab0`. The PR was open when examined on 2026-10-10; this import describes that commit rather than tracking a moving branch.

The follow-up audit inspected all 79 changed files, the PR description, and all four discussion comments. See [the file-by-file comparison](pr-319-comparison.md) for coverage, retained/adapted behavior, exclusions, and fixes found by independent review.

## What the PR contains

The PR adds repository conventions, prompt logging and summary commands, Git-history learning/rebase tooling, and an opt-in developer workflow with onboarding. Its workflow coordinates interview, specification, planning, sequential task workers, acceptance rechecks, checkpoints, and a fresh read-only review. Onboarding traces code, assembles a labelled fact sheet, writes a story-driven explanation, checks source excerpts, and audits prose claims.

Its strongest reusable property is the evidence chain: agreed intent → approved spec → executable checks → bounded tasks → verified implementation → review. Onboarding separately connects source evidence to what a developer reads. Those mechanisms survive changing editors, models, ticket trackers, or product stacks.

## Imported source components

- `tools/mm-workflow/skills/mm-workflow/SKILL.md` and its worker, quick-worker, scout, and reviewer contracts underpin `ai-dev-workflow`.
- `tools/mm-workflow/skills/onboard/SKILL.md` and the explorer, outliner, storyteller, and auditor contracts underpin `code-walkthrough`.
- `tools/mm-workflow/scripts/check_walkthrough.py` provides the original source-range and ordered-elision verification approach. The portable checker extends/reworks it with explicit uncommitted sources and stricter citation validation.
- The PR's pinned dependency, [Addy Osmani's agent-skills](https://github.com/addyosmani/agent-skills/tree/1401c8b8030e023baeebb31781a6653fe8e93026), was examined for the interview, spec, and task-planning behavior. The new instructions express those stages within the workflow; that plugin is not copied or required.

The instructions were rewritten and condensed around the approved portable behavior, rather than imported as a Claude plugin verbatim. Role contracts are ordinary references, not provider-native agent registrations.

The storyteller's writing guidance and short sample underpin `code-walkthrough/references/writing.md`. It retains a conversational teaching voice, one fictional journey, helpful diagrams, reader Q&A, and Remember lines, with an original domain-neutral sample. The developer identified Head First Java and Manning's approachable technical books as the intended teaching references. No book text is imported, and this style never substitutes for source citations or a claim audit.

## Adaptations

| Source constraint | Portable behavior |
|---|---|
| Typed Claude plugin command | Explicit skill request, with each host's manual-invocation metadata |
| Opus/Sonnet/Haiku requirements and transcript model reporting | Capability-based roles; selected model preserved; execution/review mode disclosed |
| Mandatory Linear-pattern ticket | Description, arbitrary task identity, or optional ID/URL; available connectors are read-only context sources |
| Required agent-skills plugin | Self-contained understanding, spec, and task-planning guidance |
| `docs/superpowers/` paths | Existing project conventions first; `docs/workflow/` defaults |
| Resume inferred from artifact presence | Recorded approvals, base revision, task evidence, and partial-change ownership |
| Agent-only pipeline | Native delegates when permitted; honest sequential fallback |
| Committed source checker | Commit or WORKTREE sources, mixed-revision citations, untracked files, and mutable-source disclosure |
| Uncited code fences could silently pass | Source required, or an explicit Example label; Mermaid still receives a prose/claim audit |
| Source checker did not compare target path/range | Target identity, line anchors, revision agreement, and known origin checked |

Original per-stage gates, sequential implementation, one corrective task retry, checkpoint/risk pauses, local-commit choice, and explicit publishing boundaries are preserved. Clear natural-language approvals count; literal command spellings and a particular provider's question UI are not required.

The existing tutor and mobile-design skills were moved without changing their bytes. Their declared names and discovery behavior remain intact. They are independently useful, not prerequisites for the workflow.

## Excluded and limitations

Prompt logging/redaction, PR/session-summary posting, Git learning, hook shims, rebasing, app run wrappers, and NHOS-specific business/security/convention rules are excluded. No hooks, connector registrations, editor permission settings, external posting, or model telemetry are installed by this package.

The checker verifies local evidence agreement, not prose accuracy, remote URL availability, or that a provided permalink was actually published. The claim audit handles explanatory certainty and causation. Supported remote citation shapes are GitHub/GitLab commit permalinks; other hosts use local links. Working-tree citations can go stale after edits. Same-session review/audit lacks the independent context of a separate agent.

Per-skill license declarations in the two pre-existing skills are retained. No repository-wide license was found in the examined source tree, so no blanket MIT claim is added for this imported package. Source attribution and pinned revisions are retained here and in the checker.
