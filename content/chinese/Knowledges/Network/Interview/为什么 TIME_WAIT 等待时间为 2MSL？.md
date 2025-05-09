---
title: "为什么 TIME_WAIT 等待时间为 2MSL？"
author: "Roser"
date: 2025-03-12
image: "images/content/Network.png"
draft: false
tags:
  - Network
  - Interview
  - Review
sr-due: 2025-05-07
sr-interval: 56
sr-ease: 270
---
[Linux 中一个 MSL 等待 30 秒](../../MSL-与-TTL)，因此 TIME_WAIT 状态固定维持 60 秒。

之所以为 2MSL 是因为最后发送的 ACK 数据需要确保服务端收到，如果服务端因为没有收到 ACK 触发超时重传，会重发 FIN，这样一去（ACK）一回（重发的 FIN）就能保证要么收到响应数据，要么主动连接方在这个时间内能收到重传的 FIN，因此应该等待 2MSL 时间。

超时重传的时间是小于 MSL 的，因此 2MSL 时长允许 ACK 或重传 FIN 报文**至少丢失一次**。那为什么不设置 4MSL 或 8MSL 呢？因为丢包率达到百分之一的糟糕网络中，连续两次丢包的概率只有万分之一，忽略这种情况比处理这种情况更有性价比。

另外需要注意，TIME_WAIT 的 2MSL 计时是在主动断开连接方收到 FIN 报文并发送 ACK 报文后开始的，并且每次收到重传 FIN 报文会重置等待时间。

