---
image: "images/content/OpenGL.png"
draft: false
title: Steep Parallax Mapping
author: Roser Han
date: 2025-04-15
tags:
  - OpenGL
  - Lighting
  - Review
  - Texture
---
陡峭视差映射（Steep Parallax Mapping）与[Parallax Mapping](Parallax%20Mapping.md)本质是一样的，只不过视差贴图制作了一次采样，而陡峭视差贴图会多次采样，以获得更好的模拟点。这种方式能够得到更好的结果，即使高度变化很陡峭也能更精确的获取偏移点。

> 以下均在[切向空间](../../Graphics/切向空间.md)中。

![](images/陡峭视差贴图示意图.png)

陡峭视差贴图的计算方式通常是将深度范围等高度划分到多个层级（Layer），视线会穿过多个层级，我们通过计算每个层级的高度与层级在视线交点处对应投影到纹理的高度值，来确定视线是否穿过了实际观察点 B。

例如上图从高到低检查视线与每个层级交点处的纹理高度值，当层级高度**大于**纹理高度时（注意这里最上面是 0，最下面是 1），表示穿过了纹理（高度）表面。

在进行偏移时，选择与纹理高度值最近的层级交点对应的纹理坐标作为实际（模拟）纹理坐标。
### 编码实现

```cpp
vec2 ParallaxMapping(vec2 texCoords, vec3 viewDir)
{
	// 层级数量
	const float numLayers = 10;
	// 每层的高度差
	float deltaLayerDepth = 1.0 / numLayers;
	// 当前层级的高度
	float currentLayerDepth = 0.0;
	vec2 p = viewDir.xy * height_scale;
	vec2 deltaTexCoords = p / numLayers;


	vec2 currentTexCoords = texCoords;
	vec2 currentDepthMapValue = texture(depthMap, currentTexCoords).r;

	while (currentLayerDepth < currentDepthMapValue) 
	{
		// 修改纹理坐标
		currentTexCoords -= deltaTexCoords;
		// 对纹理处的高度进行采样
		currentDepthMapValue = texture(depthMap, curentTexCoords).r;
		// 修改层级高度
		currentLayerDepth += deltaLayerDepth;
	}

	return currentTexCoords;
}
```

上述代码中，`p`  向量没有除以 `viewDir.z`，因为该计算方法不需要考虑角度问题，此处乘以高度缩放量主要是为了**让 `p` 的长度接近从纹理接触点 $T_0$ 正好到最底层**，因为这样才能与层级交点的纹理坐标对应上。

> 但上图没有精确计算，只是通过一个缩放量进行模拟。

因为层级的高度是相等的，因此映射到纹理坐标上，每层的纹理变化是线性的，此处计算了 `deltaTexCoords`，用于在每层迭代时对 `p` 向量进行线性修改。

后面就可以逐渐逼近正确高度值的纹理坐标了。上面的代码比较粗略，直接将高于纹理高度的层级对应的纹理坐标作为了目标采样点返回了。
### 动态层级

上面的算法可以进行优化。因为当观察角度较大（接近垂直）时，不需要那么多层级，可以通过动态设置层级数来优化。

```cpp
const float minLyaer = 8.0;
const float maxLayer = 32.0;
float numLayers = mix(maxLayer, minLayer, max(dot(vec3(0.0, 0.0, 1.0), viewDir), 0.0));
```
### 问题

我们直接用每个层级来模拟，会导致最终的效果是存在锯齿的，虽然可以增加层级数量，但是会大大降低性能。

为了解决这个问题，在该基础上衍生了更多的算法，例如 [Relief Parallax Mapping](https://github.com/Rabbid76/graphics-snippets/blob/master/documentation/normal_parallax_relief.md#relief-parallax-mapping) 和 Parallax Occlusion Mapping 算法。

- 前者采用二分插值，有更精确的结果。
- 后者采用线性插值，有比前者更好的性能，更常用。