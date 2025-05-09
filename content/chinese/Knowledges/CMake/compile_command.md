---
title: "compile_command"
author: "Roser"
date: 2025-05-09
image: "images/content/CMake.png"
draft: false
tags:
  - CMake
---
`compile_command.json` 是 Clang 项目的一部分，最早由 LLVM 开发团队引入，以支持 Clang-based 工具的编译数据库功能。

由于它是 JSON 格式，相比 Makefile 和 VS Solution 更通用，因此逐渐成为编译数据库的标准格式，广泛用于各类 LSP 用于语法检查和智能补全等。

但是要注意，在 Visual Studio 17 2022 生成器和 MSVC 编译器下，不会生成 `compile_commands.json`，即使添加了对应的配置。需要修改为 `Ninja` 和 `Clang` 编译器才可以。