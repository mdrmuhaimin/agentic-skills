# Validation evidence

## Current review: 2026-10-11

Package: **agentic-skills 0.1.0**. Platform: macOS. Tools: Python 3.13.4, Git 2.50.1, Claude Code 2.1.296, and Codex 0.159.2.

This review includes new engineering references, instruction maintenance, Ponytail practices, and the language pass. The four skills retain their identities and invocation policies.

### Automated checks

```sh
python3 -m unittest discover -s tests -q
claude plugin validate .
claude plugin validate .claude-plugin/plugin.json
claude plugin validate skills
git diff --check
```

The suite passed **55 tests**. All three Claude validators passed. The whitespace check passed.

| Area | Tests and coverage |
|---|---|
| Installer | 15 tests cover scope, selection, conflicts, repeat installation, resources, symlinks, unsafe paths, and dry runs |
| Walkthrough checker | 34 tests cover excerpts, elisions, citations, ranges, revisions, targets, working-tree sources, and repository boundaries |
| Package | Four tests cover manifests, marketplaces, skill identities, invocation policy, and reference links for all four skills |
| End to end | Two tests exercise installed resources and conflict refusal in temporary projects |

The end-to-end installation test covers all three hosts and both scopes. Each case installs all four complete skill folders.

Dry runs create no destination. Repeat installation keeps resource timestamps. Conflicting content prevents all selected copies, including skills not yet installed.

Each installed checker accepts committed baseline and explicit WORKTREE excerpts. It rejects an altered excerpt. Source files, Git HEAD, and the index stay unchanged.

The tests do not create editor settings or marketplace configuration. User-scope tests replace `Path.home()` with an isolated test path.

### Current host checks

| Check | Result | Limit |
|---|---|---|
| Claude native validators | All three passed on the actual package | No interactive invocation or model-routing test |
| Codex native project discovery | All four installed skill names appeared with repository scope and no discovery errors | Temporary project only, with no model call |
| Portable plugin schema | `plugin.json` passed Agent Plugins 1.0.0 validation | Schema validation does not test host behavior |
| Cursor schemas | Plugin and marketplace manifests passed the official schemas | No Cursor editor reload or invocation test |
| Skill common fields | All four passed skill-creator validation in temporary copies | The common validator does not accept the host extension field |
| Invocation extensions | Actual frontmatter and `agents/openai.yaml` passed separate checks | Metadata checks do not test implicit model routing |

For common-field validation, temporary copies omitted only `disable-model-invocation`. Claude's native validator examined the actual entrypoints with that field present.

The workflow and walkthrough keep `disable-model-invocation: true` and `allow_implicit_invocation: false`. Tutor and design keep normal discovery.

Codex discovery used the selective installer in a temporary project. The probe called `initialize` and `skills/list` with `forceReload: true`.

The probe used temporary SQLite state and logs through command-line overrides. It did not change user settings, marketplaces, or installed plugins.

The [configuration reference](https://developers.openai.com/codex/config-reference/) documents the runtime directory overrides. The earlier plugin installation test appears below as historical evidence.

Official schemas were fetched during this review. Temporary validation libraries remain outside the package. The committed helpers and tests use only Python's standard library.

### Independent review

A read-only reviewer compared the old tutor and design contracts with the new references. The reviewer also examined workflow approval, resume, retries, and publishing boundaries.

The review found two lost requirements. Both are restored:

- MEDIUM and HIGH lessons give recovery guidance after each checkpoint answer.
- Design approval applies before final delivery and implementation for the designated tasks.

A resolved blocking condition also requires approval before final delivery or implementation. This rule applies at all design sizes.

The reviewer ran all 55 tests and three Claude validators. A temporary checker mutation caused two expected test failures.

The mutation changed excerpt equality. It did not modify the canonical checker.

The reviewer checked the corrections. No actionable finding from that review stays unresolved.

### Independent workflow exercises

A separate agent followed the current skills in temporary Git projects. It used synthetic approvals and sequential role fallback.

| Scenario | Result |
|---|---|
| Missing ticket connector | Disclosed missing access, inspected code, and stopped at understanding approval |
| Approved specification, unapproved plan | Requested plan approval and made no product edits |
| Approved implementation | Kept the public API, user edits, original build base, and uncommitted policy |
| Exhausted corrective retry | Made no new edits and kept the failed task unresolved |
| Final review correction | Found an overflow regression after six tests passed, corrected it once, and refreshed final evidence |
| Corrected implementation | All eight fixture tests passed; the original Git index and HEAD stayed unchanged |
| Three walkthrough stages | Used baseline or explicit WORKTREE sources correctly; excerpt checks and separate prose audits passed |
| Altered excerpt | Source check rejected the incorrect text; a repaired excerpt passed |
| Unsupported prose claim | Excerpt check passed, but the separate factual audit rejected the unsupported claim |
| Tutor and design | Produced bounded LOW outputs with source checks, reader context, recovery, and explicit environment limits |
| Resolved LOW design blocker | Kept resolution approval pending and the design marked as a draft |
| MEDIUM tutor | Delivered 815 words in three lessons, with a specific recovery sentence after each answer |
| HIGH design-only flow | Produced a 2,433-word draft across three screens; design and blocking-resolution approvals stayed pending |

The fixture test exposed a product regression that syntax checks did not detect. The written review process found and corrected it.

Same-session review and audit were disclosed in the fixtures. The exercise did not test native worker dispatch.

The final targeted exercises checked the restored tutor and design contracts. Their content audits found no unresolved contract defect.

Fixture commands, outputs, hashes, and reports stayed outside this repository. They are not shipped as product examples.

### Language review

The pass uses [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf), dated January 15, 2025.

The reviewed prose includes the README, four skill entrypoints, their references, and the new practice review.

Instructions use active voice, simple verb forms, explicit conditions, and consistent terms. Procedural sentences use a 20-word limit. Descriptive sentences use a 25-word limit.

Paragraphs keep one topic and no more than six sentences. New prose contains no contractions or semicolons.

A temporary screen checked sentence length, paragraph size, contractions, and semicolons. Manual review corrected conditional instructions that the first screen did not classify correctly.

Word review used the official dictionary. Examples include `examine`, `get`, `applicable`, `keep`, and `limit` in place of less suitable general words.

Technical terms, identifiers, labels, quotations, and commands need their applicable terminology and counting rules. Original source excerpts and the MIT notice stay unchanged.

This review applies the standard's writing guidance. It does not establish full dictionary or grammar conformance or formal certification.

### Limits

Interactive host invocation, native worker execution, real ticket connectors, actual human approval responses, and cross-platform operation remain untested.

Tests use synthetic approvals and temporary projects. No live installation, marketplace submission, deployment, or release publication occurred during this review.

The source coverage and adaptations appear in [best-practices-review.md](best-practices-review.md). Historical findings below describe the earlier package state.

# Earlier validation: 2026-10-10

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
