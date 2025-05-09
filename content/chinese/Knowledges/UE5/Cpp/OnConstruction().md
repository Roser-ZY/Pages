---
title: "OnConstruction()"
author: "Roser"
date: 2025-05-09
image: "images/content/UE5.png"
draft: false
tags:
  - UE5
draft: true
---
当 Actor 被放置（编辑时）或者生成时回调。

一些希望在编辑时能在 UE5 中看到并且编辑的内容可以在此处重写。

但是该函数内的逻辑不会在运行游戏时调用，只是用于辅助编辑时可视化编辑等，这些编辑后的结果会保存在该 Actor 的属性中，后续 BeginPlay 中会保留编辑的属性。因此 BeginPlay 时需要重新写一遍逻辑。

[建议](https://isaratech.com/ue4-be-careful-with-the-construction-script/)

谨慎使用该函数。