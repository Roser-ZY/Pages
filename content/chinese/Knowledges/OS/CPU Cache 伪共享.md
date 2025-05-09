---
title: "CPU Cache 伪共享"
author: "Roser"
date: 2025-05-09
image: "images/content/OS.png"
draft: false
tags:
  - OS
  - Concurrency
  - Review
sr-due: 2025-06-19
sr-interval: 55
sr-ease: 250
---
在 [CPU 缓存一致性](../CPU-缓存)问题中，采用 MESI 解决了写传播的效率问题和事务串行化。CPU Cache 伪共享也被 MESI 引入。

缓存的更新是按照 [Cache Line](../CPU-缓存) 读取到 Cache 的，MESI 针对的也是 Cache Line。假如有两个变量 A 和 B 在相同的 Cache Line 中，并且 A 和 B 分别在两个 CPU 核心中访问并修改。则此时，每个核心在修改各自不同的变量时，都会不断地标记 Cache Line 为 Invalid 并写入内存进行同步，但是实际上他们的修改并不影响彼此。这就是 Cache 伪共享（False Sharing）问题。

伪共享会大大降低 CPU 的并发性能。

目前伪共享的解决方案有两种，一种是将两个数据的多线程访问绑定到同一个 CPU 核心，另一种是将两个变量进行填充并让其分别位于两个不同的 Cache Line。