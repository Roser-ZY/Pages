---
title: "Harel 和 Koren 的分层布局算法"
author: "Roser"
date: 2025-01-16
image: "images/content/Algorithm.png"
draft: false
tags:
  - Algorithm
  - Force-Directed
  - GraphLayout
---
Harel 和 Koren 提出了针对 Large Graph 的分层布局优化算法，超过 1000 顶点的图布局算法也能有比较可观的时间复杂度。该算法基于 [Kamada-Kawai 图布局算法](../Kamada-Kawai-图布局算法) 实现。

该算法的核心观点是考虑对图进行抽象，而不去考虑细节优化。先将一个抽象图绘制出来，产生一个粗略的布局，只展示图的概要结构，然后再对细节进行修正。

该算法需要有一个策略获取到图的抽象结构，该结构应该能包含该图最重要的特征。这个粗粒度表示（*Coarse-Scale Representation*）简化组合结构，但是要保留重要的的布局特征。后续的操作会细化这个粒度，并进行修正。

算法整体可以分为三步：
1. 对抽象结构进行细化调整。
2. 对不在第一步的节点进行粗粒度修正。
3. 对第二步的节点细粒度修正。

算法复杂度与 Kamada-Kawai 算法近似。

$$
\begin{array}{l}
\textbf{Layout}(G(V, E)) \\
\text{Goal: Find } L, \text{ a nice layout of } G \\

\textbf{Constants:} \\
\text{\% Rad [= 7] – determines radius of local neighborhoods} \\
\text{\% Iterations [= 4] – determines number of iterations in local beautification} \\
\text{\% Ratio [= 3] – ratio between number of vertices in two consecutive levels} \\
\text{\% MinSize [= 10] – size of the coarsest graph} \\

\textbf{Algorithm:} \\
\text{\% Compute the all-pairs shortest path length: } d_{uv} \\
\text{\% Set up a random layout } L \\
k \gets \text{MinSize} \\

\textbf{while } k \leq |V| \textbf{ do} \\
\quad \text{centers} \gets \text{K-Centers}(G(V, E), k) \\
\quad \text{radius} \gets \max_{v \in \text{centers}} \min_{u \in \text{centers}} \{d_{uv}\} + \text{Rad} \\
\quad \text{LocalLayout}(d_{centers \times centers}, L(\text{centers}), \text{radius, Iterations}) \\
\quad \textbf{for every } v \in V \textbf{ do} \\
\quad \quad L(v) \gets L(\text{center}(v)) + \text{rand} \\
\quad k \gets k \cdot \text{Ratio} \\

\textbf{return } L \\
 \\
\textbf{K-Centers}(G(V, E), k) \\
\text{\% Goal: Find a set } S \subseteq V \text{ of size } k, \text{ such that } \max_{v \in V} \min_{s \in S} \{d_{sv}\} \text{ is minimized.} \\
S \gets \{v\} \text{ for some arbitrary } v \in V \\
\textbf{for } i = 2 \text{ to } k \textbf{ do} \\
\quad \text{Find the vertex } u \text{ farthest away from } S \\
\quad \text{(i.e., such that } \min_{s \in S} \{d_{us}\} \geq \min_{s \in S} \{d_{ws}\}, \forall w \in V \text{)} \\
\quad S \gets S \cup \{u\} \\

\textbf{return } S \\
 \\
\textbf{LocalLayout}(d_{v \times v}, L, k, \text{Iterations}) \\
\text{\% Goal: Find a locally nice layout } L \text{ by beautifying } k\text{-neighborhoods.} \\
\textbf{for } i = 1 \text{ to } \text{Iterations} \ast |V| \textbf{ do} \\
\quad \text{\% Choose the vertex } v \text{ with the maximal } \Delta^k_v \\
\quad \text{\% Compute } \delta^k_v \text{ as in Kamada-Kawai} \\
\quad L(v) \gets L(v) + (\delta^k_v(x), \delta^k_v(y)) \\

\textbf{end} \\
\end{array}
$$