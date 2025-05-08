---
title: "normal 命令"
author: "Roser"
date: 2025-03-10
image: "images/content/Vim.png"
draft: false
tags:
  - Vim
---
`:normal {commands}` 可以在命令模式下执行普通模式的命令，其中 `commands` 表示命令序列。

配合选取范围（% 选取整个文件，n,m 选取 n 到 m 行，或者通过视图模式选取范围）可以实现在选取范围内执行一些普通模式命令。