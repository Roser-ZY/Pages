---
title: "git add"
author: "Roser"
date: 2025-02-19
image: "images/content/Git.png"
draft: false
tags:
  - Git
---
[TOC]
# --renormalize

执行清洁程序，来更新所有被追踪的文件，将他们重新添加到索引中。这个一般用于修改 `core.autocrlf` 配置或者 `.gitattribute` 文件的 `text` 配置之后，来修正文件中错误的 `CRLF/LF` 换行符。