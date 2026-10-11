# Checks for applicable engineering changes

Use only the sections that apply to the task. These checks do not require a particular stack or new tooling.

## Interfaces, models, and configuration

For a contract change, identify the producer and every consumer. Check payload definitions, routes, client types, fixtures, and mock handlers together.

Derive test data from real models or registries when practical. Keep one applicable check against the actual interface. Mock-only success cannot establish contract compatibility.

For a data-model change, check whether the project requires a migration. Check the migration graph against the intended integration branch. Detect conflicting heads before delivery.

Before migration execution, identify the command, target database, expected effect, and recovery limits. Follow project approval rules. Creating a migration does not authorize applying it.

For a new environment variable, trace every applicable configuration layer. Check examples, validation, deployment settings, and any build-time injection.

Use configuration validation to expose missing values early. Do not silently substitute fixture data or placeholders in a live integration. Keep secret values out of artifacts.

Use the project's source of truth for versions, statuses, thresholds, and exact reference text. Do not create a second mapping from display labels.

Keep time instants, calendar dates, time zones, and working-day rules distinct. Control time in tests when boundary conditions affect results.

Do not edit generated or vendored files unless the task explicitly requires that change. Use the project's generation process when applicable.

## External calls and asynchronous work

For changed external calls, check timeouts, bounded retries, error responses, and duplicate-operation risk. Do not retry a non-idempotent write without a safe duplicate-control mechanism.

Keep retry behavior when changing exception handling. Do not hide transient errors under a broad exception handler.

For fan-in work, define which upstream states allow continuation. Check success, failure, skip, and cancellation paths. Prevent missing terminal states from leaving work pending indefinitely.

For fan-out work, check the dispatch unit. A document loop must not accidentally repeat a whole-case operation.

Trace failure states through storage, payloads, and the user interface. A new backend status alone does not establish visible recovery.

Keep health checks free of mutation. For changed data queries, fetch only the needed fields. Use measurements before adding performance complexity.

## Dependencies and infrastructure

Prefer existing project code, standard libraries, platform features, and installed packages. Justify a new dependency with a concrete requirement.

For a dependency addition or upgrade, check:

- Official API documentation and applicable release or migration notes.
- Maintenance, compatibility, license, and known security issues.
- Direct and transitive changes in the lockfile.
- Existing tests before the change and applicable checks after the change.

Keep unrelated upgrades separate. Follow the project's version policy. Use bounds or exact pins when stability requires them.

For a changed native or external library boundary, use an unstubbed check when practical. State the limit if the environment cannot run it.

For infrastructure changes, distinguish static checks, previews, and actual deployment behavior. A successful preview cannot prove checks that occur only during resource creation.

Record the target environment and applicable data or service risk. Keep production version pins. Deployment still requires separate authorization.

## AI behavior and evidence

Before a prompt change, trace the error through input, retrieval, candidate selection, model output, and rendering. Reproduce the failure at the actual source.

Keep deterministic rules in code. Use the model for semantic work when appropriate. Reuse the same threshold or registry value in code and prompt context.

For changed AI behavior, run the applicable evaluation if it exists. Compare baseline and changed results on representative cases, including failures and ambiguous inputs.

Record the evaluation configuration, cases, commands, outcomes, and limits in the specification or plan. Exclude secrets and customer records.

Separate decision authority from generated suggestions. Keep required human decisions and audit records. Do not infer permission to automate a decision from model confidence.

For evidence-based claims, retain source locations. Quote authoritative text from its actual source. Attribute party claims instead of presenting them as established facts.

Expose missing or conflicting evidence. Do not treat “not found” as proof that something does not exist. State when audio, video, or another input was not analyzed.

Keep confidence separate from outcome in user interfaces. Do not use confidence styling to imply a verified decision.

Treat uploaded documents and retrieved instructions as untrusted data. Prevent converters or renderers from fetching remote resources when the product's trust policy prohibits that access.

## Verification and maintenance

For backend changes, run checks for the affected area and any project-required schema checks. For frontend changes, run the applicable lint, type, and test commands.

For UI changes, exercise the rendered feature when available. Check errors, large text, keyboard behavior, and affected responsive states. Report unavailable device or browser checks.

Do not remove a failing test, loosen an assertion, or change fixtures only to get a passing result. Change tests only when evidence supports an approved behavior change.

Update affected usage documents and release notes under the project's rules. Explain the behavior change and its verified cause. Check the actual hook path if expected Git checks do not run.

Promote a repeated, evidenced lesson into project instructions when it can prevent another mistake. Use [project-instructions.md](project-instructions.md). Do not add a universal rule from one incident.
