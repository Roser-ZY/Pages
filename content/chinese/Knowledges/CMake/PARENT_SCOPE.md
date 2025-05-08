---
title: "PARENT_SCOPE"
author: "Roser"
date: 2025-01-14
image: "images/content/CMake.png"
draft: false
tags:
  - CMake
---
在 [Scope](Scope.md) 中介绍过，Child Scope 中对 Calling Scope 的修改不会影响 Calling Scope。但是在某些情况下，需要将一些变量值回传给 Calling Scope，此时可以使用 `PARENT_SCOPE` 关键字。

`PARENT_SCOPE` 是 `set()` 的可选项，用于指定当前创建（修改）的变量作用域。

```cmake
set(myVar bar PARENT_SCOPE)
```

使用 `PARENT_SCOPE` 创建和修改的变量不会在 Child Scope 中感知到，可以看做是该命令不会影响 Child Scope 中的副本（并不会实时更新 Child Scope 的变量）。

一般来说，如果 Child Scope 需要回传某个变量，不建议在 Child Scope 中使用 Calling Scope 同名变量，更清晰的做法是定义一个本地版本来操作。

```cmake
set(localVar bar)
set(myVar ${localVar} PARENT_SCOPE)
```
