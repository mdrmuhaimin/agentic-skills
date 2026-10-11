# Complete PR #319 comparison

Audited on **2026-10-10** against commit **62e07a50ccfb002ca359495dbaf49bf44c8f3ab0**. The PR head still matched that pin. All **79 changed files** were fetched and read: 17 workflow/onboarding files, two spec/plan artifacts, 29 Git-learning files, 23 prompt-story files, and eight conventions/wrapper/catalog/documentation files. The PR description and all four discussion comments were also examined; there were no submitted reviews or inline review comments.

Independent readers covered the workflow and design artifacts, onboarding/checker/tests, and excluded components. The coordinating review covered conventions, packaging, shared documentation, discussion, and the generated package. Downloaded file hashes were checked against the snapshot inventory. No upstream scripts or hooks were executed.

## Findings and changes

| Finding | Improvement made here |
|---|---|
| The short teaching sample was initially omitted | Restored dedicated `code-walkthrough/references/writing.md` with an original sample and the intended Head First Java/Manning teaching approach: a running fictional journey, reader questions, diagrams, and Remember lines |
| The source's live run found delegates could not read plugin resources | Coordinator explicitly reads the relevant references and supplies role instructions, writing guidance/sample, and necessary safe artifact content in the brief; inaccessible resources are not silently replaced with invented facts |
| Final checks/review could exist only in chat | Plan now records final verification, reviewed source state, verdict, findings/resolutions, and mode; absent records remain pending during resume |
| Review corrections could make earlier evidence stale | Affected task/final-check/review evidence is invalidated, checks are refreshed, and the final corrected diff is reviewed within the correction bound |
| Scout citation checking covered the spec but not the plan | Coordinator verifies scout evidence before it shapes understanding, specification, or planning; replies are bounded and secrets omitted |
| Mechanical checks could be superficial | Runnable/buildable changes need a check that exercises the relevant path; syntax-only success or a check that did not start cannot establish completion. Prose keeps proportionate checks |
| Retrieved evidence lacked an explicit authority boundary | Ticket/comments, source snippets, tool output, and role evidence cannot change permissions, scope, or recorded approvals |
| Quoted source-code fences could bypass exact comparison | Checker now normalizes blockquote containers, including nested quotes, while preserving source content; inline-list opening fences are rejected with an actionable message |
| Malformed prose links/revision suffixes silently disappeared | Source-like labels are recognized separately from valid citations; missing targets, malformed ranges, and invalid explicit revision tokens fail |
| Bare executable `...` was accepted as omitted source | Elision now requires a comment marker; literal Ellipsis is compared normally |
| The upstream negative later-commit test was lost | Corrupted after-excerpts are checked at full SHA, abbreviated SHA, and WORKTREE; the formerly surviving committed-only comparison-bypass mutation now fails |
| Source coverage was not visible to a maintainer | This report maps every changed file to its adaptation or intentional exclusion |

The checker weaknesses above were inherited or exposed by the broader portable contract; they were not all regressions introduced by this import. The missing sample, incomplete delegate brief guarantee, narrower scout requirement, durable-final-record gap, and lost negative test came from condensing the source.

## Intentional adaptations

- Keep one canonical catalog and thin host manifests, rather than separate provider copies or mandatory external skill dependencies.
- Preserve the selected model. Fixed Claude model/effort choices, model transcript reporting, provider permission-rule strings, and `/clear`/`/goal` handovers are excluded.
- Accept a description or arbitrary task identity with optional connector access. No Linear pattern, NHOS domain assumptions, mandated branch scheme, or forced `develop` base.
- Follow project artifact conventions first, with `docs/workflow` as the fallback. Preserve approval and verification evidence rather than inferring readiness from file presence or task checkboxes.
- Use one-level native delegation when available/permitted, with sequential same-session fallback disclosed. Writing workers remain sequential. Background walkthroughs and parallel explorers are not required: concurrent mutable sources would need coordination, and the source itself left interactive/background validation open.
- Pause at approved checkpoints and designated high-risk tasks. Use actual consequences/project instructions rather than requiring a new approval for every prompt, infrastructure, or CI edit already authorized.
- Default to uncommitted output; local per-task commits are an explicit plan-gate choice. Publishing remains a separate authorization.
- Retain the excerpt check and separate claim audit. Unlike the source auditor, the portable audit also covers factual diagram labels. Explicit WORKTREE sources support uncommitted completion without creating citation commits.
- Keep tutor/design skills independent. They are not stages or dependencies of development/onboarding.

Historical instructions in the source spec/plan describe superseded designs as well as the final design. The pinned skills/agents and later artifact amendments determine final source behavior; old model tables, nested orchestration, and handovers are not restored from historical steps.

## Evidence and remaining limits

The package suite now passes **53 tests**. New cases first demonstrated the checker failures, then passed after correction. Native Claude marketplace/manifest/component validators pass. Independent synthetic exercises confirmed durable final-state resume and a restricted writer brief containing the teaching sample. See [validation.md](validation.md) for host checks and the distinction between synthetic exercises and runtime-tested discovery.

The source PR reports live sessions, a generated NHOS-412 walkthrough/fact sheet, and experiment E1. The pinned tree contains no workflow walkthrough directory, fact-sheet output, sandbox output, or session transcripts. Those originals cannot be inspected through this PR; their reported outcomes are evidence claims in the PR/plan, not reproduced results. E1's source-size/performance measurements are not promises about this portable package.

Cursor compatibility remains schema/documentation checked; interactive routing, real connectors, host-enforced delegation/resource restrictions, and cross-platform execution remain untested. Python helpers use a documented citation/fence grammar, not a full Markdown parser. There is no new repository-wide license claim, live installation, publication, or automatic logging/history-learning behavior.

## Every changed file

