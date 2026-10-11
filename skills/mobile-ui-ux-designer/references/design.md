# Define the design contract

## Control the document size

Keep research within five rows and design principles within seven items. Keep information hierarchy within eight rows.

Keep screen states within ten rows unless the flow requires more. Keep interaction contracts within eight unless implementation requires more.

Use at most seven major vertical wireframe blocks unless the screen needs more. Explain any exception. Merge duplicate sections and omit inapplicable sections.

LOW work needs affected states, one or two interactions, accessibility, blocking questions, and checks. MEDIUM work needs the applicable contracts below.

HIGH work also needs the complete user flow, platform decisions, usability plan, and approval record.

## Problem and principles

State the current problem, desired outcome, primary and secondary actions, prohibited outcomes, and expected design risks.

Choose three to seven concrete principles for MEDIUM and HIGH work. Examples include visible next actions, separate warnings, and kept input during recovery.

Record significant decisions with options, choice, and reason. Do not record trivial formatting choices.

## Information hierarchy

Use this order when applicable:

1. Identify the screen.
2. Show the current status.
3. State the next instruction.
4. Present the primary action.
5. Provide necessary support.
6. Provide recovery or help.
7. Offer optional education.

Record each region's purpose, component, visibility, interaction, and design decision. Keep each row within one or two lines.

## States

List every applicable state. Consider initial, empty, loading, ready, in-progress, complete, error, offline, denied, locked, disabled, partial, pending-sync, and restored states.

For each state, specify visible content, actions, disabled controls, recovery, and the applicable decision.

Explain disabled controls. Offer recovery from errors. Explain locked states without blame. Do not show false progress. Give empty states a useful next action.

## Interaction contract

For each affected interaction, specify:

- Trigger and preconditions.
- System response and visible feedback.
- Loading, success, and failure behavior.
- Analytics event when applicable.
- Accessibility announcement.
- Prohibited behavior.

For a locked feature, explain the requirement and offer a contact or recovery action. Do not imply that fictional preview data is real.

For a filter, keep other selections and show the result count. Retain previous results when a refresh fails.

For a measurement form, validate fields and keep input on failure. Confirm a save with text. Do not imply a clinical diagnosis.

## Layout and wireframes

Specify behavior for each applicable responsive class. Include visible content, action placement, safe areas, keyboards, scroll, sheets, and large text.

Keep the primary action available without scroll where practical. Let localized text wrap without hiding actions. Reduce choices on high-stress screens.

Use plain-text wireframes for early concepts. Add component and token tables for engineering handoffs. Provide implementation code only when requested.

Use a four-column planning grid for compact screens. Label component regions and content priority. Mark `[sticky]`, `[scroll]`, `[sheet]`, `[accordion]`, and `[tooltip]` regions.

Show hierarchy rather than exact pixels. Use separate compact wireframes when behavior differs. Explain each region's purpose.

## Visual treatment

Specify actual color roles, text styles, icon treatment, card properties, spacing, illustration purpose, and motion. Identify the intended emotional effect through concrete choices.

Name design tokens where they exist. Do not use unsupported aesthetic adjectives as the specification.

Hide decorative icons from screen readers. Reduce or remove illustrations that displace essential content on compact screens.

## Motion

Define each transition's trigger, purpose, duration, and reduced-motion behavior. Motion must explain a state change.

Suggested duration classes are 0–100 ms for immediate toggles, 150–250 ms for brief transitions, and 250–400 ms for screen transitions.

These ranges are design starting points, not platform requirements. Use project conventions and verify actual behavior.

Avoid longer motion unless the task requires it. Do not delay critical warnings. Do not use motion as the sole feedback.

Avoid decorative loops on task screens. Do not imply measured progress with an indefinite loading animation. Pair completion motion with text or state change.

## Accessibility

Include accessibility in every task size. Require:

- Semantic labels that describe action outcomes.
- Text explanations for locked and disabled states.
- Specific recovery messages for errors.
- Decorative icons excluded from screen readers.
- Status and warnings that do not rely on color alone.
- System text scaling without lost actions or clipped critical content.
- Appropriate target sizes and spacing.
- Logical focus order and correct focus after dialogs.
- Meaningful state announcements.
- Reduced motion and accessible task completion.

State the applicable platform and target-size standard. For web, check WCAG 2.2 SC 2.5.8 and its documented exceptions.

For native mobile, follow the platform or established design-system target requirements. Define hit-area padding when icons are smaller than the required target.

Check adjacent-target spacing in dense controls. Specify contrast, labels, roles, values, announcements, focus, and persistent readable errors.

## Tokens and components

Use the existing token by name. If no token fits, propose a role that follows project naming.

Label proposed roles clearly. If the role or component requires a scope change, report the gap before implementation.

For each element, specify its component, token roles, and applicable state limits. Do not invent installed token names.

## Product copy

Write short, direct titles and instructions. Begin action labels with a verb. State errors and recovery steps specifically.

Avoid blame, unsupported promises, and unfamiliar terms. Localize meaning. Keep the required product language and expert-review rules.

Keep product copy separate from professional advice in sensitive domains.

## Blocking conditions

Stop before final design or implementation when an unresolved condition affects correctness:

- Unknown users or an unclear primary action.
- Unrelated goals combined in one screen.
- Missing data, states, navigation ownership, or recovery.
- Sensitive claims that need expert review.
- Missing tokens or components that expand scope.
- Unresolved platform or accessibility conflicts.
- Essential content that cannot fit the compact layout.
- A design that makes unavailable functionality appear active.
- Meaning communicated only through color, icons, or motion.
- A new state discovered during implementation.

An explicit choice state can resolve equally important actions. Report the affected contract and proposed correction. Get approval when the design decision requires it.
