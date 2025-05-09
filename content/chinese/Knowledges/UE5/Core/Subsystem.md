---
title: "Subsystem"
author: "Roser"
date: 2025-05-09
image: "images/content/UE5.png"
draft: false
tags:
  - UE5
  - Review
  - Todo
draft: false
---
子系统是 UE5 引擎中为了分离功能模块、实现清晰职责划分而引入的架构设计。通常有四类子系统：

| 子系统类型                    | 用途           |
| ------------------------ | ------------ |
| `UEngineSubsystem`       | 网络、渲染等全局服务   |
| `UGameInstanceSubsystem` | 存档管理、成就系统    |
| `ULocalPlayerSubsystem`  | 输入映射、UI、本地配置 |
| `UWorldSubsystem`        | 天气、时间系统等     |
