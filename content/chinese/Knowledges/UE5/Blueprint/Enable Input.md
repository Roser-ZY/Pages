---
title: "Enable Input"
author: "Roser"
date: 2025-05-09
image: "images/content/UE5.png"
draft: false
tags:
  - UE5
  - Blueprint
  - Todo
---
`Enable Input` 和 `Disable Input` 主要用于控制玩家输入的启用和停用，通常用于非默认玩家控制的 Actor，例如环境交互对象，特定 UI 控制等，使其能够获取玩家输入。

该节点不影响**默认拥有输入**的 Actor，仅用于**非玩家控制**的 Actor，仅限于目标 Actor，不影响其他 Actor。

通常与 [[Get Player Controller]] 配合使用。