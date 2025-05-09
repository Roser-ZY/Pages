---
title: "Fruchterman 和 Reingold 算法改进"
author: "Roser"
date: 2025-05-09
image: "images/content/Algorithm.png"
draft: false
tags:
  - Algorithm
  - Force-Directed
  - GraphLayout
---
Fruchterman 和 Reingold 对 [Eades 算法](../Eades-算法) 进行了改进，他们添加了顶点均匀分布的计算，让图中的顶点视为“彼此之间具有吸引力和排斥力的原子、粒子或者天体。“

吸引力和排斥力计算方式为：

$$
f_a(d)=d^2/k,\ \ \ \ \ f_r(d)=-k^2/d
$$

其中 $d$ 为顶点之间的距离，$k$ 为两个顶点之间的最佳距离：

$$
k=C\sqrt{\frac{area}{number\ of\ vertices}}
$$

此外，该算法还引入了 Temperature （的概念）来控制布局变化过程中顶点的位移。它可以从初始值（比如画布宽度的十分之一开始，然后以逆线性方式衰减到 0。

Fruchterman 和 Reingold 建议使用网格变体（Grid Variant）进行复杂度优化，远距离顶点之间的排斥力被忽略。对于稀疏图，并且采用线性分布的顶点，这个方法计算排斥力时有接近 $O(|V|)$ 的时间复杂度。

#### 完整算法

$$
\begin{array}{l}
area := W * L; \text{ // W and L are the width and length of the frame} \\
G := (V, E); \text{ // the vertices are assigned random initial positions} \\
k := \sqrt{area/|V|}; \\
\\
\textbf{function}~f_a(x)~:=~\textbf{begin}~\textbf{return}~x^2 / k;~\textbf{end;} \\
\textbf{function}~f_r(x)~:=~\textbf{begin}~\textbf{return}~k^2 / x;~\textbf{end;} \\
\\
\textbf{for}~i := 1~\textbf{to}~iterations~\textbf{do}~\textbf{begin} \\
\quad \text{ // calculate repulsive forces} \\
\quad \textbf{for}~v~\textbf{in}~V~\textbf{do}~\textbf{begin} \\
\quad\quad \text{ // each vertex has two vectors: .position and .displacement} \\
\quad\quad v.displacement := 0; \\
\quad\quad \textbf{for}~u~\textbf{in}~V~\textbf{do} \\
\quad\quad\quad \textbf{if}~(u \neq v)~\textbf{then}~\textbf{begin} \\
\quad\quad\quad\quad \ //\ \delta\ is\ the\ difference\ vector\ between\ the\ positions\ of\ the\ two\ vertices \\
\quad\quad\quad\quad \delta := v.position - u.position; \\
\quad\quad\quad\quad v.displacement := v.displacement + (\delta / |\delta|) * f_r(|\delta|); \\
\quad\quad\quad \textbf{end} \\
\quad\quad \textbf{end} \\
\quad \textbf{end} \\
\\
\quad \text{ // calculate attractive forces} \\
\quad \textbf{for}~e~\textbf{in}~E~\textbf{do}~\textbf{begin} \\
\quad\quad \text{ // each edge is an ordered pair of vertices v and u} \\
\quad\quad \delta := e.v.position - e.u.position; \\
\quad\quad e.v.displacement := e.v.displacement - (\delta / |\delta|) * f_a(|\delta|); \\
\quad\quad e.u.displacement := e.u.displacement + (\delta / |\delta|) * f_a(|\delta|); \\
\quad \textbf{end} \\
\\
\quad \text{ // limit max displacement to temperature t and prevent from displacement outside frame} \\
\quad \textbf{for}~v~\textbf{in}~V~\textbf{do}~\textbf{begin} \\
\quad\quad v.position := v.position + (v.displacement / |v.displacement|) * \min(v.displacement, t); \\
\quad\quad v.position.x := \min(W/2, \max(-W/2, v.position.x)); \\
\quad\quad v.position.y := \min(L/2, \max(-L/2, v.position.y)); \\
\quad \textbf{end} \\
\\
\quad \text{ // reduce the temperature as the layout approaches a better configuration} \\
\quad t := cool(t); \\
\textbf{end}
\end{array}
$$

