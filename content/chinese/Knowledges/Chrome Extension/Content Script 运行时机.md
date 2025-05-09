---
title: "Content Script 运行时机"
author: "Roser"
date: 2025-01-06
image: "images/content/Chrome Extension.png"
draft: false
tags:
  - ChromeExtension
  - ContentScript
---
[Manifest V3](../Manifest-V3-是什么) 在配置内容脚本时，可选配置 `run_at` 配置项，类型为 [`RunAt`](https://developer.chrome.com/docs/extensions/reference/api/extensionTypes?hl=zh-cn#type-RunAt)，共有三个类型，默认为 `document_idle`：

- `document_start`
	在 css 中的任何文件之后、构建任何其他 DOM 或运行任何其他脚本之前注入脚本。

- `document_end`
	在 DOM 完成之后，在图片和框架等子资源加载之前立即注入脚本。

- `document_idle`
	浏览器会选择一个时间，在 `document_end` 之间以及 `window.onload` 事件触发后立即注入脚本。注入的确切时刻取决于文档的复杂程度和加载用时，并针对网页加载速度进行了优化。在 `document_idle` 运行的内容脚本不需要监听 `window.onload` 事件；它们一定会在 DOM 完成后运行。如果脚本确实需要在 `window.onload` 之后运行，该扩展程序可以使用 `document.readyState` 属性检查 `onload` 是否已触发。

因此，默认情况下 DOM 已经加载完成，不需要额外监听 DOM 加载相关事件，除非有特殊需求。