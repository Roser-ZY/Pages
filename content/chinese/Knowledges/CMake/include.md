---
title: "include"
author: "Roser"
date: 2025-01-20
image: "images/content/CMake.png"
draft: false
tags:
  - CMake
---
```cmake
include(fileName [OPTIONAL] [RESULT_VARIABLE myVar] [NO_POLICY_SCOPE])
include(module [OPTIONAL] [RESULT_VARIABLE myVar] [NO_POLICY_SCOPE])
```

第一个形式和 [add_subdirectory()](../add_subdirectory) 类似，但是有以下不同：
- `include()` 需要传入被读取的**文件**，而 `add_subdirectory()` 传入的是一个包含 `CMakeLists.txt` 的目录。传给 `include()` 的文件名通常为 `.cmake` 文件，但是实际上可以是任何文件。
- `include()` 不会引入新的[变量作用域](../Scope)。
- 两个命令都会默认引入新的 Policy Scope，但是 `include()` 可以通过 `NO_POLICY_SCOPE` 可选配置来告知 CMake 不引入新 Policy Scope，而 `add_subdirectory()` 没有这个可选配置。
- 处理 `include()` 时不会修改 [`CMAKE_CURRENT_SOURCE_DIR` 和 `CMAKE_CURRENT_BINARY_DIR`](../Source-和-Binary-目录常量)，而 `add_subdirectory()` 会修改。

第二个形式用于加载模块（*Module*），上述所有要点也都适用。

`include` 文件时，可能会在多处引用同一个文件，但是一般只需要引入一次即可。因此，类似 C++，可以通过定义变量（C++ 宏），或者在目标文件开头使用 `include_guard()`（C++ pragma once）避免引入多次。

```cmake
if(DEFINED cool_stuff_include_guard)
return()
endif()

set(cool_stuff_include_guard 1)
# ...
# 或者
include_guard()
```

