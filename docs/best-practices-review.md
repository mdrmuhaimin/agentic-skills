# Software development practice review

Review date: **2026-10-11**. Package: **agentic-skills 0.1.0**.

This update checks the source instructions, published engineering guidance, Ponytail, and technical language. It keeps four independent skills and their invocation policies.

## Source records

| Source | Record and use |
|---|---|
| NHOS `CLAUDE.md` and `CLAUDE_BP.md` | [Pinned source](https://github.com/simplexico/nhos-ai-workbench/tree/62e07a50ccfb002ca359495dbaf49bf44c8f3ab0), commit `62e07a50ccfb002ca359495dbaf49bf44c8f3ab0` |
| Addy Osmani, workflow | [My LLM coding workflow going into 2026](https://addyosmani.com/blog/ai-coding-workflow/), published January 4, 2026 |
| Addy Osmani, specifications | [How to write a good spec for AI agents](https://addyosmani.com/blog/good-spec/), published January 13, 2026 |
| Addy Osmani, instruction maintenance | [Audit your Agent files](https://addyo.substack.com/p/audit-your-agent-files), published August 27, 2026 |
| Andrej Karpathy | [Original post](https://x.com/karpathy/status/2015883857489522876), published January 26, 2026 |
| Ponytail | [Skill source](https://github.com/DietrichGebert/ponytail/blob/9b58c1ffb790c075ca32e70a89cf1d80588f4abf/skills/ponytail/SKILL.md), commit `9b58c1ffb790c075ca32e70a89cf1d80588f4abf` |
| Technical English | [Official ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf), January 15, 2025 |

The NHOS and Ponytail files were read at the recorded commits. External source files were kept outside this package. No upstream hooks or scripts ran.

X blocked direct access to the complete Karpathy post. Its public embed confirmed the author, date, and opening text.

A read-only mirror supplied the full post. Its substantive coding observations agree with the community adaptation referenced by `CLAUDE_BP.md`.

The community guidelines are not a skill published by Karpathy. This review does not claim his endorsement or independently verify the mirror's complete text.

## Coverage of the source instructions

The mappings below identify portable decisions. They do not transfer NHOS product policy to unrelated projects.

| Practice in `CLAUDE.md` | Maintained location |
|---|---|
| Examine before coding and state assumptions | `ai-dev-workflow/references/stages.md`, Understand |
| Explain users, current behavior, impact, affected paths, and exclusions first | `stages.md`, Understand |
| Use minimum code and focused changes | `references/roles.md`, Worker |
| Define observable success and checks | `stages.md`, Specify and Plan |
| Find, verify, classify, and disclose problems | `stages.md`, Specify |
| Get approval before external issue filing | `stages.md`, Specify and delivery boundary |
| Verify backend, frontend, UI, and AI changes appropriately | `references/engineering.md`, Verification and AI sections |
| Keep the required decision authority and evidence | `engineering.md`, AI behavior and evidence |
| Expose missing, conflicting, and unanalyzed evidence | `engineering.md`, AI behavior and evidence |
| Keep deterministic rules outside prompts | `engineering.md`, AI behavior and evidence |
| Use authoritative registries, thresholds, and exact reference text | `engineering.md`, Interfaces and AI sections |
| Keep required audit records and separate confidence from outcome | `engineering.md`, AI behavior and evidence |
| Authorize external contact separately | Entrypoint and `references/build.md`, Deliver |
| Keep product invariants and domain limits | `stages.md`, Specify |
| Distinguish time instants, dates, zones, and business calendars | `engineering.md`, Interfaces |
| Keep canonical statuses and payload contracts | `engineering.md`, Interfaces |
| Keep retry semantics when changing exception handling | `engineering.md`, External calls |
| Update server, client, fixture, and mock contracts together | `engineering.md`, Interfaces |
| Follow actual logging, style, locale, and component conventions | `references/roles.md` and design references |
| Do not edit generated or vendored files accidentally | `engineering.md`, Interfaces |
| Follow project Git and release-note rules | Entrypoint, plan record, and `build.md`, Deliver |
| Confirm hook configuration when expected checks do not run | `engineering.md`, Verification |
| Handle terminal states on all asynchronous paths | `engineering.md`, External calls |
| Avoid accidental repeated dispatch | `engineering.md`, External calls |
| Make failure states visible with recovery | `engineering.md`, External calls and design contracts |
| Bound external calls and keep side-effect-free health checks | `engineering.md`, External calls |
| Fetch only needed query data and measure performance | `engineering.md`, External calls |
| Check migration graph and execution authority | `engineering.md`, Interfaces |
| Keep test data aligned with real interfaces | `engineering.md`, Interfaces |
| Trace configuration through examples, deployment, and build layers | `engineering.md`, Interfaces |
| Expose placeholder or fixture fallbacks | `engineering.md`, Interfaces |
| Review dependency pins and unstubbed boundary checks | `engineering.md`, Dependencies |
| Treat uploaded content as untrusted | `engineering.md`, AI behavior and evidence |
| Diagnose AI errors before changing prompts and record evaluation results | `engineering.md`, AI behavior and evidence |
| Attribute disputed claims and avoid unsupported absence claims | `engineering.md`, AI behavior and evidence |
| Distinguish preview success from deployment proof | `engineering.md`, Infrastructure |
| Keep secrets and project-specific high-risk boundaries | `stages.md`, boundaries and `roles.md` |
| Maintain evidenced lessons and stale instructions | `references/project-instructions.md` |
| Do not invent answers to open product questions | `stages.md`, Understand and Specify |

The source's stack commands, ticket prefix, branch base, domain terms, and security policies stay project-specific examples.

The workflow reads equivalent rules from the target project. It does not prescribe NHOS statuses, business calendars, model settings, or release formatting.

## Coverage of `CLAUDE_BP.md`

The project-instruction guide keeps the source's useful maintenance practices:

- Keep a short decision guide instead of a knowledge base.
- Record commands, verification, boundaries, and non-obvious project constraints.
- Link to long or changing material.
- Use real code locations and confirmed evidence.
- Define Always, Ask first, and Never boundaries.
- Reserve emphasis for rules that need special attention.
- Use existing automation for mandatory checks when authorized.
- Remove stale, duplicate, or conflicting instructions.
- Review instruction changes through the project's usual process.
- Compare representative behavior before removing a useful rule.

The workflow keeps specification-before-code, small tasks, executable feedback, human review, and explainable changes.

Automatic prompt logs, session summaries, Git-learning hooks, and provider-specific configuration stay outside the approved package scope. Manual lesson maintenance does not require them.

## Review against Osmani and Karpathy

Osmani's workflow supports staged requirements, focused implementation, applicable context, checks, review, and recoverable changes. The package implements these decisions through its stage and role contracts.

The developer retains responsibility for approval and delivery. Optional native agents provide review without imposing a different model.

The local-commit recommendation stays a plan choice. The approved package contract still defaults to uncommitted changes.

Osmani's specification guidance supports testable outcomes, clear boundaries, applicable context, and proportional detail. Specifications and worker briefs now include those records explicitly.

His later audit guidance supports removing stale rules and testing instruction changes. Supporting references reduce entrypoint size without requiring every task to load every rule.

Karpathy's coding observations identify assumption errors, unnecessary abstraction, unrelated edits, and conceptual mistakes that syntax checks miss.

The worker and reviewer contracts address these risks. They require observable criteria, focused regression checks, and retention of behavior during refactoring.

They do not impose unlimited retry loops or parallel agent groups. Existing retry and delegation limits stay in force.

## Ponytail adaptation

The core skill and its repository instructions were read at the pinned commit. This session applies the core skill's complete-solution approach.

The worker contract now checks existing components, standard libraries, platform features, and installed dependencies before new code.

It also checks callers, tests, fixtures, configuration, and exports. Short code must stay readable. A shared root cause gets one complete fix.

Safety controls stay intact. Unrelated refactors stay outside scope. Necessary shortcuts record their limits and replacement conditions.

Verification stays part of completion. Delivery reports checks that could not run and material limits.

The package does not add Ponytail as a fifth skill or require its installation. Its level commands and permanent session activation are not workflow stages.

No upstream benchmark or performance claim becomes a package guarantee. See the [third-party notice](third-party-notices.md).

## Language and skill structure

The four skill entrypoints now use short instructions and applicable reference links. Tutor and design identities, license fields, discovery, and core contracts stay intact.

The earlier byte-retention result describes the previous migration. This update intentionally changes wording and moves detailed instructions into references.

The language pass applies imperative instructions, active voice, simple forms, consistent terms, and literal examples. It removes contractions and semicolons from new prose.

It uses 20-word procedural and 25-word descriptive sentence limits. It keeps descriptive paragraphs within six sentences.

Software terms, exact labels, identifiers, commands, and source excerpts require the standard's technical-term and counting rules. They are not ordinary prose synonyms.

The historical source reports retain their dated findings. This report and the current validation record identify subsequent changes.

The source checker validates citations, not language. Sentence-length screening cannot establish full dictionary or grammar conformance.

See the [technical-language guide](../skills/ai-dev-workflow/references/language.md) for review rules. The package does not claim formal ASD-STE100 certification.

## End-to-end evidence

See [validation.md](validation.md) for current automated results, native checks, independent exercises, and unresolved environment limits.

Scope approval does not authorize deployments, marketplace submissions, or changes to the user's installed skills. This update installs only into temporary test locations.
