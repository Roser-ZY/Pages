---
title: "Animation Blueprint 与 Animation Montage 的关系与区别"
author: "Roser"
date: 2025-04-27
image: "images/content/UE5.png"
draft: false
tags:
  - UE5
draft: true
---
Animation Blueprint 通常用来做一些持续的状态动画，例如 Idle，Walk 和 Run 等。Animation Blueprint 不能在普通蓝图中访问并操作。

[Animation Montage](../Animation-Montage) 通常用来做一些一次性动画，例如攻击，施法等。Animtaion Montage 能够在普通蓝图中访问并操作，也可以在 Animation Blueprint 中使用。

如果一些动画希望能通过蓝图控制，可以创建为 Animation Montage 实现。

在 C++ 中，本质上这两个都可以实现动画播放。
- Animation Blueprint 可以通过 `NativeUpdateAnimation()` 不断读取一些状态来控制播放。
- Animation Montage 则使用和蓝图一样的方式进行控制。
***
使用 Animation Blueprint 本质上是使用状态机，但是状态机有很多缺点，一个是维护困难，变化复杂。另一个就是对于一些特殊状态，加入到状态机的难度可能会很大。这种情况下，使用 Animation Montage 会更好。

- ? 想要播放 Animation Montage，必须在 Animation Blueprint 中添加插槽，否则不会播放动画。他们二者实际上相辅相成的。
