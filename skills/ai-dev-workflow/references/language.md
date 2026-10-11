# Technical English for workflow records

Use the writing rules and dictionary in [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf).

This reference summarizes applicable rules. It does not replace the standard or certify compliance.

## Write instructions

- Use the imperative form: “Run the acceptance test.”
- Put a required condition before the action: “If the test fails, record the failure.”
- Give one instruction per sentence, except actions that must occur together.
- Use no more than 20 words in a procedural sentence.
- Identify the actor when more than one role can act.

## Write explanations

- Use active voice. Use passive voice only when the actor is unknown.
- Use simple verb forms.
- Use no more than 25 words in a descriptive sentence.
- Keep one topic per paragraph.
- Use no more than six sentences per paragraph.
- Introduce information in the order that the reader needs it.

## Use consistent words

Use dictionary-approved words with their approved meanings and parts of speech. Define necessary software terms before first use. Use one term for one concept.

Use approved technical nouns and verbs from the applicable software field. Record project-specific terms in the glossary. Do not use a technical noun as a verb unless the applicable technical-verb rules permit it.

Avoid contractions, idioms, unexplained abbreviations, figurative instructions, vague praise, and semicolons. Do not shorten a sentence by omitting necessary articles or conditions.

Use these terms consistently:

| Term | Meaning |
|---|---|
| Specification | The task requirements and acceptance criteria |
| Plan | The ordered tasks, checks, risks, and approval records |
| Acceptance criterion | An observable condition required for success |
| Build base | The recorded source state before implementation |
| Working tree | The current local files, including uncommitted changes |
| Checkpoint | An agreed pause for a developer decision |
| Regression test | A test that detects a previously identified defect |
| Fixture | Controlled test input or supporting test data |
| Mock | A test replacement for a real dependency |
| Connector | A host tool that provides access to an external service |
| Evaluation | A check of AI output against specified cases and criteria |
| Idempotent operation | An operation whose repetition has the same effect as one execution |
| Fan-in | Work that waits for several upstream operations |
| Fan-out | Work that dispatches several downstream operations |

Technical names include filenames, tool names, identifiers, units, and interface labels. Keep their exact spelling.

Technical verbs include software actions such as `commit`, `merge`, `deploy`, `parse`, and `render`. Use them only for those actions.

## Check the language

Read the result as the intended reader. Check word choice, sentence limits, actor, action, condition, and result.

Follow Section 8 of the standard for word counts. Keep commands, source excerpts, and quoted labels exactly. Do not rewrite code to satisfy a prose rule.

A sentence-length check detects only part of the problem. Review approved meanings and technical terms separately. Report any remaining terminology or conformance limits.
