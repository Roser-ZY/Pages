---
title: "MSL 与 TTL"
author: "Roser"
date: 2025-05-09
image: "images/content/Network.png"
draft: false
tags:
  - Network
  - Review
sr-due: 2025-05-16
sr-interval: 65
sr-ease: 310
---
报文最大生存时间（Maximum Segment Lifetime, MSL）是任何报文在网络上存在的最长时间，超过这个时间的报文将被丢弃。

报文生存时间（Time To Live, TTL）是一个用于控制报文生命周期的字段，位于 IP 层，指示 IP 数据报可以经过的最大路由数，每经过一个处理它的路由西，该值就减 1，当此值为 0 时，丢弃该报文。

 MSL 单位是时间，而 TTL 时经过路由的跳数，**MSL 要大于等于 TTL 消耗为 0 的时间**，以确保达到 MSL 时报文自然消亡。

一般来说，TTL 值为 64，Linux 将 MSL 设置为 30 秒，意味着 Linux 认为数据报文经过 64 个路由器的时间不会超过 30 秒，如果超过了则认为该报文丢失了。