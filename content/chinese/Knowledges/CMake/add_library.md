---
title: "add_library"
author: "Roser"
date: 2025-01-14
image: "images/content/CMake.png"
draft: false
tags:
  - CMake
  - Linking
---
```cmake
add_library(targetName [STATIC | SHARED | MODULE]
[EXCLUDE_FROM_ALL]
source1 [source2 ...]
)
```

上述 STATIC，SHARED 和 MODULE 分别对应三种类型的库。
- STATIC
	生成静态库，在 Windows 上生成 `.lib` 文件，在 Unix-Like 平台上生成 `.a` 文件。

- SHARED
	生成动态库，在 Windows 上生成 `.dll` 文件（会同时生成 `.lib` 文件，该文件与静态库不同，主要用于导入库），在 Apple 平台生成 `.dylib` 文件，在其他 Unix-Like 平台生成 `.so` 文件。

- MODULE
	生成类似动态库的内容，但主要用于运行时加载，而并非链接到某个库或可执行文件。
	这类内容通常为插件或者可选组件，可以让用户选择是否加载。
	在 Windows 上这类动态库只生成 `.dll`，不会生成 `.lib`。

其中可选项 `EXCLUDE_FROM_ALL` 表示在编译 ALL Target 时（比如 VS 中对 ALL 生成解决方案），是否包含该链接库，如果设置该选项，则只有被其他 ALL Target 依赖，或者显式选择该 Target 编译时，才会参与编译。