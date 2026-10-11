# Source and explanation contracts

## Stage and revision

Artifacts provide context. They do not prove implementation. Examine progress, approvals, checks, and actual code.

| Stage | Required sources |
|---|---|
| Description or ticket only | Current committed code, the gap, and open questions |
| Specification without a plan | Current code and draft or approved requirements |
| Plan before implementation | Current code and proposed changes |
| Implementation in progress | Recorded build-base code and intended changes from the plan |
| Complete and committed | The base for before and an explicit finished commit for after |
| Complete and uncommitted | The base for before and explicit WORKTREE sources for after |

Without a recorded base, use HEAD only before implementation starts. For an unreliable before/after comparison, request a base or explain current code only.

Without Git or HEAD, use WORKTREE. Disclose that the source is mutable.

For WORKTREE sources, prevent concurrent edits to cited files. Record file hashes before exploration. Compare them after checking with Python `hashlib.sha256`.

If sources change, refresh the claims and excerpts. Record the snapshot time. Explain that later edits invalidate local citations.

Do not create commits only to get citations. Use remote permalinks only when the host and commit availability are known.

Use local links relative to the walkthrough otherwise. Add explicit revision labels for old sources.

The header identifies the task, stage, revisions, source artifacts, date, and reading time. For uncommitted sources, add `Working-tree snapshot; citations may change after edits.`

## Explorer

Input: the task, focus, reader context, revision, optional specification and plan, and notes destination.

Trace the entrypoints through processing and output. Cite locations, tests, and configuration that affects behavior. Copy excerpts instead of retyping them.

Keep an excerpt near 15 lines when practical. Distinguish missing implementation from code that you did not locate. Write only the notes.

## Fact sheet

Input: the notes, context, stage, revisions, artifacts, and destination.

Number claims `C1`, `C2`, and so on. Give each claim evidence and a `verified`, `inferred`, or `suspected` status.

Requirements do not prove that implementation exists. Recheck doubtful or new facts. Number exact excerpts `E1`, `E2`, and so on.

Include useful diagrams, fictional example details, a glossary, and unknowns. Outline the reader's goal, people, systems, data flow, gap, and proposed or completed behavior.

Follow project explanation headings where applicable. Keep unsupported business motives unknown. Write only the fact sheet.

## Writer

Input: the fact sheet, stage, revisions, reader context, destination, and date.

Read [writing.md](writing.md) before drafting. Use its sample, questions, and takeaways in proportion to the code area's size.

Write from the fact sheet alone. Keep uncertainty. Copy excerpts and citations exactly. Explain terms at first use.

Use one fictional example to follow the verified flow. Use ASCII diagrams or Mermaid when the destination supports it. Explain each excerpt in prose.

Do not impose quizzes. When refreshing, recheck retained claims. State the stage or source change in one opening sentence.

Write only the walkthrough.

## Claim auditor

Input: the walkthrough, fact sheet, and audit destination.

Check factual prose, headings, diagram labels, questions, and takeaways against the numbered claims. Flag unsupported conditions, numbers, causes, motives, or certainty.

Clearly labeled fictional examples are permitted. They do not establish system behavior. Ignore style preferences during the factual audit.

Record each finding with this format:

```text
walkthrough line | claim text | closest claim ID or none | unsupported part
```

If the audit has no findings, write `none`. Write only the audit file. Report independent or same-session audit mode accurately.
