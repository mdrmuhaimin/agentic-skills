---
name: online-tutor
description: Explain dense reports, research, code, or previous answers for a specific reader. Use for simpler explanations, tutorials, lessons, courses, and onboarding guides.
license: MIT
metadata:
  author: custom
  version: "1.0"
---

# Online tutor

Turn dense source material into an accurate explanation that the intended reader can understand and use.

## Start

1. Read the full source.
2. Identify the reader and their existing knowledge.
3. State the one result that the reader must understand or achieve.
4. Check the source's evidence and uncertainty.
5. Select the task size below.

When the reader is unspecified, assume a capable adult new to this topic. State the assumption. Ask only when missing context materially changes the lesson.

| Size | Scope | Output budget |
|---|---|---|
| LOW | One paragraph, term, or confusing answer | 100–300 words |
| MEDIUM | One document, concept, or system | 500–1,200 words in 2–5 lesson sections |
| HIGH | A course or complex onboarding sequence | 1,500–4,000 words in 4–10 lesson sections |

For MEDIUM or HIGH work, read [teaching.md](references/teaching.md) for the reader model, lesson plan, review, and delivery requirements.

## Explain

Teach one idea per section. Put a concrete example before an abstract restatement. Define unfamiliar terms at first use.

End each lesson section with a question, prediction, or short task. Put the answer immediately after it. LOW work can use an optional brief check.

For MEDIUM and HIGH work, add a recovery sentence after each answer. Tell the reader what to reread if needed.

Use a table for comparisons. Use prose for causal explanations. Use a plain-text diagram only when it clarifies a structure or relationship.

Do not use Mermaid or another renderer-dependent diagram format in this skill. Label every diagram element and explain its purpose.

Use a short story only when it clarifies the mechanism. State its connection to the lesson explicitly. Do not invent evidence or authority.

## Language and review

Use ASD-STE100 writing rules: active voice, simple verbs, consistent defined terms, and no contractions or semicolons.

Limit procedural sentences to 20 words and descriptive sentences to 25 words. Keep each paragraph to one topic and six sentences.

Check dictionary meanings and necessary technical terms separately. Keep exact quotes and identifiers. Use literal worked examples instead of figurative instructions.

Check the result against the source and reader goal. Remove repetition, vague praise, unnecessary background, and template sections that add no value.

For conflicting or questionable source claims, ask for the needed decision before final delivery. Keep uncertainty in sensitive subject matter.

For HIGH or domain-sensitive work, get the required review before treating the draft as final. Respect explicit approval already given for that version.

Return the explanation, source limits, and useful next steps. Do not publish without separate authorization.
