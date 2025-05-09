---
title: "Source 和 Binary 目录常量"
author: "Roser"
date: 2025-01-20
image: "images/content/CMake.png"
draft: false
tags:
  - CMake
  - Variable
---
使用 [add_subdirectory](../add_subdirectory) 之后，项目的编译结构可能会非常复杂，为了更方便的获取目录信息，CMake 提供了一些预定义的目录常量。

`CMAKE_SOURCE_DIR`
	 *source* 文件树的顶层目录，即顶层 `CMakeLists.txt` 所在目录。该变量的值不会变更。
`CMAKE_BINARY_DIR`
	*build* 文件树的顶层目录。该变量的值不会变更。
`CMAKE_CURRENT_SOURCE_DIR`
	当前 `CMakeLists.txt` 所在目录。该变量会在每次处理 `add_subdirectory` 文件时进行变更，并且在完成时还原。
`CMAKE_CURRENT_BINARY_DIR`
	对应 `CMakeLists.txt` 的 *build* 目录。该变量会在每次处理 `add_subdirectory` 文件时进行变更，并且在完成时还原。

其中 `CMAKE_CURRENT_SOURCE_DIR` 和 `CMAKE_CURRENT_BINARY_DIR` 在 [include](../include) 时不会变化，CMake 提供了额外的变量以供 `include` 使用。

`CMAKE_CURRENT_LIST_DIR`
	类似 `CMAKE_CURRENT_SOURCE_DIR`，但是不论 `include` 还是 `add_subdirectory` 都会变更该变量。该变量总为绝对路径。
`CMAKE_CURRENT_LIST_FILE`
	当前正在处理的文件名，总是绝对路径。
`CMAKE_CURRENT_LIST_LINE`
	给出当前正在处理的文件行号，一般用于调试 CMake 时使用。
