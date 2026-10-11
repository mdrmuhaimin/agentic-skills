# Sequential build and final review

## Before implementation

Confirm current spec/plan approvals or explicit waivers. Record `Build base: <git rev-parse HEAD>` once and inventory existing staged, unstaged, and untracked changes. Do not reset, stash, stage, or include pre-existing work in task commits without authorization. Without Git, document a before snapshot.

State execution mode: native delegates where permitted, or sequential roles here. Delegation changes neither scope nor permissions. Do not change the selected model. If delegates cannot read the skill directory, include relevant role instructions in the brief.

## Each task

1. Check dependencies and pre-task risk gate. At a checkpoint/high-risk gate, summarize the concrete decision and wait. Preserve authorization already given for the same action; avoid duplicating host permission prompts.
2. Brief one worker using [roles.md](roles.md), or perform that role here: objective, artifacts, relevant code, acceptance check, scope, exclusions.
3. Wait, then inspect the actual diff, including new files, against the task and initial-change inventory. Read check output. Independently run acceptance checks when safe/runnable; for costly or side-effectful checks, examine evidence and record why they were not rerun.
4. On failure, give exact evidence for one corrective retry. A second failure preserves edits, leaves the task unchecked, and surfaces the failing check/prerequisite. An unavailable check is unverified unless the developer approves an observable alternative.
5. On a pass, tick the task and record changed paths, command/result, executor, and limitations. Under approved local-commit policy, stage only task changes and the plan. If shared-file edits cannot be safely separated from pre-existing work, leave them uncommitted and explain.

Replan material scope changes. In-scope defects may be corrected within the task; unrelated findings are recorded, not silently fixed. Do not repeatedly retry a blocked task or install undeclared dependencies to force a pass.

## Final checks and review

Run the final checks and project-required verification. Review the entire build against the approved requirements.

Save final commands/outcomes in the plan, including failed or unavailable checks. Record the reviewed commit or working-tree snapshot, mode, verdict, and findings/resolutions; a chat-only report cannot establish completion for the next session.

Give a fresh read-only reviewer the spec, plan, base, initial-change inventory, and check evidence. It inspects tracked/untracked changes and reports requirement/correctness gaps with citations. Prefer independent context, not a mandatory different model.

If unavailable, perform the same review here and record `Review mode: same-session; no independent context`. This fallback may complete the workflow but cannot be called fresh/independent. An explicitly requested independent review remains required.

Route an in-scope review finding to one bounded correction and verify it. Scope-expanding findings return to the developer. Remaining correctness findings mean not ready, regardless of checked tasks.

After any correction, mark affected task/check/review evidence pending until refreshed. Run the affected acceptance checks and relevant final checks, then have the reviewer confirm the correction and inspect its diff for regressions, or disclose the same-session fallback. Keep the correction bound; unresolved findings remain not ready.

Report task outcomes, final checks, review mode/verdict, findings, commits if any, and remaining decisions. Stop at delivery; build approval does not authorize publishing.
