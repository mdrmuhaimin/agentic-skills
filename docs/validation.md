# Validation evidence

Validated on **2026-10-10** for plugin **agentic-skills 0.1.0**, on macOS. Helpers require Python 3.10+ and Git; validation ran with Python 3.13. Native tools: Claude Code **2.1.296**, Codex CLI/app-server **0.159.2**. These are observations of this checkout, not a guarantee about every host version.

## Automated helper and package checks

```sh
python3 -m unittest discover -s tests -q
```

Result after the comprehensive source comparison: **53 tests passed**.

| Area | Coverage |
|---|---|
| Selective installer, 15 tests | Explicit selection/scope; project and isolated user destinations for all three hosts; dry runs; complete resource copying; unchanged repeat installs; all-destination conflict preflight; extra resources; missing skills; traversal/symlink refusal; cache exclusions; actual walkthrough checker and invocation metadata copying |
| Walkthrough checker, 34 tests | Exact/altered excerpts; quoted/nested fences; rejection of inline-list fences; indentation; trailing whitespace; comment-only ordered/all-elided excerpts; literal Ellipsis; invalid/missing ranges/files; missing/malformed citations and revision suffixes; wrong targets; fence closure; explicit illustrative/diagram exemptions; mixed revisions, including corrupted after-excerpts at full/short SHAs and WORKTREE; committed and dirty/untracked sources; local/remote links; origin identity; SSH ports; UTF-8 under an ASCII locale; scope escapes; non-Git WORKTREE; invalid revisions |
| Package, 4 tests | Consistent manifest identity/version; canonical skill paths; one root plugin per catalog; explicit availability; skill identity and manual-invocation policies; supporting links outside illustrative examples |

A mutation probe changed a **temporary copy** of the checker to bypass exact excerpt comparison. Both altered-character and altered-indentation assertions failed as expected. The canonical checker was never modified by that probe.

Git baseline bytes were compared with both migrated files: `online-tutor/SKILL.md` and `mobile-ui-ux-designer/SKILL.md` are unchanged from their previous lowercase entrypoints. `git diff --check` passed, and an additional scan of tracked/new textual package files found no trailing whitespace.

## Host compatibility

| Host/format | Check and result | Limit |
|---|---|---|
| Claude Code | `claude plugin validate .`, `claude plugin validate .claude-plugin/plugin.json`, and `claude plugin validate skills`: all passed without warnings | Native manifest/component validation; no interactive Claude session or model-routing test |
| Codex plugin | In a temporary `CODEX_HOME`: add local marketplace, list available plugins, install `agentic-skills@agentic-skills-marketplace`, initialize app-server, request `skills/list` | Native installation/discovery passed; no live user configuration changed |
| Codex discovered skills | Exactly four plugin skills: `agentic-skills:ai-dev-workflow`, `agentic-skills:code-walkthrough`, `agentic-skills:online-tutor`, `agentic-skills:mobile-ui-ux-designer`; discovery errors empty | Discovery also reads existing global skills; assertions filtered by this plugin's ID |
| Codex standalone | Selective installer copied workflow/walkthrough into a temporary project's `.agents/skills`; refreshed `skills/list` returned both names with repository scope and no errors | Project discovery tested; user-path copying tested with an isolated mocked home |
| Portable manifest | Validated `plugin.json` against the [Agent Plugins 1.0.0 schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json): passed | Root skills discovery was additionally demonstrated by Codex |
| Cursor | `.cursor-plugin/plugin.json` and `.cursor-plugin/marketplace.json` passed the official [plugin schema](https://github.com/cursor/plugins/blob/main/schemas/plugin.schema.json) and [marketplace schema](https://github.com/cursor/plugins/blob/main/schemas/marketplace.schema.json) | Schema/documentation compatibility only; no Cursor editor reload/discovery or interactive invocation test |

For Codex native validation, the tested commands were `codex plugin marketplace add <checkout> --json`, `codex plugin list --available --json`, and `codex plugin add agentic-skills@agentic-skills-marketplace --json`. The catalog was available before installation and reported version `0.1.0`. Temporary plugin caches/configuration were removed with the fixture.

All four skills passed skill-creator's `quick_validate.py` for common fields. That validator does not permit the documented host extension `disable-model-invocation`, so validation used temporary entrypoint copies with **only that field removed**. Actual canonical frontmatter was separately parsed and checked: workflow/walkthrough declare `disable-model-invocation: true`, and both `agents/openai.yaml` files declare `policy.allow_implicit_invocation: false`. The other two skills retain ordinary discovery. Claude's native validation covered actual entrypoints. Implicit model routing was not exercised through model calls.

Schema/YAML validation libraries were installed only in a temporary validation environment. The installer, checker, and committed test suite remain standard-library-only.

## Independent skill exercises

A separate agent read the skill instructions and exercised synthetic Git fixtures. These were forward tests of the written instructions, with synthetic approval records; they did not solicit real approvals or contact external systems.

| Scenario | Observed behavior |
|---|---|
| Description with no ticket connector | Inspected source and prepared understanding; disclosed missing access; stopped at the understanding gate without implementation |
| Existing approved spec, unapproved plan | Presented the existing plan for approval; file existence did not supply approval |
| Approved build, uncommitted policy | Added four regression cases, observed three initial failures, implemented the approved behavior, inspected changes, verified all four checks, recorded task evidence and same-session review; changes remained uncommitted |
| Interrupted task with unrelated edits | Preserved both partial task edits and unrelated notes; stopped at continue/restart decision |
| Failed acceptance | Used one corrective retry; a remaining failing negative-input check left the task unchecked and surfaced the failure |
| Pending high-risk task gate | Overall plan approval did not authorize the pending deletion; no implementation/acceptance command ran, task stayed unchecked, fixture data hash stayed unchanged |
| Before and during build walkthroughs | Used committed/build-base sources and distinguished current behavior from intended changes; excerpt checks passed |
| Completed, uncommitted walkthrough | Used explicit baseline and WORKTREE sources; both excerpts passed; source hashes remained unchanged |
| Unsupported prose | Injected “The free-shipping rule increases checkout conversion.” Exact excerpts still passed; the separate fact-sheet audit rejected the unsupported causal claim. One revision restored uncertainty, then check/audit passed |
| Unavailable delegation | Sequential roles and same-session review/audit were disclosed; no claim of independent context |

Independent helper review found two portability defects: locale-dependent Git blob decoding and SSH origins with explicit ports. Both were fixed and covered by regression tests. No remaining actionable helper/manifest finding was reported.

The [comprehensive PR comparison](pr-319-comparison.md) subsequently found inherited checker weaknesses in quoted fences, malformed prose citations/revision tokens, and literal Ellipsis handling, plus a missing negative later-commit assertion. All were corrected. A temporary mutation bypassing excerpt comparison only for explicit committed revisions passed the old checker tests; the restored corrupted-after-excerpt assertion now rejects that mutation. No canonical file was altered by mutation testing.

Additional synthetic workflow exercises covered all tasks ticked with absent final verification/review records, and a corrected snapshot newer than previous passing evidence. They selected final verification/review and invalidated affected evidence respectively; three real regression checks passed in each fixture. The instructions now require durable final records and rechecking review corrections. The walkthrough coordinator now supplies role instructions and writing guidance/sample in the brief when delegates cannot access installed skill resources.

Native worker delegation, actual ticket connectors, real human approval responses, cross-platform execution, and interactive host model invocation remain untested. No marketplace submission, live installation, push, or release publication was performed.
