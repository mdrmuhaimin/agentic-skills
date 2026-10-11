# Review and implement the design

## Review the contract

Check user clarity, content hierarchy, states, wireframes, visual specifics, motion, accessibility, and implementation readiness.

The screen's purpose should be identifiable quickly, with three seconds as a usability-test target. Do not claim this result without observation.

Check that essential content and actions stay available on compact screens. Keep optional detail deferred. Check every required recovery path.

Check component labels, region markers, responsive differences, and token roles. Make sure that localization keys and applicable analytics events are correct.

Score required areas from one to five as an editing aid. Revise an area below four. Do not report self-scores as user-test evidence.

If missing context prevents correction, report the specific problem and decision needed.

## Usability plan

For HIGH work, prepare a usability test plan. MEDIUM work can use one when it adds useful evidence.

| Test | Success | Correction if unsuccessful |
|---|---|---|
| Identify the screen purpose | User names the intended task | Improve title or status |
| Select the next action | User selects the correct action | Adjust hierarchy |
| Recover from an error | User finds the next step | Add a recovery action |
| Use large text | User completes the task without hidden content | Adjust layout |
| Explain an icon | User recognizes its meaning | Add a label or remove it |

## Implementation handoff

For each affected component, record purpose, props, state, reusable components, justified new components, tokens, interactions, and motion.

Also record accessibility, localization, analytics, and platform differences.

Also record prohibited behavior and verification requirements. Include a wireframe and state model when the task needs them.

For LOW work, give the issue, change, reason, reuse, accessibility, tokens, implementation note, decision, and checks.

For MEDIUM work, add the user context, research, hierarchy, states, interactions, responsive layout, visual treatment, motion, and copy.

For HIGH work, add the full flow, platform decisions, usability plan, and approval record. Omit irrelevant headings instead of empty template content.

## Approval

For HIGH work, get explicit design approval before final delivery or implementation.

For changes to navigation or core product behavior, get the same approval.

Also get approval for sensitive screens, new system components, onboarding, payments, identity, permissions, trust, or data sharing.

Present the design as a draft until approval occurs. Design-only work must also follow this rule.

If a blocking condition occurred, get approval for its resolution before final delivery or implementation.

Follow a request for review before implementation. Clear approval for the same design counts.

Silence does not count. Implementation approval does not authorize publication or deployment.

## Implement

1. Reread the approved design contract.
2. Recheck project design conventions.
3. Reuse existing components.
4. Implement one state at a time.
5. Use design tokens for styling.
6. Use localization keys for copy.
7. Keep native navigation behavior.
8. Add accessibility semantics.
9. Add only motion that clarifies state.
10. Check compact layouts and text scaling.
11. Run the applicable project checks.

Replan when components, states, localization, tokens, accessibility, or reduced motion cannot meet the contract. Also replan false data or inaccessible compact content.

Record the affected section and proposed revision. Request a decision when the approval rules apply.

## Execute checks

Discover commands from the actual repository. These are examples, not assumed project commands:

```sh
# Flutter example
flutter analyze
flutter test

# React Native or web example
npm test
npm run lint
```

Search actual component, semantics, token, and localization paths. Do not invent paths or commands.

For implemented UI changes, check the rendered screen. Text analysis alone cannot establish layout, contrast, keyboard, or large-text correctness.

Check small, standard, and large compact layouts. Also check supported dark mode, right-to-left layouts, errors, empty states, and loading states.

Check sheet height, scroll, focus, safe areas, and primary-action access. Capture before/after screenshots or device captures when available.

If rendered checks are unavailable, state that device or browser review stays required. Report which checks ran and which did not.
