---
title: "服务端大量出现 CLOSE_WAIT 的原因有哪些？"
author: "Roser"
date: 2025-03-12
image: "images/content/Network.png"
draft: false
tags:
  - Network
  - TCP
  - Interview
  - Review
sr-due: 2025-05-17
sr-interval: 66
sr-ease: 310
---
CLOSE_WAIT 是 [TCP 四次挥手](../TCP/TCP%20四次挥手.md)被动断连方才有的状态，被动断连方没有调用 `close()` 关闭 Socket，就会导致始终不发出 FIN 报文，从而服务端会一直处于 CLOSE_WAIT 而不会转为 LAST_ACK 状态。