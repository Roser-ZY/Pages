---
title: "Scope"
author: "Roser"
date: 2025-01-14
image: "images/content/CMake.png"
draft: false
tags:
  - CMake
---
使用 [add_subdirectory](add_subdirectory.md) 后，会为 *subdirectory* 创建新的 Scope。主要有以下特性：
- Child Scope 可以使用 Calling Scope 的变量。
- Child Scope 定义的新变量不能被 Calling Scope 访问。
- Child Scope 中对变量的修改只会被局限于 Child Scope 本地，即使修改了 Calling Scope 的变量，也不会改变 Calling Scope 中该变量的值。被修改的变量就像是在 Child Scope 中新创建的变量一样。

可看做 Child Scope 操作的是 Calling Scope 的副本。