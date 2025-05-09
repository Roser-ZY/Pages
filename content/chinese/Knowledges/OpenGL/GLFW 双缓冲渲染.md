---
title: "GLFW 双缓冲渲染"
author: "Roser"
date: 2025-04-10
image: "images/content/OpenGL.png"
draft: false
tags:
  - OpenGL
  - GLFW
  - Review
sr-due: 2025-07-22
sr-interval: 103
sr-ease: 270
---
GLFW 使用双缓冲机制来渲染屏幕画面。

- **前缓冲区（Front Buffer）**：当前显示在屏幕上的画面。
- **后缓冲区（Back Buffer）**：存储当前帧的渲染结果，未显示

使用 GLFW 进行窗口管理时，我们会在最后执行 `glfwSwapBuffers()`。该函数的作用是交换前后缓冲，使后缓冲区的渲染的内容显示到屏幕上。

在调用该函数前，我们会进行很多渲染操作，这些操作不会实时渲染到屏幕上，而是都保存在了后缓冲区。只有调用交换函数后，才会更新屏幕。

通常调用 `glfwSwapBuffer()` 之后，会调用 `glfwPollEvents()` 来处理键盘、鼠标等输入事件，确保交互正常。