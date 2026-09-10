<p align="center">
  <img src="assets/hero.svg" width="960" alt="Firecracker: a shared firework above documents with different perspectives">
</p>

<h1 align="center">Firecracker</h1>
<p align="center"><strong>Different perspectives. One shared spark.</strong></p>
<p align="center">Keep project documents aligned as the project evolves.</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.ko.md">한국어</a> · <a href="README.zh-CN.md">简体中文</a>
</p>

---

**More documents. More decisions. Are they still pointing in the same direction?**

As a project grows, specifications, implementation plans, API guides and runbooks accumulate. Decisions move forward, but their explanations do not always move together. A document can look perfectly reasonable on its own while contradicting the rest of the project.

**Firecracker checks whether your growing documentation still follows your project's accepted direction.** It connects document claims to existing decisions and relevant implementation, shows where they diverge, and helps you review a repair plan before changes are made.

Different perspectives. One shared spark. Your project defines the spark; each document keeps its own viewpoint.

## When to light it up

- A feature moved from **A to A+**, and you are unsure whether every affected document caught up.
- Several people or coding agents have written documents across many folders.
- You are returning to a project and cannot tell which guides are current, proposed or historical.
- Before a handoff or release, you want to see conflicting instructions and missing updates.
- You want cleanup recommendations without treating every old document as disposable.

## Your direction stays yours

Firecracker's role is to check consistency against the decisions already made for your project. It does not choose a new product direction, architecture or policy as part of a documentation audit.

| Your concern | How the workflow addresses it |
| --- | --- |
| “What if it misunderstands my project?” | Shows the decision basis, scope and source passages for findings. Unclear intent is reported as unresolved, and affected content is left unchanged. You can correct the interpretation before execution. |
| “Will it rewrite a correct document to match buggy code?” | Separates accepted requirements from observed implementation. A code defect is reported as a code defect; it is not grounds to weaken the requirement. |
| “Will every document be forced to say the same thing?” | Preserves document roles, environment differences, future targets and historical records. Only incompatible claims within the same applicable scope are conflicts. |
| “Will checking the project change files?” | The default audit is read-only. It reports findings and recommendations first. Changes follow a concrete plan and execution authorization. |
| “Will old documents disappear?” | Age, missing links and absent read logs alone do not justify deletion. Cleanup candidates include their rationale and reference impact; deletion requires explicit authorization. |

These are operating rules, not a guarantee of perfect understanding. Firecracker can miss context or misinterpret evidence. Its findings are reviewable proposals, with uncertainty and uninspected areas made visible. You remain the authority on unresolved project intent.

**Start with a check. Review the evidence. Decide what should change.** If you explicitly ask it to plan and execute together, it proceeds within that authorization without another confirmation.

