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

Your spec says **A+**. Your README still says **A**. Your runbook quietly assumes **B**.

Firecracker helps Codex find those disagreements, trace the decisions behind them, and repair the documents that have fallen behind. Like people watching one firework from different places, each document keeps its own perspective while following the same applicable direction.

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

**Audit and repair**

```text
$firecracker Inspect the project documents and fix inconsistencies supported by clear evidence.
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

## How it works

1. **Map the documents.** Discover candidates, content hashes, exclusions and unreadable material.
2. **Recover the decisions.** Compare claims by topic, environment, release and authority.
3. **Find the drift.** Check contradictions and missing propagation against original passages.
4. **Repair and verify.** Apply requested, evidence-backed edits, then compare the affected documents again.

A report connects each finding to its evidence, applicable decision, proposed or applied action, and confidence. Cleanup recommendations also describe replacement documents and references that could be affected.

<details>
<summary>Inside the skill · inventory helper</summary>

| File | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Shared audit and repair instructions |
| [scripts/inventory.py](scripts/inventory.py) | Candidate discovery and content hashes |
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
- An audit is read-only. Repair requests permit supported documentation edits; deletion needs explicit authorization.
- Coverage is reported honestly, including unreadable files and unreviewed sections.

## Languages and design

[English](README.md) · [한국어](README.ko.md) · [简体中文](README.zh-CN.md)

The three READMEs describe one shared skill. Runtime instructions and reference files are maintained in English; there are no separate language-specific engines. Keep examples, installation steps and limits aligned when updating translations.

Presentation references: [Ponytail](https://github.com/DietrichGebert/ponytail) for clear branding and before/after storytelling; [Kill AI Slop](https://github.com/yetone/kill-ai-slop) for concrete examples and direct installation guidance. Firecracker uses its own fireworks identity and artwork. No affiliation is implied.
