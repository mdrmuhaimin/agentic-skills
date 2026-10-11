# Maintain project instructions

Read this reference only when project instructions need a change. Do not create or modify instruction files merely because this workflow runs.

## Discover the instructions

Find the files that the active host supports, such as `AGENTS.md`, `CLAUDE.md`, or Cursor project rules. Read applicable nested instructions.

Check the host's precedence and discovery rules. Do not assume that every host reads every filename. Identify conflicting instructions before implementation.

Keep one source for shared project guidance when the host supports references. Use small host-specific adapters if necessary. Do not install global rules or change editor permissions automatically.

## Write a short decision guide

Include facts that affect work and that ordinary source inspection cannot reliably reveal. Useful content includes:

- Exact install, build, test, and single-test commands.
- A short map of important project areas.
- Product invariants and architecture boundaries.
- Generated files, environment requirements, and dangerous commands.
- Project style exceptions and authoritative modules.
- Branch, commit, review, and release-note rules.
- Confirmed lessons with links to evidence.

Define **Always**, **Ask first**, and **Never** from real project policy. Keep authorization already given for the same action.

Link to long explanations, domain references, and changing product status. Do not repeat standard language conventions or facts that the code already makes clear.

Use [language.md](language.md). Keep the primary guide short, normally within 100–200 lines. This range is a review signal, not a reason to omit necessary safety instructions.

Use bold text or `IMPORTANT` only for rules that need special attention. Repeated emphasis makes priorities less clear.

A required check belongs in the existing CI or validation system when practical. An instruction file alone does not enforce it. Add automation only within the approved scope.

## Review an instruction change

Before editing instructions, read current official host guidance for project instructions, prompts, and context. Record which sources apply.

1. Identify the problem that the instruction prevents.
2. Check the rule against current code and official tool documentation.
3. Test each changed path or command when safe.
4. Remove stale or duplicate text.
5. Check for conflicts with other instruction files and stored preferences.
6. Compare behavior on a representative task when the change affects the workflow.
7. Present the instruction change through the project's usual review process.

Keep an evidenced lesson specific to the applicable project or code area. Do not store a temporary task correction as a permanent personal preference.

Update stale instructions in the same change that makes them stale. Periodically review the guide, normally every two to four weeks.

Before removing a rule, keep a recoverable copy or Git revision. Do not delete instructions, hooks, skills, or memory without authorization.

Report which documents and commands you checked. A smaller instruction file is useful only if it still guides correct behavior.
