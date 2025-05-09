---
title: "istream 常用函数介绍"
author: "Roser"
date: 2025-05-09
image: "images/content/C++.png"
draft: false
tags:
  - Cpp
  - IO
draft: true
---
[TOC]

# `istream& read (char* s, streamsize n);`

该函数尝试读取 n 个字符到 s，如果读取数量不足 n，则会设置 `eofbig` 和 `failbit`。

当数量不足 n 时，可以借助[`streamsize gcount() const;`](istream%20常用函数介绍.md#`streamsize%20gcount()%20const;`) 获取实际读取的字节数量。
# `streamsize gcount() const;`

获取上一次**非格式化读取操作**提取的字符数量。