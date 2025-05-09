---
title: "TCP 连接为什么会出现 select() 触发读事件但数据长度为 0 的情况？如何解决？"
author: "Roser"
date: 2025-05-09
image: "images/content/Network.png"
draft: false
tags:
  - Network
  - Interview
  - TCP
  - Review
sr-due: 2025-12-27
sr-interval: 261
sr-ease: 290
---
`select()` 监听的套接字接收到数据长度为 0，为对端主动调用 `close()` 或 `shutdown()` 关闭连接，意味着当前 TCP 连接应已被远端关闭，此时本端也应该关闭连接，并确保资源释放。

> 如果 `recv()` 数据长度小于 0，则说明连接发生异常错误。

这个过程主要是 [TCP 四次挥手](../../TCP/TCP-四次挥手)时，主动关闭方会向对方发送 FIN 报文，以告知对方准备关闭连接，此时会触发 `recv()` 并接收数据长度为 0。

接收到 FIN 报文时，对方可能还未关闭，只有本地关闭连接（调用 `close()`）后，才会发送确认报文。

具体可以看 [TCP 四次挥手在 Socket 中的体现](../../TCP/TCP-四次挥手在-Socket-中的体现)。