---
title: "ChildActorComponent"
author: "Roser"
date: 2025-04-18
image: "images/content/UE5.png"
draft: false
tags:
  - UE5
draft: true
---
### 与 Attach Actor 并用数组保存的区别？

最初做飞行棋盘时，直接用了一个 Actor 数组作为 Property，并期望以这种方式来管理棋盘格子，但是实际上这种方法非常错误。

首先 Actor 当时并没有 Attach 到棋盘类，导致 Spawn 的格子 Actor 是乱的，而且这种方式，即使 Attach，格子 Actor 也是独立的，它们的生命周期不会跟随棋盘 Board Actor。

正确方式应该是让棋盘格子作为 Board Actor 的组件。组件的生命周期是跟随父 Actor 的，父 Actor 销毁时，组件内的子 Actor 也会销毁。
***
