---
title: "Linux 文件映射段"
author: "Roser"
date: 2025-04-03
image: "images/content/OS.png"
draft: false
tags:
  - OS
  - Review
draft: true
---
程序运行过程中还需要依赖动态链接库，这些动态链接库以 `.so` 文件的形式存放在磁盘中。它们也有自己对应的代码段、数据段、BSS段，也需要一起加载进内存。

还有用于内存文件映射的系统调用 `mmap`，会将文件与内存进行映射，则映射的这块内存也需要在虚拟地址空间中有一块区域存储。

上述所说的内存，就会被放在文件映射段。