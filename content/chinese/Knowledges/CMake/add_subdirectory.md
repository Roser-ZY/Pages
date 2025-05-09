---
title: "add_subdirectory"
author: "Roser"
date: 2025-05-09
image: "images/content/CMake.png"
draft: false
tags:
  - CMake
---
```cmake
add_subdirectory(sourceDir [ binaryDir ] [ EXCLUDE_FROM_ALL ])
```

`sourceDir` 可以是绝对路径或相对路径，并且不一定是当前项目的子目录（可以是其他位置的目录）。

如果是当前项目的子目录，一般使用相对路径，此时 `binaryDir` 是可选项，CMake 会自动在 build 目录下创建与 `sourceDir` 同名的编译目录。

**如果使用绝对路径，或者 `sourceDir` 不是当前项目的子目录，则必须指定 `binaryDir`，因为 CMake 无法通过相对路径来自动处理**。

`EXCLUDE_FROM_ALL` 和 [add_library](../add_library) 类似，但是在一些编译器上会导致问题，不建议在该命令使用，而是在 `add_library` 和 `add_executable` 上控制。