---
title: "directory_iterator"
author: "Roser"
date: 2025-05-09
image: "images/content/C++.png"
draft: false
tags:
  - Cpp
  - STL
  - Review
draft: false
sr-due: 2025-05-25
sr-interval: 32
sr-ease: 270
---
[`std::filesystem::direcotry_iterator`](https://en.cppreference.com/w/cpp/filesystem/directory_iterator)

`directory_iterator` 是一个 *Legacy Input Iterator*，对一个目录内的 `directory_entry` 进行遍历（但不会递归访问子目录）。

遍历顺序是不确定的，但是每个 `directory_entry` 只会被访问一次，特殊路径例如 `.` 和 `..` 会被跳过。

如果 `directory_iterator` 报错，或者到达了越过最后一个 [`directory_entry`](../directory_entry)，它会等于**默认构造的迭代器（*Default Constructed Iterator*）**，也就是**结束迭代器（*End Iterator*）**。

> 两个 End Iterator 总是相等的，对 End Iterator 执行自增或解引用操作是未定义行为。

如果在迭代器遍历过程中在目录创建或删除了某个文件或目录，并不能保证在后续遍历能看到该变化。