---
title: "Service Worker 基础"
author: "Roser"
date: 2024-12-23
image: "images/content/Chrome Extension.png"
draft: false
tags:
  - ChromeExtension
  - ServiceWorker
---
Extension Service Worker（后续笔记均简称 Service Worker，与 Web Service Worker 区分）需要在 [Manifest](Manifest%20V3%20是什么.md) 中注册。与 Content Script 可以注册多个脚本文件不同，Service Worker 只能注册一个脚本文件（类似入口）：

```json
{
	"name": "Awesome Test Extension",
	...
	"background": {
		"service_worker": "service-worker.js"
	},
	...
}
```

但是 Service Worker 是很复杂的，为了更好的进行管理，可以通过两种方式将依赖脚本导入 Service Worker 入口脚本：`impoert` 和 `importScripts()` 方法。

> 注意：不支持 `import()` 动态导入。

如果要使用 `import`，必须在 Manifest 中设置 `type` 字段：

```json
	"background": {
		"service_worker": "service-worker.js",
		"type": "module"
	}
```

使用 `importScript()` 则和在 Web Service Worker 中一样。