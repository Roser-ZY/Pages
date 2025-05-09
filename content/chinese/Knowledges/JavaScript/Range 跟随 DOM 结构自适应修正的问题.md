---
title: "Range 跟随 DOM 结构自适应修正的问题"
author: "Roser"
date: 2025-05-09
image: "images/content/JavaScript.png"
draft: false
tags:
  - JavaScript
  - DOM
---
Range 记录了当前选取的区域信息。

如果调用 `Range.cloneRange()` 创建了（多个）副本保存，则对源 Range 的修改不会反映到副本，但是如果 DOM 进行了修改并且影响了当前的 Range，则所有 Range（包括副本）都会受到影响并修改。

> 例如对 Range 区域内部的 DOM 进行了修改，则 Range 的`endContainer` 会设置为 `startContainer`，并且 `endOffset` 会设置为 `startContainer`。

这个需要注意，即使对 Range 设置了 `const` 并不能保证在其他作用域不修改该值。

这个问题在对选取区域进行高亮时会出现。