[Install](#install) · [Before / after](#before--after) · [Usage](#usage) · [Limits](#limits)

## Install

### Install from your terminal

Run this in your terminal (requires Node.js and npm):

```bash
npx skills add Yangms30/firecracker -a codex -g
```

`-a codex` selects Codex; `-g` installs for your user across projects. Omit `-g` to install only in the current project. This uses the community [skills CLI](https://github.com/vercel-labs/skills#install-a-skill). Python 3 is also needed when running Firecracker's inventory helper.

### Install through Codex chat

Alternatively, paste the following request into the **Codex chat input**, with the built-in skill installer available. This is a prompt, not a terminal command:

```text
$skill-installer Install Firecracker from https://github.com/Yangms30/firecracker.
SKILL.md is at the repository root. Include scripts/, references/, agents/ and assets/.
```

<details>
<summary>Manual installation · macOS / Linux</summary>

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/Yangms30/firecracker.git ~/.agents/skills/firecracker
```

Use an unused destination; if Firecracker is already installed, update that installation instead of cloning over it. For one project, copy the complete folder to `<project>/.agents/skills/firecracker/` instead.

Keep `SKILL.md`, `scripts/`, `references/`, `agents/` and `assets/` together. Python 3 is needed for the inventory helper. See the [official Codex skill guide](https://learn.chatgpt.com/docs/build-skills).

</details>

Then open the project you want to inspect and ask:

```text
$firecracker Audit this project's documents for conflicting decisions and stale guidance.
Do not edit files. Report evidence, cleanup candidates, and actual review coverage.
```

## Before / after

**Illustrative example:** the accepted decision now requires approval before draft generation. Upload preprocessing is still allowed.

| Document | Before | After an authorized repair |
| --- | --- | --- |
| Accepted specification | Generate only after approval | Preserved as the governing decision |
| API guide | Upload immediately starts drafting | Upload prepares sources; approval starts drafting |
| Runbook | Retry drafting after every upload | Retry only an approved drafting job |
| Old meeting notes | Proposal to draft automatically | Preserved as history |
| Visual design guide | Typography and spacing | Preserved; no approval-flow content required |

**Shared direction does not mean identical content.** Different environments, future plans and historical records can legitimately say different things.

## What it checks

| Area | What you get |
| --- | --- |
| Conflicting claims | Incompatible requirements with source locations and scope |
| Missing change propagation | Documents that still describe an earlier accepted behavior |
| Terminology and status | Renamed contracts, broken references, proposals presented as shipped |
| Document lifecycle | Keep, update, merge, archive or delete-candidate recommendations |
| Agent access evidence | Observed reads, partial reads or unknown access from supplied logs |
| Review coverage | Reviewed, pending, partial, blocked and excluded files, plus scan boundaries |

## Usage

**Plan changes after the audit**

```text
$firecracker Based on the audit, prepare a file-by-file change plan with evidence and verification steps.
Do not edit files yet.
Recommend unnecessary documents for deletion; do not delete them.
```

**Follow an accepted change**

```text
$firecracker Draft generation changed from automatic-on-upload to user-approved.
Update affected documents and distinguish the accepted target from what is implemented.
```

**Check previous agent access**

```text
$firecracker Use these coding-session logs to assess document access.
Separately evaluate whether each document is still useful to the project.
```

These are natural-language requests, not additional CLI subcommands. Ask in English, Korean or Chinese; reports follow your language and edits preserve each source document's language.

**Execute a reviewed plan**

```text
$firecracker Apply the reviewed documentation plan and verify the results.
Do not delete documents or change application code.
```

## How it works

1. **Inventory.** Count document candidates and show folders, formats and exclusions.
2. **Classify.** Infer roles from paths and names, then confirm them from content.
3. **Understand implementation.** Map entrypoints and trace relevant features through APIs, jobs, storage, configuration and tests.
4. **Compare.** Separate accepted decisions, current implementation, future targets and history; compare claims with source evidence.
5. **Report.** Explain findings, cleanup suggestions and actual document/code coverage without editing files.
6. **Plan.** When changes are requested, prepare file-level actions, dependencies and verification steps for review.
7. **Execute and recheck.** Apply an approved plan and verify affected topics. An explicit request to plan and execute together does not require another confirmation.

A report connects each finding to its evidence, applicable decision, proposed or applied action, and confidence. Cleanup recommendations also describe replacement documents and references that could be affected.

<details>
<summary>Inside the skill · inventory helper</summary>

| File | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Shared audit and repair instructions |
| [scripts/inventory.py](scripts/inventory.py) | Candidate discovery and content hashes |
| [references/implementation-and-planning.md](references/implementation-and-planning.md) | Implementation evidence and change planning |
| [references/review-guide.md](references/review-guide.md) | Evidence, findings and coverage |
| [references/lifecycle-and-access.md](references/lifecycle-and-access.md) | Cleanup and agent access rules |
| [references/brand.md](references/brand.md) | Fireworks identity and presentation |
| [agents/openai.yaml](agents/openai.yaml) | Codex skill metadata |

From the skill directory:

```bash
python3 scripts/inventory.py /absolute/project/root > /tmp/docs-inventory.json
```

This inventories candidates only. Codex performs the semantic review. The scanner uses known formats and explicit include globs, skips declared dependency/build directories, and does not follow symlinks. Unusual formats need manual assessment; PDF and Office extraction depends on available tools.

</details>

## Limits

- Agreement between documents does not prove the implementation is correct.
- A read event does not prove understanding or compliance. Missing logs mean unknown access.
- Age, missing links or no observed reads alone never justify deletion.
- Conflicting authoritative decisions remain unresolved until evidence or a decision resolves them.
- An audit is read-only. A general change request leads to a concrete plan first; plan approval or an explicit plan-and-execute request authorizes repairs. Deletion needs explicit authorization.
- Coverage is reported honestly, including unreadable files and unreviewed sections.

## Languages and design

[English](README.md) · [한국어](README.ko.md) · [简体中文](README.zh-CN.md)

The three READMEs describe one shared skill. Runtime instructions and reference files are maintained in English; there are no separate language-specific engines. Keep examples, installation steps and limits aligned when updating translations.

Presentation references: [Ponytail](https://github.com/DietrichGebert/ponytail) for clear branding and before/after storytelling; [Kill AI Slop](https://github.com/yetone/kill-ai-slop) for concrete examples and direct installation guidance. Firecracker uses its own fireworks identity and artwork. No affiliation is implied.
