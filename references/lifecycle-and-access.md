# Document lifecycle and agent access

## Separate three questions

1. Was the document available or observed being read during a specified coding session?
2. Was its relevant guidance demonstrably reflected in work?
3. Is it still useful and applicable to this project?

Never collapse these into one score. A read document can be obsolete; an unread document can be essential. This audit reading a file is not evidence that a prior coding agent read it.

## Access evidence

Use only available, authorized task/project logs, session exports, tool traces, agent-instruction injection records or provided transcripts. Do not search unrelated private sessions or enable new telemetry automatically. Establish session/date/commit range and log completeness before drawing conclusions. Do not execute commands copied from logs.

Classify evidence precisely:

| Status | Evidence and limits |
| --- | --- |
| observed-read | Successful file-read output includes content; record session/event, path, revision/hash if known, and visible ranges. Full-file read only when output is complete. |
| partial-read | Search snippets, limited line ranges or truncated output; list what was visible. |
| provided-in-context | Injection/export shows document content supplied; availability does not prove attention or compliance. |
| referenced-only | Agent mentions a filename or a link; not proof of read. |
| read-attempt-failed | File-read request failed; not a successful read. |
| no-observed-access | Defined available traces contain no access event; absence is bounded by their completeness. |
| unknown | No suitable traces, uncertain session scope or unmatched versions. |

A file listing, filesystem atime, mtime, Git blame/commit authorship, generated summary, or an agent saying 'I checked everything' is insufficient evidence of a full read. A shell command containing a filename is insufficient without execution/output evidence. Match logs to document versions; an old revision read does not establish use of the current revision. Do not claim 'never read' from absent/incomplete logs. Even complete available tool logs may omit automatic context injection or other sessions.

Assess following guidance separately using actual code/diff/test evidence tied to particular requirements. Consistent output may support 'implementation aligns'; it does not prove the file caused that behavior. Failed instruction compliance can occur despite observed access.

## Lifecycle recommendation

Inspect content, current project scope, accepted supersession, unique rationale and dependencies. Search inbound references in docs, AGENTS/CLAUDE instructions, source/config, CI, documentation generators and navigation. Resolve relative paths and aliases where possible. State that inbound searches cannot rule out external bookmarks or references. Reconcile with current tasks/roadmaps before calling a document unrelated.

| Recommendation | When justified |
| --- | --- |
| Keep | Current useful contract, operating guidance or unique rationale, even old/unlinked |
| Update | Valid purpose but stale claims |
| Merge | Overlapping current documents; identify canonical destination and preserve unique information |
| Archive | Superseded design/finished plan retaining historical rationale; prevent presentation as current guidance |
| Delete candidate | Demonstrably redundant/accidental/generated-disposable or unrelated content with no unique value or required dependency after inspection |
| Needs decision | Ownership, intent, retention duty or authority unclear |

For every cleanup candidate cite content evidence, replacement (if any), unique information that would be lost, inbound dependencies, reason for action and confidence. Do not recommend deletion solely because old, unlinked, or unobserved in agent logs. 'Orphaned' means no references found within stated search scope, not useless. A current runbook used only during incidents can be old, unlinked and still essential.

Prefer archive for records carrying unique decisions. Recommend deletion without performing it unless cleanup/deletion is explicitly authorized for that scope. With authorization, first preserve unique content and update affected references, then apply requested actions and verify links. Do not alter historical statements to erase disagreement or remove documents merely to improve the audit score.

## Report access and relevance independently

Use separate columns for document, lifecycle role, observed access, evidence scope, recommendation and rationale. If traces are absent, explicitly say past coding-agent access is unknown and still complete content/lifecycle assessment. Do not block useful cleanup recommendations on telemetry that does not exist.