Paths below are relative to the source repository at the pinned commit. “Excluded” means deliberately outside the approved import, not missed during review. Mapped paths are relative to this package root.

| Source path | Disposition / package counterpart |
|---|---|
| `.gitignore` | Excluded logging/sandbox ignore additions; this package independently ignores helper caches |
| `CLAUDE.md` | Examined conventions; generic evidence/verification principles retained in workflow references; product rules excluded |
| `CLAUDE_BP.md` | Examined writing/process principles; project instructions remain authoritative; no global provider rules installed |
| `docs/superpowers/plans/2026-10-07-nhos-448-claude-code-tooling.md` | Fully examined design/live-test/experiment evidence; not imported as a generic task plan |
| `docs/superpowers/specs/2026-10-07-nhos-448-claude-code-tooling.md` | Fully examined requirements/findings/amendments; not imported as a generic product spec |
| `git_learning.md` | Excluded product history/lessons artifact; generic evidence-authority lesson retained |
| `scripts/dev_run_be.sh` | Excluded product/macOS startup and migration wrapper |
| `scripts/dev_run_fe.sh` | Excluded product/macOS frontend wrapper |
| `tools/.claude-plugin/marketplace.json` | Adapted into three host catalogs exposing one root plugin; external skill dependency removed |
| `tools/README.md` | Adapted relevant installation/invocation/troubleshooting into README.md; excluded commands omitted |
| `tools/git-learning/.claude-plugin/plugin.json` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/README.md` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/hooks/hooks.json` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/scripts/ensure_hooks.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/scripts/errors.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/scripts/finalize.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/scripts/gitutil.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/scripts/learn.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/scripts/pending_notice.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/scripts/prompts.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/scripts/run_claude.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/scripts/settings.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/scripts/tracker.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/scripts/triage.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/skills/finalize-learning/SKILL.md` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/skills/git-learning/SKILL.md` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/tests/conftest.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/tests/test_ensure_hooks.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/tests/test_finalize.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/tests/test_gl_settings.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/tests/test_guard.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/tests/test_hooks_json.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/tests/test_learn.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/tests/test_pending_notice.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/tests/test_run_claude.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/tests/test_shims.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/tests/test_smoke.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/tests/test_tracker.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/git-learning/tests/test_triage.py` | Excluded Git-history learning/rebase/hooks/memory component; fully reviewed |
| `tools/mm-workflow/.claude-plugin/plugin.json` | Adapted into root and host plugin manifests; shared skills autodiscovery |
| `tools/mm-workflow/README.md` | Adapted into README.md, source analysis, and validation evidence |
| `tools/mm-workflow/agents/onboard-auditor.md` | code-walkthrough/references/pipeline.md; bounded claim audit extended to factual diagrams |
| `tools/mm-workflow/agents/onboard-explorer.md` | code-walkthrough/references/pipeline.md; revision-bound tracing/notes |
| `tools/mm-workflow/agents/onboard-outliner.md` | code-walkthrough/references/pipeline.md; bounded labelled facts/outline/glossary/questions |
| `tools/mm-workflow/agents/onboard-storyteller.md` | code-walkthrough/references/{pipeline,writing}.md; original portable sample and teaching approach |
| `tools/mm-workflow/agents/quick-worker.md` | Shared worker contract with proportional real-check guidance; no duplicate agent registration |
| `tools/mm-workflow/agents/reviewer.md` | ai-dev-workflow/references/{roles,build}.md; fresh read-only review or disclosed fallback |
| `tools/mm-workflow/agents/scout.md` | ai-dev-workflow/references/roles.md; narrow read-only questions, concise evidence, coordinator recheck |
| `tools/mm-workflow/agents/worker.md` | ai-dev-workflow/references/roles.md; reuse/tests/evidence contracts, no fixed model |
| `tools/mm-workflow/scripts/check_walkthrough.py` | skills/code-walkthrough/scripts/check_walkthrough.py; extended/repaired citation checker |
| `tools/mm-workflow/scripts/model_report.py` | Excluded Claude-specific transcript/model telemetry |
| `tools/mm-workflow/skills/mm-workflow/SKILL.md` | skills/ai-dev-workflow/SKILL.md and references/{stages,build,roles}.md |
| `tools/mm-workflow/skills/onboard/SKILL.md` | skills/code-walkthrough/SKILL.md and references/{pipeline,citations,writing}.md |
| `tools/mm-workflow/tests/test_check_walkthrough.py` | Behavior compared with tests/test_check_walkthrough.py; later-commit negative restored; new portable cases added |
| `tools/mm-workflow/tests/test_model_report.py` | Excluded telemetry tests; reviewed to understand the omitted helper |
| `tools/mm-workflow/tests/test_structure.py` | Portable identity/reference/invocation checks in tests/test_package.py; fixed-model/provider assertions excluded |
| `tools/prompt-story/.claude-plugin/plugin.json` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/README.md` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/hooks/hooks.json` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/scripts/errors.py` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/scripts/log_prompt.py` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/scripts/note_understanding.py` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/scripts/nudge_pr_story.py` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/scripts/redact.py` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/scripts/session_rule.py` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/scripts/settings.py` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/scripts/setup.py` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/skills/post-conversation-summary/SKILL.md` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/skills/pr-story/SKILL.md` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/tests/conftest.py` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/tests/test_errors.py` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/tests/test_log_prompt.py` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/tests/test_note_understanding.py` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/tests/test_nudge.py` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/tests/test_redact.py` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/tests/test_session_rule.py` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/tests/test_settings.py` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/tests/test_setup.py` | Excluded prompt logging/summary/posting component; fully reviewed |
| `tools/prompt-story/tests/test_skills.py` | Excluded prompt logging/summary/posting component; fully reviewed |
