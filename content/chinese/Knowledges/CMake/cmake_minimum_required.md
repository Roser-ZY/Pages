---
title: "cmake_minimum_required"
author: "Roser"
date: 2025-05-09
image: "images/content/CMake.png"
draft: false
tags:
  - CMake
---
```cmake
cmake_minimum_required(VERSION major.minor[.patch[.tweak]])
```

`cmake_minimum_required()` 是 `CMakeLists.txt` 中最重要且基础的命令，虽然它的名称似乎是指明最小版本号，但是实际上的含义是：“*Behave like CMake version X.Y.Z*”。即使系统安装了更新版本的 CMake，在解析该 `CMakeLists.txt` 时，依然会按照指定的版本号来进行相应的底层操作。

如果系统安装的 CMake 版本低于最小版本号（更老的版本），则会给出报错。

如果`CMakeLists.txt` 没有给出 `cmake_minimum_required()` 则会给出警告，所以该命令是必须提供的，并且放在第一行。