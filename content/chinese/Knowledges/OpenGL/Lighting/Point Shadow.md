---
title: "Point Shadow"
author: "Roser"
date: 2025-04-15
image: "images/content/OpenGL.png"
draft: false
tags:
  - OpenGL
  - Lighting
  - Draft
  - Review
---
对于点光源和聚光灯来说，需要使用透视投影而不是正交投影。这类阴影映射称为点光源映射或全向阴影。

需要注意，与[Shadow Mapping](Shadow%20Mapping.md)不同，透视投影的深度值变化不是线性的。

对于点光源，我们需要对周围所有方向进行深度测试，并确认阴影。存储深度测试数据最佳的结构是[立方体贴图](../Advanced/立方体贴图.md)。