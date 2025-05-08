---
title: "List"
author: "Roser"
date: 2025-01-07
image: "images/content/CMake.png"
draft: false
tags:
  - CMake
  - Variable
---
List 是一个比较特殊的变量，在 CMake 中是一个字符串，每一个元素会用 `;` 分隔。

`set(mylist a b c d)` 会创建一个名为 `mylist` 的变量，值为 `"a;b;c;d"`。

可以通过 `list()` 对 List 变量进行相关操作。