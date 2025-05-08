---
title: "CMake 的作用"
author: "Roser"
date: 2024-12-30
image: "images/content/CMake.png"
draft: false
tags:
  - CMake
---
如果没有编译系统（例如 CMake），一个项目仅仅是一堆文件的集合。CMake 则是将这些文件通过**平台无关的**配置文件 `CMakeLists.txt` 组织起来，生成特定平台（*Platform*）构建工具（*Build Tools*）能够识别的[项目文件](生成项目文件.md)（Project Files）。

