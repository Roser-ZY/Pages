---
title: "Actor 生命周期"
author: "Roser"
date: 2025-04-18
image: "images/content/UE5.png"
draft: false
tags:
  - UE5
draft: true
---
![](image/Actor生命周期示意图.png)

# 从磁盘加载

从磁盘加载（Load From Disk）适用于已经在关卡中设置的 Actor。当 `UEngine::LoadMap` 调用时，或者当关卡流送调用 `UWorld::AddToWorld` 时。

1. 从磁盘加载包/关卡中的 Actor。
2. 序列化的 Actor 从磁盘加载完成后调用 `PostLoad`，所有自定义版本化和修复操作在此处执行。
	`PostLoad` 和 `AActor::PostAcrotCreated()` 互斥。
3. 
（TODO）
# 在编辑器中运行

在编辑器中运行（Play in Editor）路径，Actor 是从编辑器中复制来。复制的 Actor 按照从磁盘加载路径先沟通流程初始化。
# 生成

生成 Actor 实例是在世界生成后，一般在开始游戏后才可调用。

这类 Actor 在编辑器中是看不到的。