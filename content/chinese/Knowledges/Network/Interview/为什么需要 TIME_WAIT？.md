---
title: "为什么需要 TIME_WAIT？"
author: "Roser"
date: 2025-03-12
image: "images/content/Network.png"
draft: false
tags:
  - Network
  - TCP
  - Review
  - Interview
sr-due: 2025-05-06
sr-interval: 55
sr-ease: 270
---
[TCP 四次挥手](../../TCP/TCP-四次挥手)时，主动断开连接的一方在最后发送 ACK 报文后，会进入 TIME_WAIT 状态，该状态[持续时间为 2MSL](../为什么-TIME_WAIT-等待时间为-2MSL？)。

TIME_WAIT 主要有两个作用：

- 确保被动断开连接方能收到 ACK，如果未收到则主动断开连接方可以重新发送 ACK。
- 防止历史连接中的数据被后续相同四元组的连接错误接收。

由于 2MSL 的延迟，能保证旧连接的所有报文都已经在网络中消失，新建立连接时接收的报文均为新连接产生。