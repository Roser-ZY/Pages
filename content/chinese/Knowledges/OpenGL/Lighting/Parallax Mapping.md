---
image: "images/content/OpenGL.png"
draft: false
tags:
  - OpenGL
  - Texture
  - Lighting
  - Review
title: Parallax Mapping
author: Roser Han
date: 2025-04-15
---
在现实世界中，我们观察一个物体时，会出现[视差](https://zh.wikipedia.org/wiki/%E8%A7%86%E5%B7%AE)，即在两个不同位置观察相同物体时，物体在视野中会产生位置变化。视差映射（Parallax Mapping）的名字由此而来。

当物体凹凸不平时，我们能够在物体自身看到视差。在图形学中，可以通过视差贴图来产生更真实的物体表面效果，这种效果与[Normal Texture](Normal%20Texture.md)不同。法线贴图是对光线角度进行处理，而视差贴图是对观察者的视线进行处理（模拟）。

> 后续会使用纹素术语，在某种程度上可以近似理解为片段，但本质要有所区分。

对于视差贴图，贴图每一个纹素代表一个高度。如果不做处理（即当作平面），进行片段着色器处理时，视线看向的是片段 A，但如果加上高度，理应看到的是 B，而 B 对应的应当是 B 垂直于纹理表面的纹素。我们想要更真实的物体表现，就需要找到 B 及其对应的纹素。
![](images/视差贴图简化示意图.png)
但是实际应用中，通过视差贴图精准找到 B 是很困难的，因此一般的视差贴图处理都会通过一些方法寻找**近似值**来**模拟**真正看到的纹素。模拟就会有偏差，但是这种偏差在实际应用中的影响是很小的。

如下图所示，可以通过向量 $P$ 到纹理表面的投影来获取近似的高度 $H(P)$。此处向量 $P$ 的方向与视线方向相同，长度与片段（纹素）A 处的纹理值（高度）$H(A)$ 相同。
![](images/视差贴图近似处理示意图（上方）.png)
这种近似方法在大部分情况下都表现良好，但是也是非常粗略的模拟，如果高度变化比较剧烈，会得到偏差较大的向量 $P$ 导致效果不真实。

![](images/视差贴图错误近似.png)

计算视差贴图时，需要在[切向空间](../../Graphics/切向空间.md)内处理（后续介绍均在切向空间下），视差贴图的高度在 $[0.1]$，，通常视差贴图的值会选择前面示意图的反向（即 $1 - Height$），如下图所示：

![](images/视差贴图计算.png)

> 这种方式**据说**要比前面的方法处理起来更合理。
> 可以直接对视差贴图通过图像工具“反向”，或者在片段着色器中手动计算。
> 本例是贴图本身已处理。

此时向量 $P$ 的方向是由纹素 A 处的向量 $A$ 减去向量 $V$ 得到，方向与 $V$  相反。我们最终要做的就是计算出实际（模拟）的纹理坐标偏移量（即 $P$ 投影到纹理平面的纹理坐标到 A 处的偏移量），然后使用偏移后的纹理坐标计算。

```cpp
#version 330 core
out vec4 FragColor;

in VS_OUT {
    vec3 FragPos;            // 世界空间下的片段位置
    vec2 TexCoords;          // 纹理坐标
    vec3 TangentLightPos;    // 切向空间下的光线向量
    vec3 TangentViewPos;     // 切向空间下的视线向量
    vec3 TangentFragPos;     // 切向空间下的片段位置
} fs_in;

uniform sampler2D diffuseMap;
uniform sampler2D normalMap;
uniform sampler2D depthMap;

uniform float height_scale;  // 高度缩放量

// 视差贴图计算实际（模拟）纹理坐标
vec2 ParallaxMapping(vec2 texCoords, vec3 viewDir);

void main()
{
    // Offset texture coordinates with Parallax Mapping
    // 计算片段到观察者（摄像机）的方向向量，即向量 V
    vec3 viewDir = normalize(fs_in.TangentViewPos - fs_in.TangentFragPos);
    vec2 texCoords = ParallaxMapping(fs_in.TexCoords, viewDir);

    // then sample textures with new texture coords
    vec3 diffuse = texture(diffuseMap, texCoords).rgb;
    vec3 normal = texture(normalMap, texCoords).rgb;
    normal = normalize(normal * 2.0 - 1.0);

    // proceed with lighting code
    [...]
}

```

这里关键的函数是 `ParallaxMapping()`。

```cpp
vec2 ParallaxMapping(vec2 texCoords, vec3 viewDir) {
	// 获取视差（高度）贴图中的高度值
	float height = texture(depthMap, texCoords).r;
	// 实际是 P 向量在纹理上的投影
	vec2 p = viewDir.xy / viewDir.z * (height * height_scale);
	return texCoords - p;
}
```

***
这里计算 `p` 的代码有些跳跃，为什么是 `viewDir.xy / viewDir.z`？为什么乘上高度和高度缩放量？我们一点点看。
### $\frac{V_{xy}}{V_z} * h$ 的[原因](https://catlikecoding.com/unity/tutorials/rendering/part-20/)

假设纹理高度在某个区域都是 0，则如下图：

![](images/视差贴图P向量计算解释示意图.png)

能够得到等式：

$$
\begin{align}
\frac{offset}{Height} &= \frac{V_{xy}}{V_z} \\ 
offset &= \frac{V_{xy}}{V_z} \times Height 
\end{align}
$$

该算法有个问题，当观察角度较小时，$V_z$ 分量也相应较小，此时计算结果会非常大。为了解决这个问题，通常会加一个偏移量 0.42 来减少低角度的影响：

$$
offset = \frac{V_{xy}}{V_z + 0.42} \times Height
$$
***
因此上面的计算示意图如下：

![](images/视差贴图实际计算示意图.png)

代码中计算得到的 `p` 是途中在纹理平面的二维向量，因为视线方向的 `xy` 是（图中）向右的，因此 `p`  的方向也是（图中）向右的，最后得到的偏移后的纹理坐标为 `TexCoords`（A 的纹理坐标）减去偏移向量。

 直接使用 A 的高度值会导致偏差较大，因此乘以一个缩放量来优化计算结果。
 
在边缘位置，由于视差贴图偏移后可能会超出纹理坐标的 $[0, 1]$ 范围，因此需要剔除超出部分，否则会导致实际效果不真实。

![](images/视差贴图与法线贴图对比.png)