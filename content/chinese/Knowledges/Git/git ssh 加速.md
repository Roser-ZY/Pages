---
title: "git ssh 加速"
author: "Roser"
date: 2025-05-09
image: "images/content/Git.png"
draft: false
tags:
  - Git
  - Todo
---
使用 SSH 连接时，可能会出现 git fetch/pull/push 时卡很久才出现后续命令提示的问题，并且后续过程很流畅。这是因为在前期握手阶段卡顿导致。

可以添加 `~/.ssh/config` 配置文件，然后添加

```bash
Host github.com
  HostName github.com
  User git
  ProxyCommand nc -x 127.0.0.1:7890 %h %p
```

如果是 clash，则可以使用以下配置

```bash
Host github.com
  ProxyCommand /usr/bin/nc -X 5 -x 127.0.0.1:7890 %h %p
```