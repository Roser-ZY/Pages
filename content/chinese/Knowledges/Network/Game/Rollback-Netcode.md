---
title: "Rollback-Netcode"
author: "Roser"
date: 2025-05-09
image: "images/content/Network.png"
draft: false
tags:
  - Network
  - Algorithm
  - MultiplayerGame
  - Review
draft: true
---
回滚网络代码（Rollback Netcode）是一种解决网络延迟的方法，用于需要严格帧同步的联机游戏，通常为格斗游戏（例如街霸，拳皇等）。

该算法的核心思想就是回滚，类似于[分支预测](../../../Computer-Architecture/分支预测)。