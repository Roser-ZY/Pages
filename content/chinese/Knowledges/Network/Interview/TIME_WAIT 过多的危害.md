---
title: "TIME_WAIT 过多的危害"
author: "Roser"
date: 2025-03-12
image: "images/content/Network.png"
draft: false
tags:
  - Network
  - TCP
  - Interview
  - Review
sr-due: 2025-05-13
sr-interval: 62
sr-ease: 310
---
- 占用系统资源，例如文件描述符，内存，CPU 或线程等。
- 占用端口资源。

对于客户端来说，[TIME_WAIT](为什么需要%20TIME_WAIT？.md) 过多会导致无法向相同四元组发起连接，即端口资源和系统资源都会被影响。

对于服务端来说，主要影响是会占用过多系统资源，因为服务端一般只监听一个端口