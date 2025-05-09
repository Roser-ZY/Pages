---
image: "images/content/OpenGL.png"
draft: false
title: Parallax Occlusion Mapping
author: Roser Han
date: 2025-04-15
tags:
  - OpenGL
  - Lighting
  - Texture
  - Review
---
Parallax Occlusion Mapping 在 [Steep Parallax Mapping](../Steep-Parallax-Mapping) 的基础上，对包含目标高度的两个层级（一个层级高度大于纹理高度，另一个层级高度小于纹理高度）进行线性插值，从而得到更平滑的视觉效果。

> 纹理偏移也会更接近真实值。

![](images/Parallax_Occlusion_Mapping示意图.png)

上图可知，该方法只是在 Steep Parallax Mapping 的基础上额外对高度进行了进行了线性插值后再计算纹理坐标。

```cpp
[...] // Steep parallax mapping.

vec2 prevTexCoords = currentTexCoords + deltaTexCoords;

// 下面保证了 afterDepth 和 before 都是正值
// 获取当前层与当前纹理高度的高度差
float afterDepth =  currentLayerDepth - currentDepthMapValue;
// 获取前一层与前一层纹理高度的高度差
float beforeDepth = texture(depthMap, prevTexCoords).r - currentLayerDepth + layerDepth;

// 线性插值
float weight = afterDepth / (afterDepth + beforeDepth);
vec2 finalTexCoords = prevTexCoords * weight + currentTexCoords * (1.0 - weight);

return finalTexCoords;
```

```
// 公式推导

x + (y - x) * i / (i + j) = target

x * i + x * j + y * i - x * i = target / (i + j)

x * j + y * i = target / (i + j)

target = x * j / (i + j) + y * i / (i + j)

```
