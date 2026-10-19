# 凯尔希虚拟宠物

已创建并在 Pets 列表中验证，名称为“凯尔希”。当前尚未设为活动宠物，可在 Pets 中选择使用。

- 稳定 ID：pet_6ad5c8c8736c8191b73f81443ebca072
- 规格：v2，1536 × 2288 透明 PNG，73 帧，9 组基础动作与 16 个视线方向。
- 外观：依据用户提供的 kst.jpg 差分图，保留灰绿短发、猫耳、绿眼、粗黑轮廓与非对称腿带。
- 性格表现：严谨克制、观察敏锐、专注工作，问候时流露温柔与信任。

## 文件

- spritesheet.png：通过本地和 Pets 服务端预检的最终动画图集。
- all-states.gif / all-states.mp4：基础动作预览。
- look-loop.gif / look-directions.png：16 个视线方向的连续预览和标注图。
- idle-jump-idle.gif：待机—跳跃—落地过渡。
- state-previews/：每组动作的独立 GIF。
- contact-sheet.png / four-state-stills.png：图集概览和四个标注静帧。
- pet-record.json：稳定宠物 ID、规格与功能状态。
- 完整制作包另存为上级目录的 kaltsit-production.zip，包含源图、内置 image_gen 提示词、修订、脚本与实际 QA 报告。

## 验证

本地结构验证、最终质量检查、三位独立方向盲检以及 Pets 服务端预检均通过。跳跃最高离地 27 像素，落地与待机基线差为 0。部分相邻斜向视线变化较轻；方向盲检全部匹配。连续性工具提示的上缘透明空隙是两只猫耳之间的外部空间。

## 角色参考

- https://prts.wiki/w/凯尔希
- https://prts.wiki/w/凯尔希·思衡托
