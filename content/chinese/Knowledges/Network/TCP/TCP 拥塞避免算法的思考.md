---
title: "TCP 拥塞避免算法的思考"
author: "Roser"
date: 2025-05-09
image: "images/content/Network.png"
draft: false
tags:
  - Network
  - TCP
draft: true
---
拥塞避免算法总是在增加发送包的数量，并在出现重传时修改阈值和窗口，让后续的发送速率放缓。

问题是，拥塞避免算法这样总是会再次到达阈值，然后又继续减少阈值。这不会影响后续的发送速率吗？为什么不能在发生重传时，寻找一个小一点的窗口，固定速率发送呢？然后周期性再次探测是否有更大的窗口可以提高速率。

这个想法很像的一个策略是 TCP BBR。