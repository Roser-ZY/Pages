---
title: "Construction Script"
author: "Roser"
date: 2025-05-09
image: "images/content/UE5.png"
draft: false
tags:
  - UE5
  - Todo
draft: false
---
创建蓝图类的实例时（放入场景），构造脚本（Contruction Script）在组件列表之后运行。它包含的节点图表允许蓝图实例执行初始化操作（如果继承自 C++ 类则会在该流程调用 [OnConstruction()](../Cpp/OnConstruction().md)）。

构造脚本在蓝图中可操作实现。

借助该函数可以实现在 UE5 编辑阶段就可以显示并配置类的信息，从而结合程序化实现和蓝图编辑。

需要注意的是，User Construction Script 不等于 `OnConstruction()`。