---
title: "服务器大量出现 TIME_WAIT 的原因有哪些？"
author: "Roser"
date: 2025-03-12
image: "images/content/Network.png"
draft: false
tags:
  - Network
  - TCP
  - Interview
  - Review
sr-due: 2025-05-14
sr-interval: 63
sr-ease: 310
---
TIME_WAIT 只会出现在 [TCP 四次挥手](../TCP/TCP%20四次挥手.md)主动断开连接的一方，服务端如果出现大量 TIME_WAIT，说明服务端主动断开了很多 TCP 连接。有以下几种可能：

- 没有使用长连接。
- 长连接超时（心跳停止）。
- 长连接请求达到数量上限。

