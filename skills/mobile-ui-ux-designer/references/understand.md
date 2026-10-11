# Understand the mobile task

## Clarify the outcome

Resolve available context before asking the developer. Identify the user problem, primary user, next action, visible content, and deferred content.

Identify the screen's purpose: information, a transaction, navigation, education, or an operational task. Check whether users act under stress, offline, or while moving.

State the cost of misunderstanding. Ask only when uncertainty materially affects design correctness.

## Read local context

Read narrowly until the task is bounded. Prefer these sources:

1. Applicable project instructions.
2. Product requirements and existing design documents.
3. Design tokens and typography.
4. Existing screens in the same flow.
5. Reusable components.
6. Navigation and routing.
7. Localization and locale-specific formats.
8. Applicable analytics events.
9. Tests, snapshots, and visual regression checks.

When shipped behavior and documentation disagree, report the difference. Do not silently replace an approved requirement with existing behavior.

For MEDIUM and HIGH tasks, record sources read and sources intentionally omitted.

## Research patterns

For MEDIUM and HIGH tasks, research before design unless browsing is unavailable or the user requests otherwise.

Prefer official Apple, Android, Material, and W3C guidance. Use established applications and usability research as secondary evidence. Do not copy competitor interfaces.

Extract only applicable navigation, hierarchy, interactions, states, accessibility, trust, and offline patterns.

Use at most five research rows unless requested otherwise:

| Source | Observed finding | Design effect | Evidence limit |
|---|---|---|---|
| Actual source | Supported observation | Applicable decision | Unknown or untested detail |

Disclose unavailable research. Do not invent a source or measured outcome.

## Model the user

For MEDIUM and HIGH tasks, record:

- Primary and secondary users, skill level, and emotional context.
- Environment, time pressure, connectivity, and likely one-handed use.
- Accessibility, localization, trust, and mistake risks.
- Primary success action and recovery action.

For sensitive screens, separate product guidance, choices, warnings, expert referral, emergency action, and product limits.

Do not imply medical, legal, financial, or religious authority that the product lacks. Get appropriate expert review for sensitive claims.

## Localization

Check layout direction as well as text direction for right-to-left languages. Use locale-appropriate dates, times, numbers, and currency.

Keep meaning across locales. Do not assume that literal translation keeps trust or usability. Flag sensitive cultural terms for expert review.

## Prioritize content

| Content | Priority | Placement |
|---|---|---|
| Title, essential instruction, primary action | P0 | Visible or available through an obvious first action |
| Status and necessary explanation | P0 or P1 | Visible when needed, or one action away |
| Critical warning | As required by risk | Visible at the applicable decision |
| Optional education | P2 | Deferred detail |
| Rare help or exception | P3 | Help, sheet, or disclosure control |

If all content appears P0, revise the hierarchy. Keep P3 content out of the primary action area. Do not hide critical warnings.

## Responsive classes

Use responsive classes instead of one device model. These planning ranges do not replace framework or platform guidance:

| Class | Approximate width | Primary risk |
|---|---|---|
| Small compact | 320–374 pt or dp | Crowding and clipped actions |
| Standard compact | 375–430 pt or dp | Default phone layout |
| Large compact | 431–480 pt or dp | Weak hierarchy or excess spacing |
| Medium | 600–839 dp | Navigation and pane choice |
| Expanded | 840 dp or more | Excessive content width |
| Short landscape | Variable | Keyboard and height constraints |

Do not treat pt, dp, and CSS pixels as interchangeable units. State the target platform and unit.

For MEDIUM and HIGH work, define compact layouts, safe areas, keyboard behavior, scroll regions, and sticky areas.

Also define sheets, offline behavior, and font scaling.

## Platform conventions

Check navigation, system back, primary actions, dialogs, typography, motion, accessibility, and system UI regions.

Use the established design system when it resolves a platform difference. Use native behavior at runtime when the framework supports it.

If one shared behavior is necessary, select the least confusing option for the primary users. Keep task clarity, accessibility, and recovery.

Record the alternatives and reason. Require platform-specific checks for the chosen behavior.
