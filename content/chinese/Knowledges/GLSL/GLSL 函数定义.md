---
title: "GLSL 函数定义"
author: "Roser"
date: 2025-05-09
image: "images/content/GLSL.png"
draft: false
tags:
  - OpenGL
  - GLSL
draft: true
---
GLSL中的函数和C函数很相似，它有一个函数名、一个返回值类型，如果函数不是在 `main` 函数之前声明的，我们还必须在代码文件顶部声明一个原型。我们对每个光照类型都创建一个不同的函数：定向光、点光源和聚光。