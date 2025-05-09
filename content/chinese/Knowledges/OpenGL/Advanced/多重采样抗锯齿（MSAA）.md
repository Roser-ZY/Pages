---
image: "images/content/OpenGL.png"
author: "Roser"
date: 2025-05-08
draft: false
tags:
  - OpenGL
  - Review
sr-due: 2025-05-21
sr-interval: 41
sr-ease: 241
title: 多重采样抗锯齿
---
多重采样抗锯齿借鉴了[超采样抗锯齿](抗锯齿.md)的理念，但是以更加高效的方式来实现。

在[光栅化](../光栅化.md)一节介绍过，单一采样点会导致图形边缘总是会出现锯齿。多重采样则是将单一采样点变为多个采样点（名称由来），现在不再使用像素中心的单一采样点，而是使用以**特定图案**排列的4个**子采样点（Subsample）**。多重采样抗锯齿技术用这些子采样点来决定像素的遮盖度。

这里所说的 4 个子采样点只是一种方案，还有更多的采样方法。

> 多重采样抗锯齿的问题在于它跟**延迟渲染**不兼容。

![](images/多重采样子采样点示意图.png)

> 子采样点的数量可以自定义，更多采样点能带来更精确的遮盖率，相应的也会增加性能开销。

MSAA 过程中，片段着色器只运行一次，会使用更大的深度和模板缓冲区来确定子采样点的覆盖率。被覆盖的子采样点的数量决定了像素颜色对帧缓冲的影响程度。通过这种浅色边缘，能够在视觉上产生更平滑的效果。

![](images/MSAA采样示意图.png)

![](images/MSAA着色示意图.png)

> 只运行一次片段着色器是很关键的一点。

有以下几种多重采样方式：

![](images/多重采样抗锯齿方式png.png)

由于片段着色器使用的是片段的中心位置，如果采用 4xMSAA，会因为中心没有被三角形覆盖导致片段着色器输出颜色有问题。此时会采用重心采样（Centroid Sampling）来解决这个问题。重心采样是 GPU 自动执行的，GPU 通过覆盖的采样点来确定采样的重心点，以避免出现片段着色器的采样点位于三角形之外的问题。

![](images/MSAA非重心采样的问题.png)
# 使用 MSAA

使用 MSAA 时，必须要使用一个能在每个像素中存储大于 1 个颜色值的颜色缓冲（因为多重采样的采样点为多个，每个采样点都存储一个颜色）。因此需要使用一个新的缓冲类型来存储多重采样样本，即**多重采样缓冲（Multisample Buffer）**。

GLFW 提供了该功能，使用多重采样缓冲代替默认的颜色缓冲。我们要做的只是提示（Hint）GLFW 我们希望使用一个包含 N 个样本的多重采样缓冲，在**创建窗口之前**调用 `glfwWindowHint` 实现：

```cpp
glfwWindowHint(GLFW_SAMPLES, 4);
```

上述代码让每个屏幕坐标使用一个包含 4 个采样点的颜色缓冲。之后，调用 `glEnable(GL_MULTISAMPLE)` 来启用多重采样。

> 默认情况下多重采样都是启用的，上述操作只是为了保险起见。

## 离屏 MSAA

这部分逻辑简单来说就是将多重采样的数据写入到我们自己创建的[[帧缓冲]]，并绑定到纹理附件或渲染缓冲对象（支持多重采样的）上，后续可以直接再转换到默认缓冲，或者另一个普通帧缓冲，以实现后期处理等操作。

### 多重采样纹理附件

创建支持存储多个采样点的纹理时，需要使用 `glTexImage2DMultisample` 函数代替 `glTexImage`，并将纹理绑定到 `GL_TEXTURE_2D_MULTISAMPLE` 目标。

```cpp
glBindTexture(GL_TEXTURE_2D_MULTISAMPLE, tex);
glTexImage2DMultisample(GL_TEXTURE_2D_MULTISAMPLE, 4, GL_RGB, width, height, GL_TRUE);
glBindTexture(GL_TEXTURE_2D_MULTISAMPLE, 0);
```

`glTexImage2DMultisample` 的第二个参数设置的是 MSAA 使用的子采样点的数量，最后一个参数则表示是否对每个纹素使用相同的样本位置和相同数量的子采样点个数。

使用 `glFramebufferTexture2D` 将多重采样纹理附加到帧缓冲上，但是这里的纹理类型使用 `GL_TEXTURE_2D_MULTISAMPLE`。

```cpp
glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D_MULTISAMPLE, tex, 0);
```

### 多重采样渲染缓冲对象

对应创建一个多重采样渲染缓冲对象也是类似的，需要修改下调用的函数：

```cpp
glRenderbufferStorageMultisample(GL_RENDERBUFFER, 4, GL_DEPTH24_STENCIL8, width, height);
```

第二个参数也是 MSAA 使用的子采样点的数量。

### 渲染到多重采样帧缓冲

渲染到多重采样帧缓冲很简单，绑定帧缓冲后，绘制的任何东西都会由光栅器进行多重采样运算，并最终得到多重采样帧缓冲。

这里的问题是，如何将这个多重采样帧缓冲，在屏幕上渲染出来？

多重采样帧缓冲不能直接用于着色器采样等渲染流程，因此需要在代码中提前进行处理。通常使用 `glBlitFramebuffer` 实现，它能将一个帧缓冲中的某个区域复制到另一个帧缓冲中，**并将多重采样缓冲处理（Resolve）为普通帧缓冲**。

`glBlitFramebuffer` 会将一个用 4 个屏幕空间的缓冲拷贝到另一个同样用 4 个屏幕空间的缓冲。

> 这里不明白为什么突然要强调 4 个屏幕空间，而且翻译也没看懂，这里的 4 并不是指子采样点的数量。
> 
> 其实就是 `glBlitFramebuffer` 将多重采样帧缓冲拷贝到另一个普通帧缓冲，期间处理了多重采样的信息。

在帧缓冲一节，我们同时绑定了读取和绘制的帧缓冲目标，现在我们可以分别绑定到 `GL_READ_FRAMEBUFFER` 和 `GL_DRAW_FRAMEBUFFER`，`glBlitFramebuffer` 函数会根据这两个目标决定哪一个是源，哪一个是目标。

```cpp
glBindFramebuffer(GL_READ_FRAMEBUFFER, multisampledFBO);
glBindFramebuffer(GL_DRAW_FRAMEBUFFER, 0);
glBlitFramebuffer(0, 0, width, height, 0, 0, width, height, GL_COLOR_BUFFER_BIT, GL_NEAREST);
```
### 后期处理

如果希望进行后期处理，则需要将最后这一步渲染到另一个自定义帧缓冲，然后再去进行帧缓冲那一节的后期处理部分即可。