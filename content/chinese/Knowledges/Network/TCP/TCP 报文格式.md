---
title: "TCP 报文格式"
author: "Roser"
date: 2025-05-09
image: "images/content/Network.png"
draft: false
tags:
  - Network
  - TCP
---
TCP 报文格式如下：

![](images/TCP报文格式.png)
各个字段含义如下：

| 字段名称                       | 长度  | 用途                                       |
| -------------------------- | --- | ---------------------------------------- |
| 源端口号（Source Port）          | 16位 | 标识发送方的端口号，用于区分同一设备上不同的应用程序。              |
| 目的端口号（Destination Port）    | 16位 | 标识接收方的端口号，用于将数据包正确路由到特定应用程序。             |
| 序号（Sequence Number）        | 32位 | 对字节流中的每个字节进行编号，接收方按顺序重组数据。               |
| 确认号（Acknowledgment Number） | 32位 | 表示接收方期望接收的下一个字节的序号。                      |
| 首部长度（Header Length）        | 4位  | 指定TCP报文段的首部长度，以32位字为单位。                  |
| 保留（Reserved）               | 3位  | 为将来使用保留，当前必须为0。                          |
| 标志位（Flags）                 | 9位  | 控制TCP连接状态（URG, ACK, PSH, RST, SYN, FIN）。 |
| 窗口大小（Window Size）          | 16位 | 指示发送方当前能够接收的最大数据量，用于流量控制。                |
| 校验和（Checksum）              | 16位 | 检验TCP首部和数据是否在传输中出现错误。                    |
| 紧急数据指针（Urgent Pointer）     | 16位 | 指示紧急数据在段中的最后一个字节的偏移量。                    |
| 选项（Options）                | 可变  | 提供额外选项，如最大报文段大小（MSS）、时间戳等。               |
| 数据（Data）                   | 可变  | 实际传输的应用层数据。                              |
