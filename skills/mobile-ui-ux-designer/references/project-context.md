# Use actual project context

Read this context before design or implementation. Find project values in existing documentation and source. Do not write example values into the installed skill.

| Area | Values to identify |
|---|---|
| Theme | Theme entrypoint, color, type, spacing, radius, elevation, icons, special surfaces |
| Components | Shell, app bar, buttons, cards, sheets, rows, loading, empty, error, and status components |
| Localization | System, paths, locales, key format, right-to-left support, expert-review requirements |
| Checks | Analysis, tests, lint, visual tests, device targets, and review process |
| Domain | Sensitive content, expert review, authority limits, and locale risks |
| Targets | Framework, minimum platforms, compact sizes, text scaling, dark mode, tablets, and foldables |

Record actual component names and locations. Search for existing components before creating new ones.

If context is missing, examine the applicable source or ask a focused question. Do not invent tokens, device support, or domain policy.

## Illustrative cases

For a locked travel screen, explain the missing itinerary and offer a next action. Label preview data as illustrative.

For product filters, keep selected filters and previous results during a failed refresh. Provide a clear reset action.

For health measurements, validate inputs and keep them on failure. Confirm storage without implying a diagnosis.

For offline tools, state which actions stay available. Label stale data. Queue synchronization only when the product supports it.

These cases show contract structure. They are not requirements for unrelated products.
