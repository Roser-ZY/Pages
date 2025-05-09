---
title: "WebSocket"
author: "Roser"
date: 2025-05-09
image: "images/content/Network.png"
draft: false
tags:
  - Network
  - Protocol
  - Todo
---
WebSocket 是一种 **全双工（Full-Duplex）** 的通信协议，它建立在 **TCP 之上**，允许客户端和服务器之间进行 **实时、双向通信**，比传统的 **HTTP 轮询** 或 **长轮询** 更高效。

WebSocket 和 Socket 没有关系，只是名字相似。

该协议的主要应用场景是在一些网页游戏，协同应用中，需要服务端主动向客户端推送数据。

实现 WebSocket 首先需要通过 HTTP 进行握手和协议升级，服务端响应后便可建立连接。