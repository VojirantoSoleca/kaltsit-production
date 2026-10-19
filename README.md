# 凯尔希虚拟宠物 · Kal'tsit

凯尔希 Q 版动画宠物的素材与制作归档，包含最终透明动画图集、动作预览、生成提示词、逐帧素材、检查报告和辅助脚本。

![基础动作预览](deliverables/all-states.gif)

## 最终素材

- [透明动画图集](deliverables/spritesheet.png)：1536 × 2288 PNG，73 帧，9 组基础动作、16 个视线方向。
- [视线方向预览](deliverables/look-loop.gif)
- [待机与跳跃过渡](deliverables/idle-jump-idle.gif)
- [动作概览](deliverables/contact-sheet.png)
- [交付说明](deliverables/README.md)

## 目录

| 目录 | 内容 |
| --- | --- |
| `deliverables/` | 最终图集、GIF / MP4 预览与交付记录 |
| `production/references/` | 形象参考素材 |
| `production/prompts/` | 图片生成与修订提示词 |
| `production/decoded/` | 生成结果与中间素材 |
| `production/final/` | 最终图集及结构验证报告 |
| `production/qa/` | 分帧、方向、连续性等检查记录 |
| `helpers/` | 帧对齐与预览生成的 Python 辅助脚本 |

## 使用

直接下载 `deliverables/` 中的文件即可查看素材。本仓库是制作素材归档，不包含独立运行的桌面宠物应用。

辅助脚本需要 Python 和 Pillow。以下命令从仓库根目录生成本地预览：

```sh
python -m pip install Pillow
python helpers/render_review_assets.py --atlas deliverables/spritesheet.png --output work/previews
```

如需生成 MP4，可追加 `--ffmpeg` 参数并指定本机 FFmpeg 可执行文件路径。

## 制作记录说明

制作记录中的宠物 ID、启用状态和验证结果是原制作会话的历史记录。下载本仓库不会自动将宠物导入账号。原记录中的本机绝对路径已在本发布副本中改为仓库相对路径。

原需求中的日文语音未接入；仓库不包含语音播放功能。完整设计记录见 [request-brief.md](production/request-brief.md)。
