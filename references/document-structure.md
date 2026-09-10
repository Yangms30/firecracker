# Document structure and agent navigation

## Purpose and basis

Check whether agents can locate the right project knowledge and read the necessary detail without unrelated context. This is a documentation organization review, not an architecture redesign, readability rewrite or automatic harness installation.

OpenAI's [harness engineering account](https://openai.com/index/harness-engineering/) describes a short AGENTS.md pointing into a structured docs/ knowledge base, progressive disclosure, and link/freshness checks. Its roughly 100-line entrypoint is a case-specific example, not a universal limit. The code-adjacent placement option below is our contextual recommendation, not a requirement from that account. Use a user-supplied reference when provided; identify its scope and do not invent its rules if unavailable.

## Inspect and interpret

| Dimension | Evidence to inspect | Recommendation when justified |
| --- | --- | --- |
| Entry navigation | Can a relevant task reach current guidance from the root or module entrypoint? Are links labeled with purpose and when to read? | Add a concise gateway with topic links and scope, rather than duplicating full detail |
| Length and cohesion | Lines/bytes, headings, repeated sections, unrelated tasks mixed together, exceptions far from their rule | Split coherent subjects only when it improves retrieval or independent maintenance; retain necessary conditions and rationale |
| Placement | Existing docs conventions, module ownership, code change boundaries, site generator sources, audience | Place module-specific details beside code or under a matching docs module; retain shared policies and architecture centrally |
| Authority | Multiple copies of the same current rule; summaries diverging from detail | Keep a maintained canonical source and link scoped summaries to it; retain necessary entrypoint constraints and intentional repetition required for effective loading |
| Lifecycle | Current instructions mixed with proposals, completed plans or historic rationale | Clarify status and navigation; preserve the historical record |
| Fragmentation | Tiny files requiring many hops for one task; circular or ambiguous routing | Consolidate related detail or improve direct links; do not optimize for file count alone |
| Harness behavior | Instruction-file hierarchy, automatic injection, project overrides and required constraints | Preserve effective instruction scope; keep critical always-applicable constraints available at the required entrypoint |

Counts identify candidates for closer reading. Do not use a fixed line/token ceiling, a language-biased word count, or an invented quality score to declare failure. If tokens are measured, name the tokenizer; otherwise label estimates or use lines/bytes. A long cohesive API reference with stable anchors can be appropriate. A short file with contradictory rules is still defective.

## Choose placement by responsibility

Possible layout, not a migration requirement:

- Root README or AGENTS.md: concise orientation, critical applicable constraints, links to task-specific detail.
- docs/architecture.md or existing equivalent: shared architecture and cross-module decisions.
- src/payments/README.md: payment implementation details that evolve with that module, if repository conventions permit it.
- docs/payments/: equally valid central alternative, linked from the module or root gateway.
- Existing plans/archive locations: future and historical records with explicit status.

Do not create competing copies in both locations. A gateway should explain what each destination covers, when it applies, and where authority resides. A link does not prove the agent follows it or that a harness automatically loads the linked content. Before editing instruction entrypoints, verify the actual host's loading/inheritance rules using available configuration and current official documentation. If unknown, leave instruction scope unchanged and state the limitation.

## Findings and structural plans

Report navigational/structural recommendations separately from factual contradictions. Include path/section, observed obstruction (for example three unrelated workflows in one entrypoint), size measurements if useful, intended readers/tasks, and the smallest beneficial change. Do not recommend splitting just because a document is old, large or in docs/.

For a split or move, map original sections to proposed files; specify what remains in the gateway, where the canonical rule will live, and how relative links, anchors, imports/includes, generator navigation and incoming references change. Check for unique warnings, examples, exceptions and historical rationale that could be lost. State any change to instruction scope and leave unresolved policy decisions untouched.

During authorized execution, preserve content meaning, fix affected internal links and anchors, validate existing documentation builds where relevant, and re-run the semantic comparison and coverage inventory. Check that a reader starting at the original entrypoint can still reach every required topic. For external links you cannot update, report the limitation and consider a forwarding stub when compatible with project conventions. Do not install hooks, telemetry or CI merely to implement a structural recommendation.
