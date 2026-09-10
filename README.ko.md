<p align="center">
  <img src="assets/hero.svg" width="960" alt="서로 다른 문서들이 하나의 불꽃을 바라보는 Firecracker 배너">
</p>

<h1 align="center">Firecracker</h1>
<p align="center"><strong>서로 다른 자리에서, 하나의 불꽃을 바라보다.</strong></p>
<p align="center">프로젝트가 바뀌어도, 문서가 바라보는 방향은 함께.</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.ko.md">한국어</a> · <a href="README.zh-CN.md">简体中文</a>
</p>

---

기획서는 **A+**를 말합니다. README는 여전히 **A**를 설명합니다. 운영 문서는 어느새 **B**를 전제로 합니다.

Firecracker는 Codex가 이런 불일치를 발견하고, 판단의 근거가 되는 결정을 추적하고, 뒤처진 문서를 고치도록 돕는 스킬입니다. 서로 다른 장소에서 같은 불꽃을 바라보듯, 각 문서의 역할을 살리면서 적용되는 프로젝트 방향을 맞춥니다.

[설치](#설치) · [검사 전후](#검사-전후) · [사용법](#사용법) · [한계](#한계)

## 설치

기본 스킬 설치기를 사용할 수 있는 Codex 대화창에 붙여넣으세요.

```text
$skill-installer https://github.com/Yangms30/firecracker 에서 Firecracker를 설치해줘.
SKILL.md는 저장소 루트에 있어. scripts/, references/, agents/, assets/도 함께 설치해줘.
```

<details>
<summary>직접 설치 · macOS / Linux</summary>

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/Yangms30/firecracker.git ~/.agents/skills/firecracker
```

아직 사용하지 않는 경로에 설치하세요. 이미 설치했다면 해당 설치본을 업데이트하세요. 한 프로젝트에서만 쓰려면 전체 폴더를 `<project>/.agents/skills/firecracker/`에 복사하세요.

`SKILL.md`, `scripts/`, `references/`, `agents/`, `assets/`를 함께 유지해야 합니다. 문서 목록 수집 스크립트에는 Python 3가 필요합니다. [Codex 공식 스킬 안내](https://learn.chatgpt.com/docs/build-skills)를 참고하세요.

</details>

설치 후 검사할 프로젝트를 열고 요청하세요.

```text
$firecracker 이 프로젝트 문서의 결정 충돌과 오래된 지침을 검사해줘.
파일을 수정하지 말고, 근거와 정리 후보, 실제 검사 범위를 보고해줘.
```

## 검사 전후

**설명을 위한 예시:** 초안 생성 전에 사용자 승인이 필요하도록 결정이 바뀌었습니다. 업로드 단계의 자료 전처리는 여전히 허용됩니다.

| 문서 | 검사 전 | 수정을 요청한 뒤 |
| --- | --- | --- |
| 승인된 기획서 | 승인 후에만 초안 생성 | 기준이 되는 결정으로 유지 |
| API 안내 | 업로드 즉시 초안 생성 시작 | 업로드는 자료 준비, 승인은 초안 생성 시작 |
| 운영 문서 | 업로드마다 초안 생성 재시도 | 승인된 생성 작업에 한해 재시도 |
| 과거 회의록 | 자동 생성 방식 제안 | 역사적 기록으로 보존 |
| 시각 디자인 가이드 | 글꼴과 간격 정의 | 유지; 승인 흐름을 추가할 필요 없음 |

**같은 방향이 같은 내용을 뜻하지는 않습니다.** 환경 차이, 미래 계획, 과거 기록은 서로 다른 내용을 담을 수 있습니다.

## 무엇을 검사하나요?

| 영역 | 확인할 수 있는 것 |
| --- | --- |
| 내용 충돌 | 같은 범위에서 양립할 수 없는 요구사항과 출처 |
| 변경 반영 누락 | 이전에 합의된 동작을 여전히 설명하는 문서 |
| 용어와 상태 | 바뀐 계약·명칭, 끊어진 참조, 완료된 것처럼 쓰인 제안 |
| 문서의 필요성 | 유지·수정·통합·보관·삭제 후보 제안 |
| AI의 열람 증거 | 제공한 로그에서 확인되는 열람·부분 열람·확인 불가 |
| 검사 범위 | 검토 완료·대기·부분 검토·차단·제외 파일과 탐색 경계 |

## 사용법

**검사하고 수정하기**

```text
$firecracker 프로젝트 문서를 검사하고 근거가 명확한 불일치를 수정해줘.
불필요한 문서는 삭제 후보로 추천만 하고, 실제로 삭제하지는 마.
```

**합의된 변경을 따라가기**

```text
$firecracker 초안 생성이 업로드 즉시 자동 생성에서 사용자 승인 후 생성으로 바뀌었어.
영향받는 문서를 업데이트하고, 합의된 목표와 실제 구현 상태를 구분해줘.
```

**과거 코딩 에이전트의 열람 확인하기**

```text
$firecracker 이 코딩 세션 로그로 문서별 열람 증거를 확인해줘.
각 문서가 지금도 프로젝트에 필요한지는 별도로 평가해줘.
```

별도의 CLI 하위 명령어가 아닌 자연어 요청 예시입니다. 영어·한국어·중국어로 요청할 수 있으며, 보고서는 요청한 언어로 작성하고 수정할 문서는 원래 언어를 유지합니다.

## 작동 방식

1. **문서 파악.** 후보 파일, 내용 해시, 제외 범위, 읽을 수 없는 자료를 확인합니다.
2. **결정 추적.** 주제·환경·릴리스·권위의 근거를 구분해 주장을 비교합니다.
3. **불일치 발견.** 원문을 확인하면서 모순과 변경 반영 누락을 찾습니다.
4. **수정과 재검사.** 요청받은 범위에서 근거가 있는 부분을 고치고 관련 문서를 다시 비교합니다.

보고서에는 각 문제의 근거, 적용되는 결정, 제안하거나 수행한 조치, 판단의 확실성이 연결됩니다. 정리 후보에는 대체 문서와 영향을 받을 참조도 설명합니다.

<details>
<summary>스킬 내부 구성 · 문서 목록 수집 스크립트</summary>

| 파일 | 역할 |
| --- | --- |
| [SKILL.md](SKILL.md) | 공통 검사·수정 지침 |
| [scripts/inventory.py](scripts/inventory.py) | 문서 후보 탐색과 내용 해시 |
| [references/review-guide.md](references/review-guide.md) | 근거·문제·검사 범위 기록 |
| [references/lifecycle-and-access.md](references/lifecycle-and-access.md) | 정리와 열람 증거 판단 기준 |
| [references/brand.md](references/brand.md) | 불꽃놀이 콘셉트와 표현 방식 |
| [agents/openai.yaml](agents/openai.yaml) | Codex 스킬 메타데이터 |

스킬 폴더에서 실행합니다.

```bash
python3 scripts/inventory.py /absolute/project/root > /tmp/docs-inventory.json
```

스크립트는 목록만 수집하며 의미 비교는 Codex가 수행합니다. 알려진 형식과 명시적으로 추가한 패턴을 탐색하고, 지정된 의존성·빌드 폴더를 제외하며 심볼릭 링크는 따라가지 않습니다. 특이한 형식은 별도 확인이 필요하고, PDF·Office 추출은 사용 가능한 도구에 따라 달라집니다.

</details>

## 한계

- 문서끼리 일치한다고 실제 구현까지 올바르다는 뜻은 아닙니다.
- 열람 기록은 이해나 준수를 증명하지 않습니다. 로그가 없으면 열람 여부는 확인 불가입니다.
- 오래됐거나, 링크가 없거나, 열람 기록이 없다는 이유만으로 삭제를 추천하지 않습니다.
- 기준이 되는 결정끼리 충돌하면 추가 근거나 결정이 나올 때까지 미해결로 남깁니다.
- 검사는 읽기 전용입니다. 수정 요청은 근거 있는 문서 수정을 허용하며, 삭제에는 명시적인 허가가 필요합니다.
- 읽을 수 없는 파일과 미검토 구간을 포함해 실제 검사 범위를 공개합니다.

## 언어와 디자인

[English](README.md) · [한국어](README.ko.md) · [简体中文](README.zh-CN.md)

세 README는 하나의 공통 스킬을 설명합니다. 실행 지침과 참조 파일은 영어로 관리하며, 언어별로 다른 검사 엔진을 만들지 않습니다. 번역을 수정할 때는 예시·설치 방법·한계도 함께 맞춰주세요.

구성 참고: [Ponytail](https://github.com/DietrichGebert/ponytail)의 명확한 브랜딩과 전후 비교, [Kill AI Slop](https://github.com/yetone/kill-ai-slop)의 구체적인 예시와 간결한 설치 안내. Firecracker는 자체 불꽃놀이 콘셉트와 그래픽을 사용하며, 두 프로젝트와 제휴 관계가 아닙니다.
