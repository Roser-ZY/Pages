---
title: "OSI 模型与 TCP-IP 模型"
author: "Roser"
date: 2025-05-08
image: "images/content/Network.png"
draft: false
tags:
  - Network
---
OSI 模型是由国际标准化组织制定的开放式系统互联通信参考模型，该模型有七层。

OSI 模型太复杂，提出的也只是概念上的分层，没有具体的实现方案。目前比较普遍且实用的模型是 TCP/IP 模型，该模型有四层。Linux 系统便是按照该模型来实现网络协议栈的。

![](images/OSI与TCP.webp)

其中 TCP/IP 模型的网络接口层和应用层，在一些特定请款下可以人为拆分，下图为从该模型扩展出的五层网络模型及其数据封装流程：
![](images/五层模型层级传输过程.png)