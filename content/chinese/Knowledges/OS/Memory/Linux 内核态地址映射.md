---
title: "Linux 内核态地址映射"
author: "Roser"
date: 2025-04-07
image: "images/content/OS.png"
draft: false
tags:
  - OS
  - Review
draft: true
---
在[内核空间](../Linux-系统虚拟内存空间分布)中，有一段内存是直接映射区（32 位系统是 896MB 大小内核空间低地址那部分空间），物理内存上直接映射区（是从 `0x0` 首地址开始的 896MB 大小的物理内存空间）是从虚拟地址的内核地址一比一映射的，因此内核空间这部分是共享的。

在这 896MB 空间的前 16MB 空间，称为 `ZONE_DMA`，用于 DMA 映射。