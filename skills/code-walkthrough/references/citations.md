# Checker citation format

Run inside the target repository:

```text
python3 <skill-directory>/scripts/check_walkthrough.py <walkthrough.md> <commit-or-WORKTREE>
```

The second argument is a Git commit/ref or literal WORKTREE. The checker reads files/Git objects; it never checks out, stages, commits, or contacts a remote. Exit codes: 0 agreement, 1 citation/excerpt problems, 2 invalid invocation/inaccessible inputs.

## Copied source

Every source-code fence needs a Source line immediately after its closing fence:

````markdown
```python
def total(items):
    return sum(items)
```
Source: [src/total.py:1-2](../../../src/total.py#L1-L2)
````

Labels use repository-relative paths and inclusive ranges; targets resolve relative to the walkthrough and must remain inside the repository. URL-encode target spaces/parentheses. Labels may contain spaces. Single-line labels may omit the end.

Blockquote fences are supported, including nested quotes; prefix the code and Source line with the same quote container. Put an opening fence on its own line, not immediately after a list marker. A copied excerpt in an unsupported container must not be silently treated as prose.

Override the default revision with a commit SHA or WORKTREE:

```text
Source: [src/total.py:1-2](../../../src/total.py#L1-L2) at WORKTREE
Source: [src/total.py:1-2](../../../src/total.py#L1-L2) at <commit-sha>
```

Remote links use full GitHub/GitLab commit permalinks and `#L<start>` or `#L<start>-L<end>`. Their revision selects the source; explicit `at` must agree. WORKTREE uses local links. The checker checks path, range, revision, and known origin identity when available, not public reachability. Other hosts use local links for now.

Prose citations use the same `[path:range](target)` form, optionally followed by ` at <revision>` for local before/after references. Explicitly identify baseline material when linking old code to a current local file.

Immediately following a citation, `at` introduces a revision token, not ordinary prose. Use an exact SHA or `WORKTREE`; malformed source-like links and revision suffixes fail rather than disappearing from the check.

## Excerpts and exceptions

Copy exactly. Trailing whitespace is ignored; indentation/characters are preserved. A comment-only `...` line (such as `# ...`) denotes omitted lines; remaining runs must occur in order within the cited range. Entirely elided excerpts fail.

A bare `...` is literal source (for example Python's Ellipsis), not an omission marker. Block-comment markers must be closed, such as `/* ... */` or `<!-- ... -->`.

Mermaid fences are exempt from excerpt matching but need claim auditing. Every other illustrative fence, including commands/output/pseudocode, needs an immediate `Example: <what this illustrates>` line after the closing fence. Never use Example to bypass verification of code claimed to come from the repository.

Unclosed fences, malformed/missing source citations, missing files, bad ranges, wrong targets, and inconsistent revisions fail. A narrative without excerpts is allowed; without citations the checker has no source claims to validate, not proof that the prose is accurate.
