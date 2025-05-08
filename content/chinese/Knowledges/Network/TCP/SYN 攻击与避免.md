---
title: "SYN 攻击与避免"
author: "Roser"
date: 2025-02-11
image: "images/content/Network.png"
draft: false
tags:
  - Network
  - Security
  - TCP
---
SYN 攻击是指攻击者短时间伪造不同的 IP 地址的 SYN 报文，服务端每收到一个 SYN 报文，就进入 SYN_RCVD 状态，但是服务端发送出去的 ACK+SYN 报文由于无法得到未知 IP 主机的 ACK 应答，会占满服务端的**半连接队列**，从而影响服务端服务。

Linux 内核会维护两个队列，半连接队列（SYN 队列）和全连接队列（ACCEPT 队列）。

服务端收到客户端 SYN 报文时，会创建一个半连接对象并加入内核的 SYN 队列。

服务端收到 ACK 保温后，会从 SYN 队列取出半连接对象，然后**创建一个新的连接**放入 ACCEPT 队列。

通过调用 Socket 接口 `accept()` 可从 ACCEPT 队列取出连接对象。

每个队列有最大长度限制，超出限制时会丢弃后续报文。

避免方式有四种：

- 调大 `netdev_max_backlog`。
- 增大 TCP 半连接队列。
- 开启 `net.ipv4.tcp_synccookies`。
- 减少 SYN+ACK 重传次数。