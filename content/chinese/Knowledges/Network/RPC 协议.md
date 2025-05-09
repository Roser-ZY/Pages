---
title: "RPC 协议"
author: "Roser"
date: 2025-05-09
image: "images/content/Network.png"
draft: false
tags:
  - Network
  - Protocol
---
RPC 协议（Remote Procedure Call，远程过程调用）是一种允许程序在不同地址空间（通常是不同计算机）之间调用函数的通信协议。

RPC 工作流程如下：
- **客户端调用本地存根函数**，传递参数。
- **客户端存根封装请求**（序列化），发送到服务器。
- **服务器存根解析请求**（反序列化），调用本地方法。
- **方法执行完成**，服务器存根封装返回值并发送回客户端。
- **客户端存根接收返回值**，反序列化并返回给调用者。

常见的 RPC 实现协议有：

| 协议           | 传输方式               | 序列化方式      | 适用场景            |
| ------------ | ------------------ | ---------- | --------------- |
| **gRPC**     | HTTP/2             | Protobuf   | 高效、跨语言、微服务      |
| **Thrift**   | TCP/HTTP           | Thrift IDL | 适用于大规模分布式系统     |
| **JSON-RPC** | HTTP/TCP/WebSocket | JSON       | 轻量级、适用于 Web 应用  |
| **XML-RPC**  | HTTP               | XML        | 早期 Web 服务       |
| **Dubbo**    | TCP                | Hessian    | 适用于 Java 生态的微服务 |
RPC 与 RESTful API 的区别如下：

|对比项|RPC|RESTful API|
|---|---|---|
|**通信协议**|自定义协议（TCP、HTTP/2）|HTTP|
|**数据格式**|Protobuf、Thrift、JSON|JSON、XML|
|**调用方式**|方法调用（类似函数调用）|资源访问（基于 URL）|
|**性能**|高效，适用于大规模微服务|相对较低|
|**适用场景**|内部服务、微服务通信|对外开放 API|
RPC 一般用于高性能场景，例如：
- **微服务架构**（如 Kubernetes、Service Mesh）
- **分布式系统**（如云计算、存储系统）
- **高性能场景**（如游戏服务器、金融系统）
- **需要跨语言通信**（如 Python 调用 Go、C++）

本质上，RPC 是由一些实现协议定义接口格式，并且这些实现协议封装了向服务端请求和响应的细节，在调用者看来，就仿佛在调用本地函数一样，但是本质上是客户端与服务器之间的数据交换。