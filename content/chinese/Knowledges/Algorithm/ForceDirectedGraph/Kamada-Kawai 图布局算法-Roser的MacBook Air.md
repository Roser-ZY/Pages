---
title: "Kamada-Kawai 图布局算法-Roser的MacBook Air"
author: "Roser"
date: 2025-01-13
image: "images/content/Algorithm.png"
draft: false
tags:
  - Algorithm
  - Force-Directed
  - GraphLayout
---
Kamada 和 Kawai 从不同的思路考虑了图布局，将图的**拓扑距离**转化为**几何距离**，更直观地展示图的结构关系。简单来说，就是将图论中的任意两点间的最短路径长度（All-Pairs-Shortest-Path）转换为两顶点间的几何直线距离，核心目标是**让几何距离尽可能接近拓扑距离**，以便在视觉上反映图的结构特性。

该算法首先要计算顶点间的最短路径长度，保存到距离矩阵中。

> 最短路径长度的计算可以参考一些图算法，例如迪杰斯特拉算法等。

在几何空间中布局，需要设置一个理想的几何距离 $d_{ij}$，该值通常与拓扑距离 $d_{ij}^G$ 成正比：

$$
d_{ij}=K
$$

Newton-Raphson 算法通过二阶偏导进行更快速的收敛。

![](assets/Pasted%20image%2020250110143618.png)