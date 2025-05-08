---
image: "images/content/C++.png"
draft: false
title: 条款03：尽可能使用 const
author: Roser Han
date: 2025-04-14
tags:
  - Cpp
  - Review
  - EffectiveCpp
---
`const`  是非常强大的语言特性，它能在编译器层面实现约束，从而减少程序员编码过程引入问题的可能。

函数返回 `const` 值，可以避免使用函数的人对返回值进行了误操作。
### `const` 成员函数

C++ 中 `const` 比较经典的用途就是 `const` 成员函数。

有两个比较有名的概念：Bitwise Constness 和 Logical Constness。

- 前者认为只有成员函数不改变对象任何成员变量（`static` 除外）时，才可视为是 `const`。这也是 C++ 对常量性的定义。
- 后者认为 `const` 成员函数可以修改成员变量，只要使用者感知不到即可。

Bitwise 比较典型的反例是指针。

- 如果指针指向 this 之外的值，则在成员函数内部也可修改其指向的值。
- 如果指针指向 this 的成员，则将该指针作为出参或返回值时，外部可以对其指向的内容进行修改，此时虽然函数没有修改，但是仍然会有修改的风险。
### `const` 与 `non-const` 避免重复

应当在 `const` 通过类型转换调用 `non-const` 来减少重复代码，反之不行。因为在 `non-const` 函数中调用非 `const` 函数是有修改风险的。