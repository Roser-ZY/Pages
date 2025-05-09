---
title: "PCF"
author: "Roser"
date: 2025-05-08
image: "images/content/OpenGL.png"
draft: false
tags:
  - OpenGL
  - Lighting
---
PCF 全称为 Percentage-Closer Filtering，由于不好翻译，后面就使用简称 PCF。PCF 是一个术语，使用多种过滤函数来生成柔化阴影。

思路是对 Depth Map 进行多次采样，每次采样都选取稍微不同的纹理坐标。每次采样都检查当前是否在阴影中，所有的子结果最终进行组合并平均，从而得到柔化阴影。

一种比较简单的实现方法就是对某个采样点周围的纹素进行收集并取平均值。该方法会进行获得九个采样值并取平均。

> 这个过程类似卷积和抗锯齿？

除了上述实现外，还有很多策略可以用来实现 PCF。PCF 更多的是提供了一种思路。