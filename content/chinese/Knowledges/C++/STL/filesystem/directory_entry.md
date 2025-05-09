---
title: "directory_entry"
author: "Roser"
date: 2025-04-23
image: "images/content/C++.png"
draft: false
tags:
  - Cpp
  - STL
  - Review
draft: true
sr-due: 2025-05-24
sr-interval: 31
sr-ease: 270
---
- `#include <filesystem>`
- [`std::filesystem::directory_entry`](https://en.cppreference.com/w/cpp/filesystem/directory_entry)

`directory_entry` 表示一个目录项。一个 `directory_entry` 对象记录一个 Path 作为成员，并且保存额外的文件属性（例如 Hard Link 数量，状态，Symlink 状态，文件大小，最后修改时间等）。

主要用于 [`directory_iterator`](../directory_iterator) 遍历，自带一些成员方法用于检查当前目录项的