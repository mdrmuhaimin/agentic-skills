---
name: online-tutor
description: >-
  Turns dense, jargon-heavy, or AI-agent-generated output (specs, technical
  reports, research papers, code walkthroughs, audits, analyses) into content
  a human can actually read once and retain, explainers, tutorials,
  multi-lesson courses, or onboarding guides. Use this whenever the user asks
  to explain something simply, make content digestible, break something down,
  simplify for a general audience, turn something into a lesson or course, or
  hands over a technical document and wants a human-readable version, even if
  they never use the word tutor. Also use it when Claude's own earlier
  response in the conversation was dense or jargon-heavy and the user asks
  for a clearer version of it.
license: MIT
metadata:
  author: custom
  version: "1.0"
---

Turns dense, information-heavy source material (agent output, specs, research papers, technical reports, code, raw notes) into content a human can read once and actually retain: explainers, tutorials, multi-lesson courses, onboarding guides, or simplified rewrites.

**Input**: Any dense or jargon-heavy source (an AI agent's report, a technical spec, a research paper, a codebase explanation, raw notes, a previous Claude response) plus a target reader.

**Goal**: Produce content a specific reader can read once, follow without re-reading, and actually retain, not just content that is technically accurate. Accuracy is necessary but not sufficient. The output must define the reader, cut to one primary takeaway, chunk the material to fit working memory, anchor every abstract claim in something concrete, use diagrams only where text genuinely can't do the job, and end each chunk with a way for the reader to check they got it.

**Core principle**: Information density and human readability sit on different axes. Output can be exhaustively correct and still be useless to a human, because working memory holds only a handful of new items at once, attention decays without a hook, and trust in a claim depends on more than its truth value. This skill translates correct-but-dense output into something a specific person can actually learn from, without losing the accuracy that made it worth reading.

---

## PRIORITY STACK: Always Active

These rules govern every task at every tier. They override section instructions when in conflict. Read them once. Apply them throughout.

1. **Reader before content.** Never simplify a sentence before the reader, their starting knowledge, and the one thing they need to walk away with are defined. A rewrite without a defined reader is just a shorter version of the same document, not a more readable one.
2. **Respect the working-memory ceiling.** A reader can hold roughly four new, unrelated things in mind at once when actively working with them, not seven. Every lesson chunk introduces only a small handful of new named concepts. If a chunk needs more, split it.
3. **No vague praise words.** "Powerful," "seamless," "robust," "elegant," "game-changing," and "cutting-edge" describe nothing. Replace every one with the concrete fact it's standing in for.
4. **Concrete before abstract, always.** Never state a principle, rule, or definition without a worked example, a number, or a comparison the reader already understands directly beneath it. An unillustrated abstraction is the single most common reason dense writing stays dense.
5. **One idea per chunk, checked before moving on.** Each lesson chunk teaches exactly one thing and ends with a way for the reader to confirm they got it. Correct information with no checkpoints is a reference document, not a lesson.
6. **Diagrams earn their place; ASCII, never Mermaid, when one is needed.** Use a diagram only when a relationship is spatial, sequential, or hierarchical enough that prose would need extra sentences to say what a diagram says in one glance. When a diagram is warranted, use plain ASCII or box-drawing text. Mermaid and similar renderer-dependent syntaxes are never used, because their diagram is invisible in exactly the moments it matters. See Section G.
7. **Story is a delivery vehicle, not a decoration.** A story earns its place only when it does something prose can't: lower resistance to a counterintuitive claim, or make an abstract mechanism feel like something that happens to someone. A story that doesn't resolve into the lesson's point is filler and gets cut.
8. **Every dense term gets defined once, in plain words, on first use.** Jargon isn't banned; technical fields need technical words. But no term appears unglossed before its first plain-language definition.
9. **Don't invent authority the source material doesn't have.** If the source is uncertain, contested, or wrong, say so plainly rather than smoothing it into confident prose. A simplified lie is worse than a complicated truth.
10. **Compress to the tier budget.** Longer is not clearer. Cut anything that doesn't teach, transition, or check understanding. Mechanical section-filling is a failure mode, not thoroughness.

---

## PHASE 1: UNDERSTAND

### Step 0: Complexity Triage `[ALL]`

Classify before writing anything.

| Tier | Characteristics | Required Sections | Word Budget |
|------|------------------|--------------------|-------------|
| **LOW** | One dense paragraph, one confusing answer, one term to unpack | Learning Objective (inline), Voice pass, Jargon Contract (if needed), Stop Conditions | 100–300 words |
| **MEDIUM** | One document, report, or explainer-length rewrite; a single concept or system | Sections A–M | 500–1,200 words, 2–5 chunks |
| **HIGH** | A multi-concept curriculum, onboarding sequence, or full course from a long or complex source | All sections, plus a lesson sequence map | 1,500–4,000 words across 4–10 lesson chunks |

Compression rules, enforced:
- Merge sections that cover the same ground on a LOW task. Name the merge.
- Lesson Chunk Model: max 10 rows unless the source genuinely needs more. If it does, this is a HIGH task and belongs in a lesson sequence, not one long chunk table.
- Diagram count: max one diagram per lesson chunk. A chunk that needs two diagrams is really two chunks.
- If a section would be filler for this task, mark `[skipped: not applicable]` and move on.

### Step 1: Reader Clarification Check `[ALL]`

Resolve internally before asking the human.

1. Who is reading this, and what do they already know about the topic?
2. Why are they reading it? Curiosity, a task to complete, a decision to make, onboarding to something new?
3. What is the one thing they need to walk away able to do or explain?
4. What is the cost of them misunderstanding it? Low: they reread a paragraph. High: they make a bad decision, misconfigure something, or repeat the misunderstanding to someone else.
5. Will they read this once, or come back to it as reference? A tutorial and a reference document are shaped differently. This skill defaults to tutorial shape unless told otherwise.
6. Is the source material itself trustworthy, or does it need a caveat before it gets simplified?

Ask the human only when the answer materially changes the shape of the output, not for stylistic preference. A missing reader profile with an obvious default, a capable adult new to this specific topic, isn't worth a clarifying question. State the assumption and proceed.

### Step 2: Source Material Audit `[ALL]`

Read the entire source before writing a line of the rewrite. Identify:
- The core claim or conclusion: what is this document actually saying?
- The evidence or reasoning behind it: why should the reader believe it?
- The procedural content: what steps, if any, does the reader need to follow?
- The jargon and technical terms used without definition
- The genuinely optional detail: edge cases, caveats, and asides a first-time reader doesn't need in order to grasp the core idea

**Live source beats stale framing.** If the source material's own summary or headline disagrees with what the body actually supports, trust the body. Note the drift rather than propagating a misleading framing.

### Step 3: Reader and Context Model `[MEDIUM, HIGH]`

| Dimension | Answer |
|-----------|--------|
| Reader's starting knowledge | |
| Reader's motivation for reading | |
| Reading environment (focused sit-down vs. skimming on a phone) | |
| Time budget | |
| Mistake cost if they misunderstand | |
| Jargon tolerance (domain expert wanting a summary vs. total newcomer) | |
| One thing they must walk away knowing | |
| What they can safely forget by next week | |

**Domain-sensitive source material** (medical, financial, legal, religious, or safety-critical) must keep three things visibly separate in the output:
- What the source material actually claims
- Where it is confident versus uncertain
- That this is an explanation, not a professional recommendation, when the topic warrants that distinction

Do not let simplified language imply an authority the source material doesn't have. A plain-language summary of a legal document is still not legal advice, and it should not read like one.

### Step 4: Content Priority Audit `[ALL]`

Classify every piece of source content before deciding what survives into the rewrite.

| Content | Role | Priority | Treatment |
|---------|------|----------|-----------|
| Core claim / conclusion | Orientation | P0 | Stated plainly in the first sentence or two |
| Reason the claim is true | Understanding | P0 | Made concrete with one example before moving on |
| Steps the reader must follow | Task completion | P0 | Numbered, one action per step |
| Supporting detail | Confidence | P1 | Included if it fits the chunk budget, cut if not |
| Jargon / technical term | Vocabulary | P1 | Defined once in plain words on first use |
| Edge case, exception, caveat | Completeness | P2 | Brief mention or deferred to an "if this doesn't apply to you" aside |
| Background the expert included out of habit | Rarely needed | P3 | Cut, unless the reader explicitly wants depth |

Rules:
- If everything in the source reads as P0, the source hasn't been triaged yet. Go back and find what's actually load-bearing.
- P3 content never occupies the reader's first three sentences. Orientation comes first; caveats come after the reader has the shape of the idea.

### Step 5: Diagram Necessity and Tool Decision `[when a visual is being considered]`

Most explanations don't need a diagram. Text that flows in one direction, has one cause and one effect, or is naturally a list, should stay text. Reach for a visual only when the answer to one of these is yes:

- Does the content describe a structure (parts and how they connect) that a reader would otherwise have to reconstruct in their head from three or four separate sentences?
- Does it describe a sequence or flow with branches, loops, or parallel paths, not just "first this, then that"?
- Does it describe a hierarchy or nesting relationship?

If yes, pick the tool by what's being shown, not by preference:

| What you're showing | Right tool |
|---|---|
| A structure, flow, or hierarchy with 3–7 nodes | ASCII / box-drawing diagram |
| Parallel comparison across a few named items | Table |
| A single relationship or mental model | A one-line analogy in prose, no diagram needed |
| More than roughly 7 nodes or 2 branch levels | Split into two smaller diagrams, or reconsider whether this is one lesson chunk or two |

**Never Mermaid, or any other renderer-dependent diagram syntax.** See Section G for the full reasoning. Short version: a diagram that fails to render falls back silently to raw code, which is worse than no diagram, and the failure is often invisible to whoever wrote it. Plain text diagrams render everywhere prose does: chat windows, terminals, PDFs, printed pages, and code comments, with no dependency on a rendering engine being present and correctly configured.

### Step 6: Storytelling Decision `[when narrative is being considered]`

Use a story or narrative frame only when one of these is true:
- The idea is counterintuitive, and a reader is likely to resist it stated flatly but accept it once they see it happen to someone.
- The concept is a mechanism, a process that unfolds over time, and walking through one concrete instance is clearer than describing it in general terms first.
- The content is meant to be remembered and retold, not just understood in the moment.

Skip narrative when:
- The reader is scanning for a specific fact or step and a story would delay them getting to it.
- The content is reference material they'll search, not read start to finish.
- Adding a story would pad the word count without changing what the reader understands.

When a story is used, it must resolve explicitly into the lesson's point, in the same paragraph or the one immediately after. A story that trails off and leaves the reader to infer the moral hasn't done its job. See Section H.

---

## PHASE 2: DESIGN

### Section A: Learning Objective `[MEDIUM, HIGH]`

- Reader's current understanding:
- Reader's desired understanding after reading:
- The one primary takeaway (not three, not five, one):
- What must not happen (reader ends up less confident than before, or confidently wrong):
- Why the raw source material would fail this reader as-is:

### Section B: Delivery Principles `[ALL]`

Define 3–7 principles. Each must be a concrete instruction, not a mood.

Good examples:
- State the plain-language definition of a term before its first technical use, not after.
- Never introduce a second unfamiliar concept before the first one has an example attached to it.
- Write the sentence a smart friend would actually say out loud, then check it's still accurate.
- Cut any sentence that restates something already said in different words.
- One chunk, one idea, one checkpoint. A chunk that needs two checkpoints is two chunks.

Reject: "Make it engaging." "Make it accessible." "Make it easy to understand." These describe an outcome, not an instruction.

### Section C: Content and Lesson Map `[ALL]`

Preferred order for a chunk, or for a whole short piece:
1. Orientation: what this is about and why it matters to the reader right now
2. The one core idea, stated plainly
3. A concrete example or analogy that anchors it
4. The reasoning or mechanism behind it, if the reader needs it
5. A checkpoint: question, prediction, or small task
6. What this connects to, or what's next

| Section | Purpose | Format | New Concepts | Checkpoint |
|---------|---------|--------|----------------|------------|
| | | | | |

Keep each row to 1–2 lines. Omit a stage that doesn't apply rather than padding it in.

### Section D: Lesson Chunk Model `[MEDIUM, HIGH]`

Break the source material into chunks, each teaching exactly one idea.

| Chunk | Single Idea | Anchor / Analogy | Worked Example | Checkpoint | If the Reader Is Lost |
|-------|--------------|--------------------|-------------------|------------|--------------------------|
| | | | | | |

Rules, enforced:
- No chunk introduces more new named concepts than a reader can hold in mind at once. If a row needs a second distinct anchor, split the chunk.
- Every chunk has a worked example before an abstract restatement. Lead with the concrete instance; don't tack an example on as an afterthought.
- Every chunk ends with a checkpoint the reader can answer without flipping back: a question, a prediction prompt ("what do you think happens if..."), or a two-minute task.
- "If the Reader Is Lost" is not optional. Every chunk needs one sentence telling the reader what to reread or ask themselves if the checkpoint didn't land.

### Section E: Design Decision Log `[MEDIUM, HIGH]`

One row per meaningful choice: a chunk boundary, a diagram-versus-table call, a story that got cut, a term left undefined because the audience already knows it.

| Decision | Options Considered | Chosen | Reason |
|----------|-----------------------|--------|--------|
| | | | |

Do not log trivial choices. Log anything a reviewer, or a future editor of this content, might question.

### Section F: Tone and Voice Calibration `[MEDIUM, HIGH]`

Grounded in what makes explanatory nonfiction actually get read: an idea that is Simple, Unexpected, Concrete, Credible, Emotional, and told as a Story is dramatically more memorable than the same idea stated as a flat claim. Run the content through this table as a diagnostic for where it's currently flat, not as a checklist every box must fill.

| Trait | What it means here | Where it shows up in this content |
|-------|-----------------------|---------------------------------------|
| Simple | One core idea, stripped to its essential point | |
| Unexpected | Does it break an assumption the reader is likely holding? | |
| Concrete | Sensory, specific language instead of abstraction | |
| Credible | A reason to believe it: a source, a number, a named example | |
| Emotional | Does the reader have a reason to care, beyond correctness? | |
| Story | Is there a moment, a person, or a sequence the reader can picture? | |

**Curse-of-knowledge check.** Before finalizing, reread the draft as the reader defined in Section A, not as the writer. Every sentence that feels effortless to write is a candidate for a sentence the reader can't follow: deep familiarity makes an explanation feel simpler than it actually is to someone receiving it for the first time. Flag any sentence that only makes sense if the reader already half-knows the answer.

### Section G: Diagram and Visual Contract `[when a diagram is used]`

**Why ASCII over Mermaid, specifically.** Mermaid and comparable diagram-as-code syntaxes render only when the destination explicitly supports them and the syntax parses cleanly. When either condition fails, most renderers fall back to a raw, unreadable code block instead of a visible error, so the failure is often invisible to the person who wrote it. Renderer support is inconsistent across chat interfaces, terminals, PDFs, and document exports, so the same block that renders in one place shows raw text in another. Plain ASCII or box-drawing text has no rendering dependency: it displays correctly anywhere monospaced text displays, it diffs cleanly if it ever lives in version control, and it works in every medium this skill's output might end up in, chat, email, a printed handout, a terminal. It's a well-documented pattern in software documentation specifically because it stays in sync with the surrounding text and never rots the way an external image or an unrendered diagram block can.

**When to still skip the diagram entirely.** A diagram is not automatically better than prose. If the structure has only two or three parts and one direction of flow, a single well-written sentence beats a boxed diagram that takes longer to read than to say. Reserve diagrams for genuine structure: parts, connections, direction, or hierarchy that prose would need extra sentences to reconstruct.

ASCII diagram rules:
- Keep width to roughly 70–80 characters so it stays readable in a chat window, a terminal, and a printed page without wrapping.
- Use `+`, `-`, `|` for maximum compatibility, or Unicode box-drawing characters (`┌─┐│└─┘`) when the destination is known to render Unicode cleanly.
- Label every box and every arrow. An unlabeled diagram is decoration, not information.
- Max 7 nodes per diagram. If the real structure has more, split it into two diagrams that each show one layer, or reconsider whether this is genuinely one chunk.
- Always wrap it in a code block (triple backticks) so monospace alignment survives.

```text
┌──────────────┐      ┌───────────────┐      ┌──────────────┐
│ Reader's      │ ---> │ One concrete  │ ---> │ Reader can   │
│ starting      │      │ example or    │      │ check they   │
│ question      │      │ analogy       │      │ got it       │
└──────────────┘      └───────────────┘      └──────────────┘
```

Every block needs a label and a reason it's there. An unlabeled decorative diagram is a failure mode, whether it's for a screen or a lesson.

### Section H: Storytelling Contract `[when narrative is used]`

| Story Element | Trigger | Purpose | Length Budget | Must Not |
|------------------|---------|---------|------------------|----------|
| Opening scenario | Counterintuitive claim | Lower resistance before stating the claim directly | 2–4 sentences | Delay the core idea past the first paragraph |
| Worked-example story | Abstract mechanism | Show the mechanism happening to someone, not just described | Fits inside the chunk budget | Introduce a second, unrelated idea mid-story |
| Closing callback | Reinforcing the takeaway | Tie the chunk's idea back to the opening scenario | 1 sentence | Introduce new information the reader hasn't seen yet |

Rules:
- A story must resolve into the stated point in the same paragraph or the next one. Immersion in a story measurably improves recall of the content it carries, but only if the story actually delivers the point rather than leaving the reader to guess the moral.
- One story per chunk, maximum. A chunk that needs two stories to make its point is two chunks.
- A story is never used to avoid stating the claim plainly. State the claim, then use the story to make it stick, not the other way around.

### Section I: Structural Format Rules `[ALL]`

- Use a table when data is parallel or comparable across items: options, trade-offs, terms and definitions.
- Use numbered steps when order matters and the reader will act on them in sequence.
- Use prose, not bullets, for causal reasoning. "X happens because Y, which means Z" loses its logic when broken into three disconnected bullet fragments.
- Use a bare bulleted list only for genuinely parallel, unordered items with no internal reasoning connecting them.
- Headers mark a change of idea, not a change of sentence length. Don't add a header just to break up a page visually if the content underneath is one continuous thought.

### Section J: Jargon and Definition Contract `[ALL]`

| Term | Plain-language definition (one sentence) | First used in | Reused as |
|------|-----------------------------------------------|-------------------|------------|
| | | | |

Rules:
- Define a term once, in plain words, the first time it's used, then use that exact term consistently. Switching between a technical term and an informal synonym for the same thing forces the reader to do the mapping work themselves; splitting one concept across two labels adds to their working-memory load for no benefit.
- A term the reader's stated expertise already covers doesn't need a definition. Adding one anyway is condescending and wastes their attention, the mirror image of the curse of knowledge: over-explaining to someone who already knows the basics. Check the reader model in Section A before deciding.

### Section K: Retrieval and Checkpoint Design `[ALL]`

- Every chunk MUST end with a checkpoint the reader can answer without rereading: a question, a prediction, or a two-minute task.
- A checkpoint MUST test the one idea that chunk taught, not a random detail from it.
- The answer or explanation MUST appear immediately after the checkpoint, not deferred to an appendix. Actively retrieving an answer, even briefly and imperfectly, strengthens memory of it more than simply rereading the same material does.
- Checkpoints MUST NOT be decorative quiz filler disconnected from the chunk's actual point.
- A checkpoint is not the same as a throwaway "did that make sense?" line. It asks the reader to do something with the idea: apply it, predict with it, or restate it in their own words.

### Section L: Compression and Cut Rules `[ALL]`

- Cut any sentence that restates something already said. Restating doesn't add clarity, it adds length.
- Cut background detail the reader's stated expertise already covers (see Section A). Over-explaining to someone who already knows the basics is its own form of overload, not a kindness.
- Reduce a caveat or edge case to a brief aside unless the reader's specific situation makes it central.
- If a chunk exceeds its tier's word budget (Step 0), the fix is almost always to cut, not to write faster. A second pass that removes one paragraph is usually the highest-leverage edit available.

### Section M: Stop Conditions `[ALL]`

Stop before producing final output and surface to the human when:
- The reader's starting knowledge is genuinely unknown and changes the whole shape of the piece. A lesson for a total beginner looks nothing like a summary for a domain expert.
- The source material is internally contradictory, and simplifying it would require silently picking a side.
- The topic is medical, legal, financial, or safety-sensitive in a way where a plain-language rewrite could be mistaken for professional advice.
- The source is long or dense enough that it genuinely needs a multi-lesson sequence rather than one piece, and the human hasn't said which they want.
- A claim in the source material appears wrong, not just complex. Flag it rather than smoothing it into confident, readable prose.

Do not silently approximate past these. Resolve, ask, or flag.

---

## PHASE 3: VERIFY

### Section N: Hard Self-Review Gate `[ALL]`

Run before producing final output. If a required item fails, revise before output.

**Reader clarity**
- [ ] A reader with the stated starting knowledge can follow this without outside help.
- [ ] The one primary takeaway is stated in the first paragraph, not buried on page two.
- [ ] No sentence only makes sense if the reader already half-knows the answer.

**Chunking**
- [ ] Every chunk teaches exactly one idea.
- [ ] No chunk introduces more new named concepts than a reader can hold in mind at once.
- [ ] Every abstract claim has a concrete example directly beneath it.

**Diagrams and structure**
- [ ] Every diagram used is ASCII or plain text, never Mermaid or another renderer-dependent syntax.
- [ ] Every diagram earns its place: it shows something prose genuinely couldn't say as fast.
- [ ] Tables are used for parallel data, prose for causal reasoning, not the reverse.

**Story**
- [ ] Any story used resolves explicitly into the lesson's point.
- [ ] No story delays the core idea past the first paragraph.

**Retrieval**
- [ ] Every chunk has a checkpoint that tests its one idea.
- [ ] Every checkpoint's answer appears immediately after it.

**Honesty**
- [ ] No claim in the rewrite is more confident than the source material supports.
- [ ] Any contradiction or weak claim in the source is flagged, not smoothed over.

**Self-calibration.** Score each dimension 1–5 before finalizing.

| Dimension | Score (1–5) | Revise if below 4 |
|-----------|--------------|------------------------|
| Reader clarity | | Yes |
| Chunk-size discipline | | Yes |
| Concreteness (examples present) | | Yes |
| Jargon handled | | Yes |
| Diagram necessity and format | | If a diagram was used |
| Story purposefulness | | If a story was used |
| Checkpoint quality | | For MEDIUM and HIGH |
| Honesty to the source | | Yes |

### Section O: Comprehension Test Plan `[HIGH; recommended for MEDIUM]`

| Test Prompt | Success Signal | Failure Signal | Fix |
|----------------|-------------------|--------------------|-----|
| "What's the one thing this is telling you?" | States the primary takeaway in their own words | Recites a detail instead of the point | Move the takeaway earlier, cut competing claims |
| "Explain paragraph two back to me." | Restates the idea, not the exact sentence | Can only repeat the original phrasing | The paragraph is jargon-dependent, not actually understood; add a plainer anchor |
| "What would happen if X changed?" | Applies the idea to a new instance | Can't extend it past the given example | The chunk taught the example, not the idea; generalize the explanation |
| "Where did you get lost?" | Points to a specific sentence or term | "I don't know, somewhere" | The chunk is too dense; find the missing checkpoint or split it |

### Section P: Delivery Handoff `[ALL]`

- Final format: single explainer, tutorial, lesson sequence, or rewrite of existing text.
- Chunk count and approximate read time.
- Diagrams used and why each earned its place.
- Terms defined.
- Checkpoints included.
- Stop conditions encountered and how they were resolved.
- Destination platform (chat, doc, slide, README, print). Confirm ASCII diagrams and table formatting will survive it.

### Section Q: Human Review Gate

Pause for explicit confirmation before treating output as final when:
- The task is HIGH: a full lesson sequence or course.
- The content is domain-sensitive: medical, legal, financial, religious, or safety-critical.
- A Stop Condition (Section M) was hit and resolved. Confirm the resolution matches what the reader actually needs.
- A source claim was flagged as questionable. Confirm how to handle it before publishing.

Valid confirmation: "looks good," "publish it," "ship it," or a clear equivalent. Silence isn't approval.

---

## LEARNING SCIENCE GROUNDING

This skill isn't built on intuition about "what makes writing good." Each rule above traces to a specific, established finding. This table is the shared evidence base so the rules don't need to be re-derived or re-justified on every run.

| Finding | Source | What it drives in this skill |
|---------|--------|---------------------------------|
| Working memory holds roughly four novel items at once when rehearsal is prevented, not the older "seven plus or minus two" figure | Miller (1956); Cowan (2001) | Chunk-size limits (Priority Stack #2, Section D) |
| Novices learn more, and more efficiently, from studying worked examples than from solving problems cold; this reverses as expertise grows | Sweller & Cooper (1985), the worked example effect and expertise reversal effect | Concrete-before-abstract rule (Priority Stack #4); reader-tier calibration in jargon handling (Section J) |
| Static text and images are retained better than transient spoken or animated information, because a reader can re-inspect them at their own pace | Sweller, the transient information effect | Preference for static plain-text diagrams over anything that has to be watched or replayed |
| Readers immersed in a story ("narrative transportation") remember its content better and engage with it less critically than the same content stated as a flat claim | Green & Brock (2000), narrative transportation theory | Storytelling Decision (Step 6) and Storytelling Contract (Section H) |
| Ideas that are simple, unexpected, concrete, credible, emotional, and carried by a story are dramatically more memorable than flat statements of the same idea | Heath & Heath, "Made to Stick," the SUCCESs framework | Tone and Voice Calibration (Section F) |
| Experts systematically overestimate how much of their explanation a novice can follow, because deep familiarity makes an idea feel simpler than it is | Elizabeth Newton's tapper-listener study, the curse of knowledge | The curse-of-knowledge check in Section F; the reader-model steps in Phase 1 |
| Actively retrieving an answer, even briefly and imperfectly, strengthens memory of it more than rereading or restudying the same material | Roediger & Karpicke (2006), the testing effect / retrieval practice | Checkpoint requirement in every chunk (Section K) |
| Minimal, task-focused instruction that gets the reader doing something real quickly, in brief, self-contained chunks, outperforms long front-loaded explanation for practical skill-building | John Carroll, "The Nurnberg Funnel," minimalist instruction | Chunk brevity, self-contained lesson design (Section D), front-loading the reader's actual task over background theory |
| Diagram-as-code syntaxes like Mermaid render only when the destination explicitly supports the exact syntax used, and fail silently back to unreadable raw text otherwise; plain ASCII text has no such dependency | Documented rendering-reliability issues across chat interfaces, IDEs, and doc viewers; research on how programmers actually use ASCII diagrams in practice | The ASCII-over-Mermaid rule (Priority Stack #6, Section G) |
| Comprehension in written text tracks primarily with sentence length and word length, though this is a screening signal, not a full clarity measure; necessary complexity shouldn't be flattened past the point of accuracy | Flesch (1948) readability research; the U.S. Plain Writing Act's definition of plain language | Delivery Principles (Section B); the instruction to respect necessary complexity rather than oversimplify |

If a specific piece of content needs research beyond this table, a domain fact, a statistic, a current event, say so plainly rather than presenting an invented figure as established: `Research unavailable in this pass; the claim above should be verified before publishing.`

---

## FAILURE MODE REFERENCE

Check the output against these before calling it done.

| Failure Mode | Signal | Fix |
|---------------|--------|-----|
| Accurate but unreadable | Every fact in the source survived, but a first-time reader would bounce off it | Return to Section A: who is this actually for, and what's the one thing they need? |
| Vague praise language | Words like "powerful," "seamless," "robust" appear with nothing concrete behind them | Replace with the specific fact the word was standing in for |
| Wall of abstraction | A rule or definition with no worked example under it | Add a concrete instance before moving to the next idea |
| Mega-chunk | One "lesson" quietly contains three or four distinct ideas | Split by idea, not by paragraph length |
| Decorative diagram | A diagram that repeats what the adjacent sentence already said, with no new structure shown | Cut it, or rebuild it around the structure it should show |
| Mermaid or renderer-dependent diagram used anyway | Diagram syntax that assumes a specific rendering engine is present | Rebuild as plain ASCII / box-drawing text |
| Story with no landing | A narrative opens the piece and never explicitly ties back to the point | Add the explicit callback, or cut the story |
| Jargon relay race | The same concept is called three different names across the piece | Pick one term, define it once, use it consistently |
| Checkpoint-free chunk | A chunk ends and moves straight to the next one with no way to check understanding | Add a question, prediction, or task before moving on |
| Confident oversimplification | The rewrite states something more strongly than the source material actually supports | Walk the confidence level back to match the source, or flag the source's own uncertainty |
| Mechanical section-filling | Every section in this skill's templates filled with boilerplate regardless of whether the content needs it | Compress: merge, skip, and cut per Step 0 |
| Self-review skipped | Section N's checklist not actually run before finalizing | Run it. It's short specifically so there's no excuse to skip it |

---

## OUTPUT TEMPLATES

### LOW Task

```markdown
## What this is about
## The one idea
## Concrete example
## (Optional) Quick check
## Where this came from / caveats
```

### MEDIUM Task

```markdown
## Learning Objective
## Content and Lesson Map
## Chunk 1: [idea] -> example -> checkpoint
## Chunk 2: [idea] -> example -> checkpoint
## (continue for each chunk)
## Diagram(s), if used
## Jargon Contract
## Stop Conditions (if any were hit)
## Delivery Handoff
```

### HIGH Task

```markdown
## Learning Objective and Reader Model
## Lesson Sequence Overview (map of all chunks/lessons)
## Lesson 1: [title]
###   The one idea
###   Concrete example / story (if used)
###   Diagram (if used)
###   Checkpoint
## Lesson 2: [title]
## (continue for each lesson)
## Jargon Contract (full glossary)
## Design Decision Log
## Stop Conditions (if any were hit)
## Comprehension Test Plan
## Delivery Handoff
```

---

## DOMAIN EXAMPLES

Structural references only. Never copy verbatim into an unrelated task.

**A: Turning a dense agent report into a one-page explainer.** A technical audit, spec, or analysis comes back exhaustive and correct but unreadable to the person who has to act on it. Response: extract the one decision or takeaway the reader actually needs, cut everything the audit included out of thoroughness rather than necessity, replace any Mermaid diagram with a plain ASCII version or a table, end with one checkpoint that confirms the reader knows what to do next.

**B: Turning a research paper into a course lesson.** Source has real depth but is written for peers, not learners. Response: find the one mechanism the paper is actually demonstrating, build one worked example around it, use a brief narrative frame if the finding is counterintuitive, define every term the paper assumed the reader already had.

**C: Simplifying Claude's own prior dense response.** A previous answer in the conversation was accurate but the person says they're lost. Response: rerun Phase 1 on that response as the "source material," identify what made it dense (usually: no reader model, no worked examples, too many ideas per paragraph), rebuild as a MEDIUM-tier explainer rather than just shortening the same sentences.

**D: Building a multi-lesson onboarding sequence from a long internal document.** Source is a full system or process document meant for reference, not learning. Response: this is a HIGH task; don't try to compress it into one piece. Build a lesson sequence map first, one lesson per major concept, each self-contained enough to make sense out of order, with its own checkpoint.

---

## DELIVERY CONTEXT ADDENDUM

A generic skill can't be perfectly calibrated to any one voice or platform. Fill this in once and reuse it; update it when preferences change.

```
Voice and style constraints:    [e.g., no em dashes, plain direct English, no corporate buzzwords]
Preferred structural default:   [e.g., tables over dense prose wherever the content is parallel]
Typical reader profile:         [e.g., senior technical audience skimming on mobile / total beginners / mixed]
Destination platform(s):        [e.g., chat, Word doc, README, printed handout: confirm ASCII diagrams and tables survive each]
Existing glossary or style guide, if any: [pointer, or note if none exists]
Checkpoint mechanism available: [e.g., plain question in text / interactive quiz tool / text-only]
Typical source material:        [e.g., AI agent reports, technical specs, research papers, internal docs]
```

Example filled-in defaults for this user's own work: no em dashes anywhere, plain direct English with no corporate buzzwords, tables preferred over dense prose wherever the content is parallel or comparable, surgical edits preferred over wholesale rewrites when revising existing content rather than drafting fresh.

