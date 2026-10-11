# Implementation and final review

## Before implementation

Confirm the specification and plan approvals, or explicit stage waivers. Record the build base once with `git rev-parse HEAD`.

List existing staged, unstaged, and untracked changes. Identify their owners. Do not reset, stash, stage, or commit existing work without authorization.

Without Git, record a before snapshot. State whether native workers are available. If workers cannot access skill references, include the needed instructions in their briefs.

Read the applicable sections of [engineering.md](engineering.md). Record pre-existing check failures before you change code when safe and practical.

## Each task

1. Check the dependencies and any pending risk decision.
2. At an agreed checkpoint, present the concrete result or decision and wait.
3. Brief one worker with the contract in [roles.md](roles.md), or perform that role in this session.
4. Examine the actual changes, including new files, after the worker finishes.
5. Compare the changes with the task and the initial-change list.
6. Read the check output.
7. Independently repeat safe acceptance checks when practical.
8. Record the result before you select the next task.

For costly or side-effectful checks, examine the available evidence. Record why you did not repeat the check. A check that cannot run stays unverified.

On failure, supply exact evidence for one corrective retry. Record the attempt and retry count in the plan. A second failure leaves the task unchecked.

Keep changes when a task stays blocked. Report the failed check or missing prerequisite. Do not add undeclared dependencies or weaken acceptance criteria to get a pass.

On success, record changed paths, commands, results, executor, and limits. Under an approved local-commit policy, stage only the task changes and its plan record.

If existing edits share the same file, separate them safely before staging. Otherwise, leave the task uncommitted and explain the conflict.

Correct in-scope defects within the task. Report unrelated findings without silently fixing them. Replan material scope changes.

## Final checks

Run the planned final checks and required project checks. Compare every acceptance criterion with evidence from the final source state.

Include applicable runtime, interface, failure-path, and AI-output checks. Use [engineering.md](engineering.md) to identify applicable checks. A build or syntax check alone cannot establish correct behavior.

Save commands and outcomes in the plan. Include failed and unavailable checks. Record the reviewed commit or working-tree snapshot.

## Final review

Give a fresh read-only reviewer the specification, plan, build base, initial-change list, and check evidence. Use the reviewer contract in [roles.md](roles.md).

The reviewer checks the complete tracked and untracked change. It does not edit source files or affect live systems.

If an independent reviewer is unavailable, perform the review in this session. Record `Review mode: same-session; no independent context`. An explicitly requested independent review stays required.

Route an in-scope review finding to one corrective pass. Recheck the affected behavior. Return scope-expanding findings to the developer.

After corrections, mark affected task, check, and review evidence `pending`. Repeat the applicable checks. Review the correction and its effect on the complete change.

Keep the correction bound across interruptions. Unresolved correctness findings mean `not ready`, regardless of completed task checkboxes.

## Deliver

Record the review verdict, finding resolutions, and remaining decisions. Report task outcomes, final checks, review mode, limits, and local commits.

Update applicable project documentation and release notes when project rules require them. Keep release text factual. Do not claim a publication action that did not occur.

Stop at delivery. Implementation approval does not authorize a push, merge, deployment, or external post.
