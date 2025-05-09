---
title: "SpawnActor()"
author: "Roser"
date: 2025-04-17
image: "images/content/UE5.png"
draft: false
tags:
  - UE5
draft: true
---
- ? 必须在 `BeginPlay()` 之后调用，在世界中生成 Actor。不能在构造函数中调用，因此构造函数还没有生成世界。

C++ 类的构造函数在游戏开始前就已经创建好，UE5 引擎默认会提前构造好，以便在编辑器中能够看到。这就导致构造函数实际上并没有开始游戏，很多游戏时（运行时）状态是没有的。