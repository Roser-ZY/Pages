---
title: "generated.h"
author: "Roser"
date: 2025-04-23
image: "images/content/UE5.png"
draft: false
tags:
  - UE5
  - Cpp
  - Draft
---
UE5 的类总是需要将该头文件的 `include` 语句放在所有头文件的最后，否则会出现编译问题。

该头文件的作用是告知 Unreal Header Tool（UHT）当前头文件依赖[Reflection System](../Core/Reflection%20System.md)。