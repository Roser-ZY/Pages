---
image: "images/content/UE5.png"
draft: false
date: 2025-04-23
title: PROPERTY()
author: Roser Han
tags:
  - UE5
draft: true
---
`PROPERTY()` 的作用是：
- 将变量注册到 UE5 反射系统中（否则编辑器，GC，序列化，蓝图都无法处理）。
- 支持自动序列化和 GC 机制。
- 用于生成 `*.generated.cpp` 反射代码（UHT）。

PROPERTY() 中，`VisibleAnywhere` 和 `BlueprintReadOnly` 不冲突，他们作用在不同的维度。
- 前者控制编辑器可见性。
- 后者控制蓝图可读性。

如果只写 `VisibleAnywhere`，则在蓝图中可读写的（默认）。
如果只写 `BlueprintReadOnly`，则在编辑器中是不可见的（默认）。

使用 `PROPERTY()` 需要注意，成员的类型必须是能够被 UE5 [Reflection System](../../Core/Reflection-System) 识别的类型，有些类型无法被识别，因此不能用于反射系统，也就无法用 `PROPERTY()` 标记。