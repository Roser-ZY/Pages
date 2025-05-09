---
title: "Front Matter"
author: "Roser"
date: 2025-05-09
image: "images/content/Hugo.png"
draft: false
tags:
  - Hugo
draft: true
---
Front Matter 位于每个 Markdown 文件的首部，用于：
- 描述内容。
- 增强（Argument）内容。
- 建立与其他内容的联系。
- 控制发布结构。
- 决定模板的选择。

Front Matter 可以是 JSON，TOML 或 YAML 格式。Hugo 通过分隔符来确定是什么格式。

> 目前知识库使用 Obsidian 来记录笔记属性，使用的是 YAML。

格式类型可以是布尔，整型，浮点数，字符串，数组或字典。

虽然可以自行再定义一些 metadata，但是不可以与 Hugo 已有的保留字重名。

关于已有的配置域（Field），可查看[官方文档](https://gohugo.io/content-management/front-matter/#fields)。
***
以下是一些补充配置项。

一般网页标题名由 `title` 控制，如果有 `meta_title`，则网页标签的名称由该项控制。