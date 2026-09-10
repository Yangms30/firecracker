<p align="center">
  <img src="assets/hero.svg" width="960" alt="Firecracker：不同位置的文档共同望向一束烟花">
</p>

<h1 align="center">Firecracker</h1>
<p align="center"><strong>身处不同位置，共望同一束烟花。</strong></p>
<p align="center">让项目中的文档随着项目演进，始终朝向共同的目标。</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.ko.md">한국어</a> · <a href="README.zh-CN.md">简体中文</a>
</p>

---

规格说明已经变成 **A+**，README 仍然描述 **A**，运维手册却默认按照 **B** 执行。

Firecracker 帮助 Codex 发现这些分歧，追溯相关决策，并修正落后的文档。就像人们从不同位置观看同一束烟花，每份文档保留自己的视角，同时遵循适用于其范围的项目方向。

[安装](#安装) · [前后对比](#前后对比) · [使用方法](#使用方法) · [局限](#局限)

## 安装

在可使用内置技能安装器的 Codex 对话中粘贴：

```text
$skill-installer 从 https://github.com/Yangms30/firecracker 安装 Firecracker。
SKILL.md 位于仓库根目录。请同时安装 scripts/、references/、agents/ 和 assets/。
```

<details>
<summary>手动安装 · macOS / Linux</summary>

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/Yangms30/firecracker.git ~/.agents/skills/firecracker
```

请使用尚未占用的目标路径。如果已经安装，请更新现有安装。若仅用于一个项目，将完整文件夹复制到 `<project>/.agents/skills/firecracker/`。

请将 `SKILL.md`、`scripts/`、`references/`、`agents/` 和 `assets/` 保留在一起。文档清单脚本需要 Python 3。参见 [Codex 官方技能指南](https://learn.chatgpt.com/docs/build-skills)。

</details>

安装后，打开需要检查的项目并输入：

```text
$firecracker 检查这个项目的文档，找出相互冲突的决策和过时的说明。
不要修改文件。请报告依据、清理候选项和实际检查范围。
```

## 前后对比

**示例场景：** 已确认的决策要求生成草稿前取得用户批准。上传时仍可进行资料预处理。

| 文档 | 检查前 | 获准修正后 |
| --- | --- | --- |
| 已批准的规格说明 | 仅在批准后生成草稿 | 保留，作为决策依据 |
| API 指南 | 上传后立即开始生成草稿 | 上传用于准备资料；批准后开始生成 |
| 运维手册 | 每次上传后重试草稿生成 | 仅重试已批准的生成任务 |
| 旧会议记录 | 提议自动生成草稿 | 作为历史记录保留 |
| 视觉设计指南 | 字体与间距规范 | 保留；无需加入审批流程 |

**方向一致不意味着内容相同。** 不同环境、未来计划和历史记录可以合理地包含不同表述。

## 检查内容

| 领域 | 检查结果 |
| --- | --- |
| 内容冲突 | 同一范围内不兼容的要求及其来源位置 |
| 变更遗漏 | 仍在描述先前已确认行为的文档 |
| 术语与状态 | 已更名的接口约定、失效引用、被写成已完成的提案 |
| 文档生命周期 | 保留、更新、合并、归档或列为删除候选项 |
| AI 阅读证据 | 根据提供的日志区分已观察到的阅读、部分阅读和未知状态 |
| 检查覆盖范围 | 已审查、待审查、部分审查、受阻、排除的文件及扫描边界 |

## 使用方法

**检查并修正**

```text
$firecracker 检查项目文档，修正有明确依据的不一致之处。
对不再需要的文档仅提出删除建议，不要实际删除。
```

**追踪已确认的变更**

```text
$firecracker 草稿生成已从上传后自动触发改为用户批准后触发。
更新受影响的文档，并区分已确认的目标与实际实现状态。
```

**检查先前编码代理的阅读记录**

```text
$firecracker 根据这些编码会话日志，评估各份文档的阅读证据。
另外评估每份文档目前是否仍对项目有用。
```

以上是自然语言请求，不是额外的 CLI 子命令。可以用英语、韩语或中文提出请求；报告使用请求者的语言，修改文档时保留原文语言。

## 工作方式

1. **梳理文档。** 发现候选文件、内容哈希、排除项和无法读取的材料。
2. **追溯决策。** 按主题、环境、版本和权威依据比较文档中的主张。
3. **发现偏差。** 回到原文，核实矛盾与变更遗漏。
4. **修正并复查。** 在请求范围内进行有据可依的修改，再次比较相关文档。

报告将每个问题与证据、适用决策、建议或已执行的操作以及判断的确定程度关联起来。清理建议还会说明替代文档和可能受影响的引用。

<details>
<summary>技能内部结构 · 文档清单脚本</summary>

| 文件 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md) | 共用的检查与修正指令 |
| [scripts/inventory.py](scripts/inventory.py) | 发现候选文件并计算内容哈希 |
| [references/review-guide.md](references/review-guide.md) | 记录证据、问题与覆盖范围 |
| [references/lifecycle-and-access.md](references/lifecycle-and-access.md) | 清理建议与阅读证据规则 |
| [references/brand.md](references/brand.md) | 烟花主题与呈现规范 |
| [agents/openai.yaml](agents/openai.yaml) | Codex 技能元数据 |

在技能目录中运行：

```bash
python3 scripts/inventory.py /absolute/project/root > /tmp/docs-inventory.json
```

脚本仅生成候选清单，语义审查由 Codex 完成。扫描器识别已知格式及显式指定的匹配模式，跳过指定的依赖与构建目录，不跟随符号链接。特殊格式需要另外检查；PDF 和 Office 内容提取取决于可用工具。

</details>

## 局限

- 文档彼此一致，并不证明实现正确。
- 阅读事件不能证明理解或遵守了内容。没有日志时，阅读状态为未知。
- 仅凭文档陈旧、缺少链接或未观察到阅读记录，不能建议删除。
- 权威决策之间的冲突会保留为未解决项，直到有新的证据或明确决策。
- 审查为只读操作。修正请求允许有依据的文档修改；删除需要明确授权。
- 如实报告实际覆盖范围，包括无法读取的文件和未审查的部分。

## 语言与设计

[English](README.md) · [한국어](README.ko.md) · [简体中文](README.zh-CN.md)

三份 README 描述同一个技能。执行指令与参考文件以英语维护，不提供按语言分开的检查引擎。更新翻译时，请同步示例、安装步骤与局限说明。

呈现方式参考：[Ponytail](https://github.com/DietrichGebert/ponytail) 的清晰品牌表达与前后对比，以及 [Kill AI Slop](https://github.com/yetone/kill-ai-slop) 的具体示例和直接的安装说明。Firecracker 使用自己的烟花主题与图形，与这两个项目没有关联关系。
