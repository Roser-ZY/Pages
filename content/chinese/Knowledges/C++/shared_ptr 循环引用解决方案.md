---
title: "shared_ptr 循环引用解决方案"
author: "Roser"
date: 2025-04-10
image: "images/content/C++.png"
draft: false
tags:
  - Cpp
  - STL
  - Review
sr-due: 2025-06-16
sr-interval: 67
sr-ease: 290
---
[智能指针](../智能指针) `shared_ptr` 会出现循环引用问题，即两个类的互相作为成员，并封装在 `shared_ptr` 中，此时两个类如果都进行了实例化并相互引用，会导致 `shared_ptr` 对两个类对象的引用计数始终无法变为 0，从而一直保留内存，导致内存泄漏。

解决循环引用的方法是将其中一个共享指针改为 `weak_ptr`。

> 因为 `weak_ptr` 不会增加引用计数。