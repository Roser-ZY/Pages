---
title: "Hugoplate 配置"
author: "Roser"
date: 2025-05-09
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

如果只有一个语言，记得清理其他语言的配置文件，包括：
- `config/_default/menus_xx.toml`
	- 必须要删除，否则文章会重复出现。
- `i18n/xx.yaml`
- `content/xxxxxx`

其中 xx 为 language code，xxxxxx 为在 `language.toml` 中配置的对应语言的 content 目录。

> 如果只有一个语言，记得将 `hugo.toml` 中的 `defaultContentLanguageInSubdir` 设置为 `false`，否则根路由后面会添加 language code 的路由。
### 主要文章页面

在 `params.toml` 配置文件中，需要修改（添加到）`mainSections` 和 `search.includeSections`。

前者是告知主体哪些 Section 是主要文章 Section，后者是告知搜索时的范围。

注意这两个的大小写，`mainSections` 似乎大小写不敏感，但是 `search.includeSections` 是大小写敏感的，且后者似乎是要和生成的 `public` 目录下的大小写为准（或者说是路由）。

> 目前主题使用了 `categories` 配置来确认一些内容，我将其修改为判断 `tags`。

### 特殊页面

例如主页，About 等，可以参考模板中的文章。
### 作者

作者介绍文档名称需要与文章中配置的名称对应，大小写不区分。
### 数学公式

官网配置 [Hugo Latex 识别](https://gohugo.io/content-management/mathematics/)。
### 部署

仓库下有五个平台的发布配置。

github page 的发布可直接使用 `.github/workflows` 目录下的配置即可。
#### 链接格式与图片

obsidian 的链接会有 `.md` 后缀名，并且空格（`%20`）需要处理为 `-`，另外解析后的相对路径是要多一层的（因为文章会被解析到同名目录下），因此开头需要新增一层 `../`，通过脚本实现该处理过程。

使用相对路径，同目录下的 images 存储图片，然后用脚本将图片拷贝到统一的 asset/images 目录下即可。
#### 代码样式

代码在白色主题下文本颜色为黑色，而背景也是黑色，导致看不见普通文本。