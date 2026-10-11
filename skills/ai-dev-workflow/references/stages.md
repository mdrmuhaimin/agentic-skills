# Stages and work records

## Understand

Read the applicable project instructions, entrypoints, tests, and existing patterns. Examine each affected entry path. Distinguish current behavior from the requested change.

Present a short explanation in this order:

1. Identify the users and the real-world flow.
2. Describe current behavior with recently checked `path:line` evidence.
3. Explain the problem and its effect on each affected user.
4. Identify unaffected paths, exclusions, and unresolved product decisions.
5. State the desired outcome and measurable success criteria.

Use business terms before code terms. Define unfamiliar terms. Do not invent business motives or silently select between materially different interpretations.

State assumptions and trade-offs. Present a simpler complete option when applicable. Ask only questions that affect the result and that available evidence cannot answer.

For a concrete task, use a short explanation instead of an extensive interview. Get approval before the specification stage.

## Specify

Write the smallest specification that resolves the necessary implementation decisions. Include:

- The task identity, source context, and approved understanding.
- Current behavior with evidence for each applicable entry path.
- Requirements, exclusions, and measurable acceptance criteria.
- Important interfaces, data changes, compatibility needs, and components to reuse.
- Applicable product invariants and engineering risks.
- Exact check commands, prerequisites, expected results, and manual checks.
- Assumptions and unresolved decisions.
- A findings table with evidence, scope, status, and reproduction steps.

Use [engineering.md](engineering.md) only for risks applicable to this change. For new interfaces or unfamiliar libraries, verify behavior against official documentation for the installed version.

Record project boundaries as **Always**, **Ask first**, and **Never**. These boundaries describe actual project requirements. They do not add unrelated approval requirements.

Tell the developer about a new bug or gap when you find it. Record the finding as `suspected` until evidence confirms it. Include safe reproduction steps. Mark a rejected finding `dismissed` with a reason.

Include verified findings that meet the acceptance criteria in the plan. Keep unrelated findings outside the task. Draft any proposed external issue or comment before you request publication approval.

Record `Spec approval: pending` until the developer approves this version. Save the understanding in the specification. Reconfirm approval after changes to requirements.

## Plan

Use ordered tasks that each produce an observable result. Include dependent callers, contracts, tests, fixtures, and configuration in the affected-file list.

Identify existing components before new code. Bound each task to a focused change and its checks. Do not use an arbitrary file-count limit.

Use this record, or the equivalent project format:

```markdown
# Plan: <task identity>
Spec: <relative link>
Understanding approval: <actual decision and date, or pending>
Spec approval: <actual decision and date, or pending>
Plan approval: pending
Commit policy: uncommitted
Build base: pending
Initial working tree: <existing changes and ownership, or clean>
Review mode: pending
Review result: pending
Final verification: pending

- [ ] Task 1: <observable outcome>
  - Depends on: <task IDs or none>
  - Files: <affected paths, including callers and tests>
  - Context: <relevant specification sections and source references>
  - Complexity: simple | complex
  - Acceptance: <observable condition>
  - Verify: <exact command or manual observation>
  - Risk: <ordinary, or high-risk with reason and pre-task decision>
  - Attempts: 0; corrective retries used: 0
  - Result: pending

Checkpoint after Task <N>: <result for the developer to review>
Final checks: <checks that cover the acceptance criteria>
```

Place checkpoints after coherent milestones. Mark high-risk tasks from their actual consequences and project rules. Distinguish writing a migration from applying it.

At the plan decision, present dependencies, checks, risks, and the local commit policy. Keep the default of uncommitted changes. Do not commit code that you cannot explain.

Return new scope, dependencies, or live-system actions to the developer when existing authorization does not cover them.

## Resume

Use recorded approvals to select the next action:

| Recorded state | Next action |
|---|---|
| Understanding lacks approval | Understand |
| Understanding approved, specification absent or unapproved | Specify or present the existing specification |
| Specification approved, plan absent or unapproved | Plan or present the existing plan |
| Plan approved, tasks unfinished | Resume the first unfinished task |
| Tasks complete, final checks or review absent | Run final checks and review |
| Final checks and review complete | Report the result or handle the requested revision |

Do not infer approval from filenames, branches, or ticket status. Present an existing artifact when approval is missing. Do not repeat research without a reason.

Examine changes and check results before implementation resumes. Identify the owner of partial task changes. Ask whether to continue or restart those changes when the choice is unclear.

A restart never authorizes removal of unrelated work. Keep the recorded corrective-retry count across sessions. Do not reset a failed task's retry allowance.

Keep the original build base. Resolve an unavailable base explicitly. For a non-Git project, use a recorded before snapshot and disclose the review limit.

Require acceptance evidence for completed tasks. Require final commands, results, reviewed source state, review mode, verdict, and finding resolutions.

Mark absent records `pending`. Later edits invalidate affected evidence. Repeat the affected checks and review the corrected source state before delivery.
