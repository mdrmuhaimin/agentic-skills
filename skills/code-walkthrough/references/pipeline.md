# Sources and explanation contracts

## Stage and revision

Artifacts give context, not proof of implementation. Read actual progress, approvals, checks, and code; do not infer completion merely from ticket references in Git messages.

| Stage | Sources and coverage |
|---|---|
| Description/ticket only | Current committed code; today's flow, gap, open questions |
| Spec, no plan | Current code and requirement; distinguish draft/approved |
| Plan, build not started | Current code and proposed implementation |
| Build in progress | Recorded build-base code; plan/progress for intended changes |
| Complete and committed | Base for before; explicit finished commit for after |
| Complete, uncommitted | Base for before; explicit WORKTREE for current implementation |

With no recorded base, HEAD suffices only for pre-build description. If a before/after comparison lacks a reliable base, ask for it or describe current code only and disclose the limitation. With no Git/HEAD, use WORKTREE and don't claim an immutable baseline.

For WORKTREE, avoid concurrent edits to cited files. Capture file hashes before exploration and compare after checking, using Python `hashlib.sha256`. If sources change, refresh claims/excerpts before delivery. Record snapshot time and that later edits invalidate local citations. Do not create Git commits just to get citations.

The header names work, stage, revisions, source artifacts, date, and reading time. For uncommitted material add `Working-tree snapshot; citations may change after edits.` Use remote permalinks only when host and commit availability are known; otherwise local links relative to the walkthrough, with explicit revision labels.

## Explorer

Input: description, focus/audience, revision, optional spec/plan, notes destination. Trace entrypoints through processing/output. Cite exact locations, tests, and behavior-changing config. Copy rather than retype excerpts, usually about 15 lines each. Distinguish missing implementation from code not located. Write only notes.

## Fact sheet

Input: notes, context, stage/revisions, spec/plan, destination. Number claims `C1...`, each with evidence and verified/inferred/suspected status. Spec requirements are not proof that implementation exists. Re-read doubtful/new facts. Include exact excerpts `E1...`, useful diagrams, fictional-example details, glossary, unknowns.

Outline the reader's goal, people/systems, data journey, gap/change, proposed/built behavior, questions, glossary. Follow project primer headings if provided. An unsupported business motive stays unknown. Write only the fact sheet.

## Explanation

Read [writing.md](writing.md) for the teaching approach and illustrative sample before drafting. Use its running journey, reader questions, and useful takeaways in proportion to the code area's size.

Input: fact sheet, stage/revisions, audience, destination, date. Write from the fact sheet alone. Preserve uncertainty and copy excerpts/citations exactly. Use a friendly senior-colleague voice, one fictional example, and explain terms on first use. Choose ASCII/Mermaid for the renderer; diagrams clarify relationships rather than decorate every section. Explain excerpts in prose. Include takeaways where useful without imposing quizzes.

When refreshing, recheck retained claims, keep what still holds, and explain the stage/source change in one prologue line. Write only the walkthrough.

## Claim audit

Input: walkthrough, fact sheet, destination. Check factual claims, headings, and diagram labels against numbered claims. Flag unsupported conditions, numbers, causes, motives, or certainty. Clearly labelled fictional/hypothetical framing is allowed. Ignore style preferences.

Write `walkthrough line | claim text | closest claim ID or none | unsupported part`, one finding per line, or `none`. Write only the audit file and report independent versus same-session audit honestly.
