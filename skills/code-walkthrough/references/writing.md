# Writing a walkthrough people can follow

The source PR's storyteller pairs writing guidance with a short sample. Preserve that pairing: rules describe the approach; the sample shows how it sounds.

The developer's intended teaching references are **Head First Java** and approachable technical books from **Manning Publications**. Take inspiration from their teaching approach, without copying book passages, characters, illustrations, or distinctive wording. This reference and its sample are original adaptations of the PR's storyteller guidance, not extracts from those books.

## Teach through a journey

- Talk to the reader as a kind senior colleague would at a whiteboard. Use “you,” familiar words, and sentences that carry one main idea. Explain a technical or business term when it first appears; add useful terms to the glossary.
- Follow one explicitly fictional example from input to output. Make each section a stop on its journey, so the reader has a reason to learn the next concept.
- Begin a substantial section with why it matters. Show a small diagram, a concrete situation, or a before/after view when it helps; then explain it. Choose diagram size for clarity rather than a fixed box count.
- Copy source excerpts exactly from the fact sheet. Explain what each excerpt does and why it matters in plain language immediately afterwards. A reader should be able to follow the explanation without decoding the syntax.
- End substantial sections with a short `**Remember:**` line expressing the useful takeaway. Do not add one to every small paragraph.
- Once or twice in a longer walkthrough, answer the questions a reader may hesitate to ask in a “There are no dumb questions” box. Keep answers substantive and kind. Do not impose quizzes or exercises.
- Light humour is optional. Never make the reader the joke. Warmth should not bury the explanation or soften a real limitation.
- Follow the project's language conventions. Keep the reading-time estimate honest; cut secondary detail before breaking the example's journey.

These are teaching devices, not a rigid chapter template. A small code area may need only a few paragraphs. Never invent system behavior, business motives, or guarantees to make the story smoother.

## Sample voice

The following is an **illustrative writing sample**. Maya, the document, and the system behavior are fictional. It demonstrates presentation, not facts about the repository being explained. A real walkthrough must replace these behaviors with cited, audited fact-sheet claims.

### One upload, several small jobs

You want to see how a file becomes something the application can search. Following one file makes the handoffs easier to see.

Imagine Maya uploading a two-page guide. Maya is made up, and so is the guide. She clicks Upload, sees a confirmation, and then searches for a phrase she remembers from page two.

Between those two actions, the file has a few jobs to get through:

```mermaid
flowchart LR
    A[Receive the file] --> B[Extract its text]
    B --> C[Split the text into pieces]
    C --> D[Store the pieces for search]
```

Start with extraction. That means getting readable text out of the file. Think of the file as the envelope and the text as the letter inside. Receiving the envelope is useful, but search needs the letter.

Next comes splitting. In this fictional system, the extracted text is divided into smaller pieces called **chunks**. A chunk is simply a portion of that text. It is a separate step because reading the file and deciding how to divide its contents are different jobs.

Maya still sees one guide. Inside the application, several smaller pieces now represent it. That distinction helps you follow the code: a file arriving and its searchable pieces being stored are separate moments in the journey.

> **There are no dumb questions**
>
> **Q: Does an upload confirmation mean the guide is already searchable?**
>
> A: You cannot tell from the confirmation alone. Find where the application sends that response, then check which later steps have finished. In a real walkthrough, the answer needs evidence from the code.

**Remember:** Follow the handoffs. Receiving a file, reading its text, and storing searchable pieces each answer a different question.

## Apply the style without adding facts

Read the fact sheet first, then choose an example that can travel through its verified flow. Fictional names and harmless example inputs may make the explanation concrete; their framing must stay explicit. Behavior, ordering, conditions, and causes still need evidence.

Carry uncertainty into the story: “the code does,” “we infer,” and “the cause is suspected” mean different things. Diagram labels, analogies, Q&A answers, and Remember lines receive the same claim audit as ordinary prose. An analogy helps explain a fact; it does not prove it.

For source excerpts and illustrative code blocks, follow [citations.md](citations.md). Passing the excerpt checker does not validate the narrative.
