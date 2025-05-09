---
title: "PBR 是什么"
author: "Roser"
date: 2025-05-09
image: "images/content/OpenGL.png"
draft: false
tags:
  - OpenGL
  - PBR
  - Review
draft: true
---
PBR 全称为 Physically Based Rendering，即基于物理的渲染，是一系列渲染技术的集合，或多或少基于与物理世界相同的理论。

PBR 旨在按照符合物理规律的方式模拟光线，与[风式光照模型](../../Lighting/风式光照模型)和 Blinn-Phong 模型相比，PBR 实现的光照会更加真实。而且不仅仅是看上去更好，PBR 更接近现实物理规律。我们可以使用一些物理参数来定义表面材质，而不是让程序员去调整各种数值以实现光照效果。

PBR 最大的好处就是通过表面材质实现的光照不会受光照条件的影响，这是 non-PBR 渲染管线无法做到的。

PBR 只是现实物理规律的近似（基于一些物理定律），因此才称之为 Physically *Based* Shading 而不是 Physical Shading。PBR 必须满足以下三个条件：

- 基于微平面的表面模型（Be based on the microfacet surface model）。
- 能量守恒（Be energy conserving）。
- 应用基于物理的 BRDF（Use a physically based BRDF）。