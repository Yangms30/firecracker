# Implementation evidence and change plans

## Implementation map

Start with repository instructions, manifests and entrypoints, then inspect the code responsible for the documented behaviors. Use a compact map:

| Topic | Documents / role | Source path and locations | Flow and conditions | Evidence / revision / environment | Unchecked boundaries |
| --- | --- | --- | --- | --- | --- |

Follow applicable paths such as UI → API → service → queue → worker → storage. Do not impose this architecture on projects that do not have it. Read conditions, defaults, error paths, retries, permissions, configuration overrides and relevant tests. A queue consumer may enforce a rule absent from its producer; a UI guard alone may not enforce an API contract. Connect separate paths when they implement the same claim.

Record what is checked out and what environment configuration is known without exposing secret values. Static code supports a statement about the inspected implementation; passing tests support only the exercised cases. Deployment claims need deployment evidence. A test name, mock or commented implementation is not proof of live behavior.

## Interpret disagreements

| Evidence | Treatment |
| --- | --- |
| Accepted requirement and implementation agree; derived guide differs | Propose a documentation repair |
| Implementation violates an accepted requirement | Report an implementation defect; preserve the requirement |
| Accepted target is not implemented yet | Keep target and current state distinct; fix misleading completion language |
| Environments or rollout phases differ | Preserve differences and clarify scope where needed |
| Old proposal or meeting record differs | Preserve historical meaning; check whether current navigation misrepresents it |
| Equally applicable decisions conflict without supersession | Flag an unresolved decision; do not select by timestamp or majority |

Absent code access limits implementation conclusions, not all document comparison. List missing modules/flows and unresolved external boundaries. Do not infer that a document is unnecessary because its subject has no implementation: it may define required future work or a manual procedure.

## Reviewable change plan

For each action include finding ID, file/section, current and proposed meaning, decision evidence, dependencies/order, reference impact and verification. Record exclusions and unresolved decisions. Preserve historical rationale and valid scope differences. Recommend archive/delete candidates separately with their evidence and required authorization.

Suggested plan columns: finding → target → proposed change → reason → dependencies → verification → status. A plan is not an applied change. If files or decisions changed since review, reread them and revise affected actions before execution.

Default handoff: audit report → user requests changes → concrete plan → user authorizes execution → repairs and verification. An explicit request to plan and execute, or existing authorization for a concrete plan, skips a redundant approval pause. Explain any pause as Firecracker's staged workflow rather than an unspecified platform restriction.
