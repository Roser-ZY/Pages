---
title: "vector 元素使用指针访问"
author: "Roser"
date: 2025-05-09
image: "images/content/C++.png"
draft: false
tags:
  - Cpp
  - Pointer
  - STL
---
`std::vector` 不为空时，可以通过 `&vector[0]` 获取 `std::vector` 底层数组指针，并后续可使用该指针偏移访问元素。因为 `std::vector` 底层是连续分布的。

要注意避免数组越界访问和内存重新分配行为。

自 C++11 起，建议使用 `std::vector::data()` 获取底层数组指针，更简洁且安全。