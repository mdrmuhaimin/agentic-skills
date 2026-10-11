---
name: mobile-ui-ux-designer
description: Design mobile screens and flows with research, responsive layouts, accessibility, motion, component reuse, and implementation handoffs for native and cross-platform applications.
license: MIT
metadata:
  author: custom
  version: "3.1"
---

# Mobile user interface and user experience design

Accept a feature, requirement, screenshot, wireframe, user flow, critique, or implementation request. Define the user's goal before visual design.

## Start

1. Read the applicable project instructions and product context.
2. Identify the user, primary action, current problem, and failure risks.
3. Find existing components, design tokens, navigation, localization, and tests.
4. Select the task size below.

A design token is a named value for color, spacing, type, or another visual property. Use existing tokens before arbitrary values.

| Size | Scope | Output budget |
|---|---|---|
| LOW | One copy, component, spacing, or state change | 300–600 words |
| MEDIUM | One screen, form, sheet, or flow step | 900–1,600 words |
| HIGH | Several screens, sensitive flows, or design-system work | 1,800–3,500 words |

For context and research, read [understand.md](references/understand.md). For design contracts and limits, read [design.md](references/design.md).

For review or implementation, read [verify.md](references/verify.md). Get actual project values through [project-context.md](references/project-context.md).

## Design requirements

Make essential content and the next action available on compact screens. Explain any constraint from large text, localization, keyboards, or safety warnings.

Use one dominant action in a usual task state. For equal alternatives, define an explicit choice state. Do not weaken a legitimate peer action.

Give error, empty, locked, and disabled states a clear next step. Explain unavailable features honestly. Keep user input on failure.

Specify concrete components, token roles, and behavior. Do not use vague design descriptions such as “modern” or “premium.”

Keep accessibility in every task size. Respect reduced motion. Use more than color or icons to communicate meaning.

Do not invent research. If browsing is unavailable, disclose the limit. Use verified local context and known platform constraints.

Merge overlapping sections. Omit irrelevant template sections. Keep the design and handoff within the selected budget.

## Language and decisions

Use ASD-STE100 writing rules: active voice, simple verbs, consistent defined terms, and no contractions or semicolons.

Limit instructions to 20 words per sentence and descriptions to 25 words. Keep one topic and at most six sentences per paragraph.

Keep exact token names, interface labels, and quotations. Use the project's required locale for product copy.

Resolve unknown user goals, inaccessible states, missing data, and material scope changes before final design. Follow the approval rules in [verify.md](references/verify.md).

Approval already given for the same design stays valid. Do not infer approval from silence. Do not implement or publish beyond the authorized task.
