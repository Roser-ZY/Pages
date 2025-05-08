---
title: "K-Center Problem"
author: "Roser"
date: 2025-01-15
image: "images/content/Algorithm.png"
draft: false
tags:
  - Algorithm
  - Graph
---
K-中心问题是指从图中找到一个点集 $S\subseteq V$，使得 $max_{v\in V}\  min_{s\in S}\ d_{sv}$ 最小。

这里的目标函数含义为：
- $min_{s\in S}\ d_{sv}$ 找到顶点 $v$ 在点集 $S$ 中的最近顶点 $s$。
- $max_{v\in V}$ 找到到最近点集 $S$ 的最近顶点 $s$ 距离最远的顶点 $v$。

可采用贪心算法求解。
$$
\begin{array}{l}
\textbf{K-Centers}(G(V, E), k) \\
\% \text{ Goal: Find a set } S \subseteq V \text{ of size } k, \text{ such that } \max_{v \in V} \min_{s \in S} \{ d_{sv} \} \text{ is minimized.} \\
S \leftarrow \{ v \} \text{ for some arbitrary } v \in V \\
\text{for } i = 2 \text{ to } k \text{ do} \\
\quad 1. \text{ Find the vertex } u \text{ farthest away from } S \\
\quad \quad \text{(i.e., such that } \min_{s \in S} \{ d_{us} \} \geq \min_{s \in S} \{ d_{ws} \}, \, \forall w \in V \text{)} \\
\quad 2. S \leftarrow S \cup \{ u \} \\
\text{return } S
\end{array}
$$
