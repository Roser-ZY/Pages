---
title: "Snapshot Interpolation"
author: "Roser"
date: 2025-04-07
image: "images/content/Network.png"
draft: false
tags:
  - Network
  - Review
  - MultiplayerGame
draft: true
---
Snapshot Interpolation 翻译为快照插值（后续本文简称为 SI）。SI 主要用于同步**状态**。

客户端每帧或定时想服务端发送当前状态（例如位置），服务端校验后广播给所有客户端，客户端根据状态数据做**插值**或**预测**。

快照插值时，需要考虑带宽、网络包发送速率、丢包率和网络包大小。为了让接收端有更好的体验，提升网络包发送速率是最直接的（降低延迟）方法，但是在网络较差的情况下，不得不舍弃发送速率，增加插值计算和预测来减少高延迟带来的卡顿感。
# 插值

插值包括 Linear Interpolation 和 Hermite Interpolation。插值的作用是优化网络包接受的不均匀导致的画面卡顿和漂移，通过在网络包之间计算插值并模拟，可以有效提升接收方的体验。
# 预测

预测（Extrapolation）与插值（Interpolation）不同。插值是根据两个或多个已接收数据进行计算，而预测试根据最新的数据，推测客户端的下一步操作，做出预测。

> 翻译问题，英文是有对应的。
> 插值是在两个已知数据之间计算一个值，预测则实在已知数据之外推测一个值。

预测会出现错误，此时需要根据接收的数据包来进行修正。这种情况下，会出现明显的画面回滚，在一些游戏中体验并不好。

> 例如[输入预测](../输入预测)，[Rollback-Netcode](../Rollback-Netcode)等方法。
# 压缩

为了提高数据传输速率，可以对数据进行压缩。