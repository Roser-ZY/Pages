---
title: "ARP 协议与 RARP 协议"
author: "Roser"
date: 2025-04-07
image: "images/content/Network.png"
draft: false
tags:
  - Network
  - IP
  - Review
sr-due: 2025-05-11
sr-interval: 34
sr-ease: 270
---
# ARP 协议

ARP 协议用于找到下一跳的 MAC 地址。虽然[路由转发](../路由转发)过程能访问路由表并确定下一跳 IP，但是网络层下一层是数据链路层，因此还需要下一层 MAC 地址。

ARP 借助 ARP 请求与 ARP 响应两种包来确定并收集 MAC 地址。ARP 是网络层的协议。

**主机**会通过广播发送 ARP 请求，这个包中包含了想要知道的 MAC 地址的主机 IP 地址。相同网络中的所有设备（路由器，主机）收到 ARP 请求时，会进行拆包并检查请求的 IP 地址，如果与自己的 IP 相同，会将自己的 MAC 地址写入 ARP 响应并返回给请求主机。

操作系统通常会缓存 ARP 获取的 MAC 地址，但是有一定期限，超过期限会清除。
# RARP 协议

顾名思义，与 ARP 相反，RARP 时已知 MAC 地址求 IP 地址。RARP 通常需要在网络中假设一台 RARP 服务器，在该服务器上注册设备的 MAC 地址及对应 IP，其他设备向该服务器请求。