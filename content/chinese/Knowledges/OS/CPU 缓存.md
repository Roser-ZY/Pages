---
title: "CPU 缓存"
author: "Roser"
date: 2025-05-09
image: "images/content/OS.png"
draft: false
tags:
  - OS
  - Review
sr-due: 2025-06-04
sr-interval: 51
sr-ease: 290
---
CPU 中一共有三个缓存，分别为 L1，L2 和 L3。

L1 是最靠近 CPU 的缓存，其存储空间最小，速度最快。L1 Cache 分为指令缓存和数据缓存两部分，能够更快速的执行指令和获取数据。

L2 是比 L1 稍远的缓存，存储空间比 L1 大但比 L3 小，执行速度比 L1 慢但比 L2 快。L2 不区分指令和数据。

L1 和 L2 缓存是每个核独立的，每个 CPU 核心都有自己的 L1/L2 Cache。

L3 比 L2 远，在三个缓存执行速度最慢，存储空间最大。L3 Cache 不区分指令和数据，并且是多核共享的。

从内存读取数据到缓存时，是按照 Cache Line（缓存块） 一块块读取内存的。