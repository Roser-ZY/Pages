---
title: "Hugoplate 配置"
author: "Roser"
date: 2025-05-02
image: "images/content/Hugo.png"
draft: false
tags:
  - Hugo
draft: true
---
在 `config/_default` 目录下，有一些默认配置，包括：
- 语言版本的配置。
	- 不同语言的名称，Code，Content 解析目录等。
- 菜单配置（区分语言）。
- 模块配置。
	- 暂时不了解。
- Params 配置。
	- 用于主题自定义的一些配置项参数。
	- 例如页面框架等。

另外，在根目录下，会有一个 `hugo.toml` 配置文件，里面有比较全面的配置。
### 主页

主页的配置分为很多块。

`data/social.json` 文件中存了一些社交网址。
### 多语言管理

在 `hugo.toml` 中可以设置主语言，此处的值为 `config/_default/language.toml` 配置的语言名（以方括号包裹，例如`[zh]`）。

另外，需要在 `i18n` 目录下添加对应语言的网页翻译（非博文内容）。
### 主要文章页面

在 `params.toml` 配置文件中，需要修改（添加到）`mainSections` 和 `search.includeSections`。

前者是告知主体哪些 Section 是主要文章 Section，后者是告知搜索时的范围。

> 目前主题使用了 `categories` 配置来确认一些内容，我将其修改为判断 `tags`。

### 特殊页面

例如主页，About 等，可以参考模板中的文章。