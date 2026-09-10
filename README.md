![Firecracker — Different perspectives. One shared spark.](assets/hero.svg)

# Firecracker 🎆

**서로 다른 자리에서, 하나의 불꽃을 바라보다.**

불꽃놀이가 시작되면 사람들은 서로 다른 자리에서 같은 불꽃을 바라봅니다. 프로젝트의 문서도 그렇습니다. 기획서는 목적을, 설계서는 구조를, 운영 문서는 실행을 이야기합니다. 서로 다른 역할을 유지하면서도, 현재 합의된 방향을 함께 바라봐야 합니다.

**Firecracker**는 그 방향을 밝혀주는 Codex 스킬입니다. 문서 사이의 모순과 변경 반영 누락을 찾아 근거가 명확한 부분을 고치고, 중복되거나 쓸모를 다한 문서는 정리 후보로 제안합니다.

> **Different perspectives. One shared spark.**
>
> Find the drift. Follow the evidence.

---

## ✨ What it illuminates

- Compares requirements, plans, architecture, README, agent instructions, API guides and runbooks by topic, scope and effective status.
- Repairs evidence-backed documentation drift when requested; an audit request remains read-only.
- Distinguishes accepted decisions, current implementation, future proposals and historical records.
- Recommends keep, update, merge, archive or delete-candidate actions with rationale and reference impact. Does not delete merely because a document is old or unlinked.
- Reports observed/partial/failed agent access from supplied traces. No trace means unknown usage, not proof the agent never read a document.
- Reports actual review coverage and unreadable or excluded material.

## 🚀 Light it up · Install

In Codex, ask the built-in skill installer to install this repository's root skill:

```text
$skill-installer Install the firecracker skill from https://github.com/Yangms30/firecracker. The SKILL.md is at the repository root; include scripts, references and agents metadata.
```

Repository: [Yangms30/firecracker](https://github.com/Yangms30/firecracker).

[Download ZIP](https://github.com/Yangms30/firecracker/archive/refs/heads/main.zip) to install manually.

For manual installation, download or clone this repository and place the entire directory at one of these locations:

- All projects: `~/.agents/skills/firecracker/`
- One project: `<project>/.agents/skills/firecracker/`

The final entrypoint must be `firecracker/SKILL.md`. Keep `scripts/`, `references/`, `agents/` and `assets/` with it. Python 3 is required for the inventory helper; semantic analysis is performed by Codex, not by the script.

Official reference: https://learn.chatgpt.com/docs/build-skills

## 🎇 Put it to work

Audit without edits:

```text
$firecracker 이 프로젝트 전체 문서가 현재 결정과 같은 방향을 따르는지 검사해줘. 파일을 수정하지 말고 충돌 근거와 검사 범위를 보고해줘.
```

Audit and repair:

```text
$firecracker 프로젝트 문서를 검사하고 근거가 명확한 불일치는 수정해줘. 불필요한 문서는 삭제 후보로 추천만 해줘.
```

Trace an accepted change:

```text
$firecracker 초안 생성이 '업로드 즉시 생성'에서 '사용자 승인 후 생성'으로 변경됐어. 영향받는 문서를 찾아 현재 동작과 목표 상태를 구분해서 업데이트해줘.
```

Inspect past agent access:

```text
$firecracker 제공한 코딩 세션 로그를 바탕으로 각 문서의 실제 열람 증거를 확인해줘. 문서의 현재 필요성은 별도로 평가해줘.
```

## 🔭 Inside Firecracker

- `SKILL.md`: audit, repair and verification workflow.
- `scripts/inventory.py`: deterministic candidate discovery and content hashes; no semantic or access inference.
- `references/review-guide.md`: evidence and coverage ledger.
- `references/lifecycle-and-access.md`: cleanup recommendations and access evidence rules.
- `agents/openai.yaml`: Codex skill metadata.
- `references/brand.md`: fireworks concept, palette and report presentation.
- `assets/hero.svg` and `assets/icon.svg`: portable brand graphics.

The helper can run independently:

```bash
python3 scripts/inventory.py /absolute/project/root > /tmp/docs-inventory.json
```

This creates an inventory only. Documents are initially pending until an agent reviews their contents and compares applicable claims. Known documentation formats and explicit include globs are discovered; unsupported formats need manual assessment. PDF/office extraction depends on tools available to the agent.

## What the light cannot prove

Document agreement does not prove implementation correctness. A file read does not prove comprehension or compliance. No incoming reference does not prove a document is unnecessary. An unresolved policy conflict is reported rather than settled by guessing. Cleanup recommendations are not deletion authorization.
