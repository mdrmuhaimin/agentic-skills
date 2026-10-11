# Write a clear walkthrough

The teaching references are **Head First Java** and approachable technical books from **Manning Publications**. Use a concrete example, useful diagrams, reader questions, and short takeaways.

Do not copy book passages, characters, illustrations, or distinctive wording. This guide and sample are original adaptations of the source PR.

## Explain through one example

- Address the reader directly with familiar words.
- Define a technical or business term at first use.
- Follow one clearly fictional example from input to output.
- Begin each substantial section with its purpose.
- Add a small diagram or comparison when it clarifies the flow.
- Explain each exact source excerpt immediately after it.
- End substantial sections with a short `Remember` line when useful.
- Answer one or two applicable reader questions in a longer walkthrough.
- Keep uncertainty visible in prose, examples, and diagrams.

Use the writing rules in ASD-STE100 Issue 9. Limit instructions to 20 words per sentence and descriptions to 25 words.

Use active voice, simple verb forms, and one topic per paragraph. Keep paragraphs within six sentences. Avoid contractions, idioms, semicolons, and figurative instructions.

Use dictionary-approved meanings and defined software terms. Add unfamiliar terms to the glossary. Keep exact source text, commands, and interface labels.

The teaching devices are optional structures, not a fixed chapter template. A small code area may need only a few paragraphs.

## Sample

This sample is illustrative. Maya, the document, and the system are fictional. The sample demonstrates presentation, not repository behavior.

### One upload, several jobs

You need to understand how a file becomes searchable. Follow one file through the system to see the separate steps.

Imagine Maya uploads a two-page guide. She sees an upload confirmation. Later, she searches for a phrase from page two.

In this fictional system, four operations connect those actions:

```mermaid
flowchart LR
    A[Receive the file] --> B[Extract its text]
    B --> C[Divide the text into chunks]
    C --> D[Store the chunks for search]
```

The first operation receives the file. The second operation extracts readable text from it. Search uses this text.

The third operation divides the text into smaller parts called **chunks**. A chunk contains part of the guide's text. The fourth operation stores these chunks for search.

Maya sees one guide. The application stores several chunks from that guide. File receipt and search availability are separate events.

> **Questions and answers**
>
> **Q: Does the upload confirmation prove that the guide is searchable?**
>
> A: The confirmation alone does not prove search availability. Check which operation sends the confirmation and which operations have completed.

**Remember:** File receipt, text extraction, and search storage are separate steps. In a real walkthrough, each statement about these steps needs source evidence.

## Keep the explanation accurate

Read the fact sheet before selecting the example. Fictional names and harmless inputs can clarify the flow. Behavior, order, conditions, and causes still need evidence.

Distinguish “the code does,” “we infer,” and “the cause is suspected.” Do not increase certainty to simplify the story.

Include factual diagram labels, question answers, and Remember lines in the claim audit. Follow [citations.md](citations.md) for excerpts and illustrative blocks.

A passing excerpt check does not validate the explanation.
