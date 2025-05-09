---
title: "Kamada-Kawai 图布局算法"
author: "Roser"
date: 2025-05-09
image: "images/content/Algorithm.png"
draft: false
tags:
  - Algorithm
  - Force-Directed
  - GraphLayout
---
Kamada 和 Kawai 提出了与 [Fruchterman 和 Reingold 算法改进](../Fruchterman-和-Reingold-算法改进) 和 [Tutte 的重心算法](../Tutte-的重心算法) 专注于几何布局不同的算法思路，将图的**拓扑距离**转化为**几何距离**，更直观地展示图的结构关系。简单来说，就是将图论中的任意两点间的最短路径长度（All-Pairs-Shortest-Path）转换为两顶点间的几何直线距离，核心目标是**让几何距离尽可能接近拓扑距离**，以便在视觉上反映图的结构特性。

该算法首先要计算顶点间的最短路径长度，保存到距离矩阵中。

> 最短路径长度的计算可以参考一些图算法，例如弗洛伊德算法等。

在几何空间中布局，需要设置一个理想的几何距离 $l_{i,j}$，该值通常与拓扑距离 $d_{i,j}$ 成正比：

$$
l_{i,j}=L·d_{i,j}
$$

其中 $L$ 是比例因子，是一个常数，Kmada 和 Kawai 推荐将该比例因子设置为 $L=L_0 / max_{i<j}d_{i,j}$，其中 $L_0$ 为图区域某一个边的长度，而 $max_{i<j}d_{i,j}$ 为图的最大拓扑距离。

两个顶点之间的弹簧牵引力为：

$$
k_{i,j}=K/d_{i,j}^2
$$

其中 $K$ 为一个常数。将该图的几何绘制问题视为在 2D 欧几里得空间放置 $|V|=n$ 个粒子 $p_1,p_2,...,p_n$ 问题，可以得到如下能量方程：

$$
E=\Sigma_{i=1}^{n-1}\Sigma_{j=i+1}^n \frac{1}{2}k_{i,j}(|P_i-P_j|-l_{i,j})^2
$$

其中 $P_i$ 表示粒子 $p_i$ 的位置向量。上述能量方程为图中所有弹簧的弹性势能计算方程的总和。

由于位置向量可以表示为坐标 $x_i$ 和 $y_i$，因此上述方程可以转换为：

$$
E = \sum_{i=1}^{n-1} \sum_{j=i+1}^{n} \frac{1}{2} k_{i,j} \left( (x_i - x_j)^2 + (y_i - y_j)^2 + l_{i,j}^2 - 2 l_{i,j} \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2} \right)

$$

想让系统趋于稳定，实际是让上述能量方程在每一个粒子的位置的偏导数都等于 $0$，则需要解决 $2n$ 个联立非线性方程。

Kmada 和 Kawai 提出了每次只计算一个偏差能量最大的粒子 $p_m$，并将 $E$ 视为只与 $x_m$ 和 $y_m$ 相关的方程，因此可以通过 Newton-Raphson 算法做二阶偏导进行更快速的收敛，以计算处偏差能量（$\Delta_m$）最大的粒子并对其进行布局调整：

$$
\Delta_m = \sqrt{\left( \frac{\partial E}{\partial x_m} \right)^2 + \left( \frac{\partial E}{\partial y_m} \right)^2}.

$$

该算法的复杂度是很高的，除了需要 $O(|V|^3)$ 的时间复杂度和 $O(|V|^2)$ 的空间复杂度来计算并存储任意顶点的最短路径，还需要不断计算偏导数并计算能量值。

关于 Newton-Raphson 算法可以参考下图，具体算法需要再去看下高等数学（可能）：

![](images/Newton-Raphson算法.png)

完整算法如下：

$$
\begin{array}{l}
\textbf{while} \, (\max_i \Delta_i > \epsilon) \\
\quad \text{let} \, p_m \, \text{be the particle satisfying} \, \Delta_m = \max \Delta_i; \\
\quad \textbf{while} \, (\Delta_m > \epsilon) \\
\quad \quad \text{compute} \, \delta x \, \text{and} \, \delta y \, \text{by solving the following system of equations:} \\
\quad \quad 
\left\{
\begin{array}{l}
\frac{\partial^2 E}{\partial x_m^2} (x_m^{(t)}, y_m^{(t)}) \delta x + 
\frac{\partial^2 E}{\partial x_m \partial y_m} (x_m^{(t)}, y_m^{(t)}) \delta y = 
- \frac{\partial E}{\partial x_m} (x_m^{(t)}, y_m^{(t)}) \\[8pt]
\frac{\partial^2 E}{\partial y_m \partial x_m} (x_m^{(t)}, y_m^{(t)}) \delta x + 
\frac{\partial^2 E}{\partial y_m^2} (x_m^{(t)}, y_m^{(t)}) \delta y = 
- \frac{\partial E}{\partial y_m} (x_m^{(t)}, y_m^{(t)})
\end{array}
\right. \\
\quad \quad x_m := x_m + \delta x; \\
\quad \quad y_m := y_m + \delta y;
\end{array}

$$
