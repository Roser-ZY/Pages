---
title: "Eades 算法"
author: "Roser"
date: 2025-05-09
image: "images/content/Algorithm.png"
draft: false
tags:
  - Algorithm
  - Force-Directed
  - GraphLayout
---
1984 年 Eades 的算法实现了 30 个顶点的美观的 2D 图布局。

算法将每一个顶点之间的边更换成弹簧（Spring）来实现一个机械系统。顶点一开始位于初始布局处，并让弹簧强制将点移动到系统合适的位置。

在这个算法中，有两个可调整项：
1. 采用对数强度弹簧。
2. 让不相邻（即没有边）的点相互排斥，采用平方排斥力。
***
##### 对数强度弹簧

$$
c_1 \times log(d/c_2)
$$
其中 $d$ 为弹簧长度，$c_1$ 和 $c_2$ 为常数项。如果使用常数强度弹簧会使得顶点相聚较远时的力过强，而对数弹簧解决了这个问题。
##### 平方排斥力

$$
c_3 / d^2
$$
$c_3$ 是常数项，$d$ 为顶点之间的直线距离。
***
完整算法如下：

$$
\begin{array}{l}
algorithm\ SPRINT(G:graph); \\
place\ vertices\ of\ G\ in\ random\ locations; \\
repeat\ M\ times: \\
\quad calculate\ the\ force\ on\ each\ vertex; \\
\quad move\ the\ vertex\ c_4 \times(force\ on\ vertex) \\ 
draw\ graph.
\end{array}
$$
算法中，$c_1=2,c_2=1,c_3=1,c_4=0.1$ 是对大多数图都合适的常数项。几乎所有图在运行 100 次后都能够达到最小能量状态（即图趋于稳定），因此 $M=100$。

该算法计算吸引力的事件复杂度为 $O(|E|)$，计算顶点排斥力的时间复杂度为 $O(|V|^2)$。