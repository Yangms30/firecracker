# Evidence and coverage

## Ledger

Preserve root, snapshot, candidate paths/hashes, exclusions and traversal errors. Add role, scope/status, reviewed ranges/extraction coverage, topics and non-review reasons. States:

| State | Meaning |
| --- | --- |
| pending | Discovered, not reviewed |
| reviewed | Full relevant content read and claims compared in applicable topic groups |
| partial | Some content reviewed; missing ranges/pages/diagrams listed |
| blocked | Cannot read/interpret with available tools; explain |
| excluded | Explicit scope exclusion with reason, not a semantic pass |

Historical/proposed documents are not automatically excluded: read to classify and detect misleading current references. Suggested claim fields: topic, claim, modality, conditions, environment, effective release, status, path, location, authority evidence. Preserve original excerpts for findings.

Scanner counts describe discovery, not audit completeness. Known documentation suffixes, common extensionless names, and include globs select candidates. Classify JSON/YAML/XML because they can be executable configuration. Treat code/config corroboration separately. Add unsupported formats and image-only diagrams manually when needed. Symlinks and pruned directories are boundaries, not enumerated contents.

## Findings

Record a stable topic-based ID, category/severity, applicable scope, source excerpts and locations, authority evidence, consequence, proposed/applied patch and verification. High severity means behavior/contract/permission conflict; medium means consequential ambiguity or missing propagation; low means naming/reference issues without behavioral impact. Severity and confidence are separate. For omissions cite the accepted change plus why that document must cover it.

Reasoning boundaries:

- Approved spec requires user approval before drafting; API docs say upload immediately enqueues drafting: possible contradiction. Upload preprocessing can coexist with approval-gated drafting.
- An old meeting record proposing automatic drafting is history; do not rewrite it to today's decision.
- Production MSSQL and local MariaDB can coexist when environment is explicit.
- Two accepted retention policies conflict with no supersession: report unresolved; do not pick newest file or shortest duration.
- Accepted v2 target with v1 deployed needs accurate implementation status, not a false claim that v2 shipped.
- Font token docs need not mention approval flows.

## Large/incremental audits

Read bounded sections and retain decisions/source locations. Compare topic groups globally after reading; isolated per-file summaries miss contradictions. Revisit original passages for findings. Search synonyms and dependent behaviors, including unchanged files. Reuse cached reviews only with content plus dependency/authority evidence; expand scope when dependency relationships are incomplete. Surface additions/deletions/renames and revised scope/extraction capability.

## Output

Lead with findings/repairs and unresolved decisions. Include an evidence table and coverage: candidate count, reviewed, partial, blocked, pending, excluded files, pruned directories and traversal errors. Keep boundaries separate from file counts. Label full/partial and document-only/selectively corroborated scope. Provide proposals in audit mode, a concrete change plan in plan mode, and actual repairs in execute mode. Include document totals/folder roles, the implementation map, traced and uninspected code flows, and the distinction between static, tested and deployed evidence. Save a detailed ledger temporarily or at a requested report location, not as an unsolicited permanent project index.
