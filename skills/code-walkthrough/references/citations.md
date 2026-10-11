# Checker citation format

Run the checker inside the target repository:

```text
python3 <skill-directory>/scripts/check_walkthrough.py <walkthrough.md> <commit-or-WORKTREE>
```

The second argument is a Git commit or ref, or literal WORKTREE. The checker reads files and Git objects. It does not change Git state or contact a remote.

| Exit code | Meaning |
|---|---|
| 0 | Source agreement |
| 1 | Citation or excerpt problems |
| 2 | Invalid arguments or inaccessible inputs |

## Copied source

Put a Source line immediately after every copied source-code fence:

````markdown
```python
def total(items):
    return sum(items)
```
Source: [src/total.py:1-2](../../../src/total.py#L1-L2)
````

Use repository-relative paths and inclusive line ranges in labels. Targets resolve relative to the walkthrough. Targets must stay inside the repository.

URL-encode spaces and parentheses in targets. Labels can contain spaces. For one line, you can omit the end number.

The checker supports blockquote fences, including nested quotes. Use the same quote prefix for code and the Source line.

Put the opening fence on its own line. Do not put it directly after a list marker. Do not treat an unsupported copied-source container as prose.

Use a commit SHA or WORKTREE to override the default revision:

```text
Source: [src/total.py:1-2](../../../src/total.py#L1-L2) at WORKTREE
Source: [src/total.py:1-2](../../../src/total.py#L1-L2) at <commit-sha>
```

Use full GitHub or GitLab commit permalinks for remote citations. Use anchors `#L<start>` or `#L<start>-L<end>`.

The remote link selects the revision. An explicit `at` token must agree with it. WORKTREE requires local links.

The checker compares the path, range, revision, and known origin identity. It does not check public reachability. Use local links for other hosts.

Use the same citation form for prose. Add ` at <revision>` for local references to a different source state.

Identify baseline sources when an old-code citation targets a current local file. Immediately after a citation, `at` introduces a revision token.

Use an exact SHA or WORKTREE for that token. Malformed source labels, links, ranges, and revision tokens fail.

## Excerpts and exceptions

Copy source exactly. The checker ignores trailing whitespace but keeps indentation and other characters.

A comment-only `...` line marks omitted source, such as `# ...`. Remaining runs must occur in order within the cited range.

An excerpt with all content omitted fails. A bare `...` means literal source, such as Python Ellipsis.

Close block-comment omission markers, such as `/* ... */` or `<!-- ... -->`.

Mermaid fences do not require excerpt comparison. Include their factual labels in the claim audit.

For any other illustrative fence, put `Example: <purpose>` immediately after its closing fence. This rule includes illustrative commands, output, pseudocode, and ASCII diagrams.

Do not use Example to bypass checks for copied repository code.

Unclosed fences, missing citations, missing files, invalid ranges, wrong targets, and conflicting revisions fail.

A walkthrough without excerpts is permitted. Without citations, the checker has no source claims to compare. It does not establish prose accuracy.
