---
title: "Tutte 的重心算法"
author: "Roser"
date: 2025-05-09
image: "images/content/Algorithm.png"
draft: false
tags:
  - Algorithm
  - Force-Directed
  - GraphLayout
---
The Barycentric Method 被认为是最初的力导向图算法。其核心思想是基于图的拓扑结构，通过几何和物理的力平衡来优化顶点布局。该算法非常适用于**顶点已经被分组（或层次化）的场景**，要求图必须为**三重连通平面图**（3-Connected Planar Graph）。

> 三重连通图可以在平面上绘制出没有边交叉（除了在公共端点）的图，并且每一个面都能够保证是凸多边形。

算法的输入通常为两类顶点（也可以有更多其他类别，根据具体图的布局可灵活设置）：固定顶点和自由顶点。固定顶点的位置在图中是固定的，通常在算法开始时设定，自由顶点则是要进行布局的点。

固定顶点应该不少于三个，并且固定顶点构成的多边形必须是凸多边形（Convex Polygon），这是因为该算法不计算没有相邻点固定顶点的作用是计算整体重心并稳定整体布局，如果不满足上述条件，则计算后的布局仍然是不稳定的。

> 如果不提供固定顶点，则整个图布局不稳定的，生成的图形可能会漂移或旋转。
> 凸多边形是为了保证所有自由顶点被限定在凸多边形内部，如果固定顶点构成凹多边形，则自由顶点可能会出现在图形之外，并且会导致布局不稳定。
> 
> 可以将固定顶点理解为图的边界，多边形则相当于边界线。凸多边形会绷紧，内部分布会更均匀，凹多边形会松弛，布局会不稳定。

该算法的输入为一个图 $G=(V,E)$，其中 $V=V_0 \cup V_1$ 划分为两个子集，$V_0$ 至少包含三个固定顶点，并且顶点形成的多边形为凸多边形，而 $V_1$ 则为自由顶点。

算法输出为每个顶点的位置 $p_v$ 。
$$
\begin{array}{l}
1.\ Place\ each\ fixed\ vertex\ u\in V_0,\ and\ each\ free\ vertex\ at\ the\ origin.\\
2. \textbf{repeat}\\
\quad \textbf{foreach}\ free\ vertex\ v\in V_1\ \textbf{do}\\
\quad\quad x_v=\frac{1}{degree(v)}\Sigma_{(u,v)\in E}\ x_u\\
\quad\quad y_v=\frac{1}{degree(v)}\Sigma_{(u,v)\in E}\ y_u\\
\quad \textbf{until}\ x_v\ and\ y_v\ converge\ for\ all\ free\ vertices\ v.
\end{array}
$$
其中 $degree(v)$ 为每个顶点的度，即与之相连的边的数量。最终的终止条件为顶点的变化趋于稳定，例如位移量小于某个阈值。