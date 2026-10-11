# Stages and durable records

## Understand

Inspect entrypoints, tests, instructions, and existing patterns. State current behavior with `path:line` evidence and your best reading of the desired outcome. Ask focused questions only where answers affect the result and cannot be discovered. Do not manufacture confidence percentages or reject clear natural-language approval.

Confirm who benefits, what changes, why it matters, observable success, constraints, and exclusions. For a concrete task, summarize instead of running a ceremonial interview. Get approval before the spec stage. Preserve that understanding in the spec when authorized.

## Specify

Write the smallest spec that resolves implementation-relevant choices:

- Work identity, description/ticket, approved understanding, and cited current behavior.
- Requirements and measurable acceptance criteria, including important failure paths.
- Relevant interfaces, data changes, compatibility, and existing components to reuse.
- Verification commands discovered from the repository, prerequisites, and manual checks.
- Scope, accepted assumptions, and unresolved decisions. Blocking product questions return to the developer; do not guess them away.
- Findings table: finding, evidence, in/out of scope, status (`suspected`, `verified`, or `dismissed` with reason).

Record `Spec approval: pending` until the developer approves this version. Summarize, surface decisions, and wait. Requirement-changing revisions invalidate the affected approval until reconfirmed.

## Plan

Use vertical slices delivering observable behavior, ordered by dependencies. Bound tasks to focused implementation and checks; do not enforce an arbitrary file count. Identify reuse before prescribing new code.

Include this human-maintained record, adapted to existing project formats:

```markdown
# Plan: <work identity>
Spec: <relative link>
Understanding approval: <actual approval and date, or pending>
Spec approval: <actual approval and date, or pending>
Plan approval: pending
Commit policy: uncommitted
Build base: pending
Initial working tree: <existing changes and ownership, or clean>
Review mode: pending
Review result: pending
Final verification: pending

- [ ] Task 1: <observable outcome>
  - Depends on: <task IDs or none>
  - Files: <expected paths>
  - Complexity: simple | complex
  - Acceptance: <specific condition>
  - Verify: <exact command or manual observation>
  - Risk: <ordinary, or high-risk with reason and pre-task gate>
  - Result: pending

Checkpoint after Task <N>: <what the developer will review>
Final checks: <commands and observations covering acceptance criteria>
```

Choose checkpoints around coherent milestones rather than every edit. Mark high-risk tasks when consequences or project instructions warrant a pre-task decision, such as destructive data changes or live external writes. Writing a migration and applying it are different actions. A model prompt edit is not automatically an external action, but may need quality evaluation.

Present commands, risks, dependencies, and commit-policy choice at the gate. Record actual approval, not a synthesized one. Broader scope, new dependencies, or unexpected live-system actions return to the developer when not already authorized.

## Resume

Prefer explicit artifact links and identity over filename guessing. Recorded approvals determine the next stage:

| State | Next action |
|---|---|
| No approved understanding | Understand |
| Understanding approved, spec absent/unapproved | Specify or present spec for approval |
| Spec approved, plan absent/unapproved | Plan or present plan for approval |
| Plan approved, unfinished tasks | Build from first unfinished task |
| Tasks complete, final checks/review absent | Final checks and review |
| Checks/review complete | Report, or revise requested scope |

Do not infer approval from files, branches, or ticket status. For imported artifacts with missing approval, present the current version instead of repeating research.

Inspect status, task diff, and results before resuming. For an unfinished task with partial changes, identify ownership and ask whether to continue those edits or restart that task. Restarting never authorizes discarding unrelated work. Checked tasks need acceptance evidence; if missing or invalidated by later edits, verify them before relying on them.

Keep the recorded build base across interruptions. If unavailable locally, resolve it explicitly rather than silently replacing it with HEAD. A non-Git project may use a documented before snapshot, disclosing the loss of commit-based review.

Final verification and review must have recorded evidence too: commands/outcomes, reviewed revision or working-tree snapshot, review mode/verdict, and findings with their resolution. An absent record is pending even when every task is ticked. Later edits invalidate the affected evidence; rerun the relevant checks and review the final changed snapshot before delivering it.
