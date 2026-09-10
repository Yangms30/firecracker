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

## Calibrate recommendations

Use facts → interpretation → unresolved decision → proposed action when intent affects the repair. Mark confidence in the observation separately from confidence in the proposed resolution. Keep uncertainty attached throughout summaries, plans and edits. A high-confidence mismatch can still require a user decision.

Examples of inference boundaries (not project-specific rules):

- A username field does not alone establish whether identifiers are names or emails. Trace input validation and authentication. Even demonstrated name-based login does not prove email login is a future plan: it might be an unmet requirement or an abandoned idea.
- Configuration routing traffic to one backend does not establish the purpose of another backend. Report the inspected route and contract differences; do not label the other service rollback-only without evidence. Configuration alone is not live deployment proof.
- An implemented endpoint or new commit does not automatically make every omission a documentation defect. Check the document's role/status: a product overview may need a capability summary; an exhaustive API contract may need paths, permissions and parameters.

## Separate review coverage from verification

Maintain distinct records; do not mix their denominators or completion states:

1. **Documentation coverage:** candidate count, role classification, reviewed/partial/blocked/pending/excluded paths and structural-review result. Explain excluded generated artifacts without elevating disposable caches into substantive documentation problems.
2. **Implementation/configuration coverage:** inspected modules and flows, static versus observed runtime evidence, partial reads such as dependency lockfiles, and uninspected boundaries. A configuration file can serve both roles; mark the overlap instead of silently double-counting.
3. **Verification attempts:** check/command, target environment, observed result, what it supports, and what it does not establish. Distinguish passed, failed assertion, blocked execution and not run. A Docker/tool failure is not a document-read failure or a failed business assertion.

Reconcile document state counts to the declared document population and retain a path-level ledger. If inventory candidates are reclassified as implementation/configuration artifacts, show that transition. Report document-structure assessment even if no restructuring is warranted; silence is not a pass.

Keep verification proportional to the finding. Reuse relevant observed results; do not run broad suites, builds or remote checks merely to fill the report. Use only task-relevant authorized environments. A page HTTP 200 establishes a response, not a functioning authenticated workflow. An anonymous HTTP 401 does not prove role authorization for all users. Matching migration lists does not prove all deployed constraints or business data are correct. Lint/build/test success supports only the inspected or exercised properties. State the limits without inventing extra blockers for supported document findings.
