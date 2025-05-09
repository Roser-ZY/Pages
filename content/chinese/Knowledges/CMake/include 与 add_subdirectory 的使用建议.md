---
title: "include 与 add_subdirectory 的使用建议"
author: "Roser"
date: 2025-01-20
image: "images/content/CMake.png"
draft: false
tags:
  - CMake
  - RecommendedPractice
---
一般使用时，[add_subdirectory](../add_subdirectory) 要比 [include](../include) 更加灵活方便，在引入模块时使用 `include` 则更合理（`add_subdirectory` 并不支持引入模块）。如果都可用的情况下，使用 `add_subdirectory`。

另外，建议使用 `CMAKE_CURRENT_LIST_DIR` 代替 `CMAKE_CURERNT_SOURCE_DIR`，因为前者不会受引入方式的影响。