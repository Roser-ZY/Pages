---
title: "DHCP 协议"
author: "Roser"
date: 2025-05-09
image: "images/content/Network.png"
draft: false
tags:
  - IP
  - Network
  - Review
sr-due: 2025-05-09
sr-interval: 32
sr-ease: 250
---
一般来说。DHCP 客户端监听 68 端口，DHCP 服务端监听 67 端口。

![](images/DHCP%20协议流程.webp)

DHCP 协议包含四个步骤：
- 客户端首先发送 DHCP 发现报文（DHCP DISCOVER），由于客户端还没有 IP 地址，并且不知道 DHCP 服务器地址，因此该报文使用 UDP 广播通信。
- DCHP 服务器收到 DHCP 发现报文时，使用 DCHP 提供报文（DCHP OFFER）向客户端做出响应。该报文依然使用广播，并携带相关 IP 信息。
- 客户端收到一个或多个 DCHP 提供报文后，从中选择一个服务器，向选中的服务器发送 DCHP 请求报文（DCHP REQUEST），回显服务器配置的 IP 信息。
- 服务端用 DCHP 确认报文（DCHP ACK）对请求进行确认，并应答相关配置信息。

客户端收到 DCHP ACK 之后，整个协议便完成交互。IP 到期时，客户端会向 DCHP 服务器重新发送 DCHP 请求报文，如果服务器不同意租用，会响应 DCHP NACK 报文。

由于整个 DCHP 协议过程都是 UDP 广播，需要 DCHP 服务器在同一个网络内，这会导致 DCHP 服务器较多。为了解决这个问题，引入了 DCHP 中继代理。

![](images/DCHP%20中继代理.webp)

中继代理由路由器完成，同一网络内仍然使用广播，但是中继代理之间使用单播，这样便可以配置一个比较顶层的 DCHP 服务器，即可为多个子网提供服务。