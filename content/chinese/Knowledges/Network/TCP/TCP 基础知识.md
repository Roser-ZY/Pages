---
title: "TCP 基础知识"
author: "Roser"
date: 2025-02-10
image: "images/content/Network.png"
draft: false
tags:
  - Network
  - TCP
---
[TCP 报文](../TCP/TCP-报文格式)中，提供了 TCP 四元组，即源地址，源端口，目的地址，目的端口。一个四元组能唯一确定一个 TCP 连接。

服务端通常固定监听某个本地端口，等待客户端连接请求，而客户端的 IP 和端口是可变的，并且可以有多个客户端。TCP 最大连接数理论值计算公式如下：

$$
\text{最大 TCP 连接数 = 客户端的 IP 数} \times 客户端的端口数
$$

对于 IPv4 来说，客户端最大 IP 数为 $2^{32}$，客户端[最大端口数](../什么是端口号)为 $2^{16}$，理论单机最大连接数为 $2^{48}$。但是实际上服务器最大并发 TCP 连接数远小于理论上限，对于 Linux 服务器来说，主要受以下限制：
- 文件描述符
	每个 TCP 连接都是一个文件，如果文件描述符被占满了，会发生错误。
- 内存限制
	每个 TCP 连接都要占用一定内存，而操作系统的内存是有限的。

> 注意，TCP 连接本身是一对一连接，但是服务器和客户端之间可以建立多个 TCP 连接。