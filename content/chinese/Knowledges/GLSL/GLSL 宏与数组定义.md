---
title: "GLSL 宏与数组定义"
author: "Roser"
date: 2025-05-09
image: "images/content/GLSL.png"
draft: false
tags:
  - GLSL
  - OpenGL
draft: true
---
GLSL 和 C 语言有很多相似之处，也可以使用预处理指令 `#define` 定义宏，并且可以以 C 语言风格创建数组。

```c
#define NR_POINT_LIGHTS 4
uniform PointLight pointLights[NR_POINT_LIGHTS];
```
