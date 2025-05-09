---
title: "instanceof 原理"
author: "Roser"
date: 2024-12-27
image: "images/content/JavaScript.png"
draft: false
tags:
  - JavaScript
---
`instanceof` 用于测试某个对象是否是某个**构造函数**的实例，需要提供一个 `object` 和一个 `Constructor`。

`instanceof` 工作原理如下：
1. 获取 `Constructor.prototype`；
2. 判断 `object.__proto__`（对象原型）是否指向 `Constructor.prototype`。如果不匹配，则递归检查 `object.__proto__.__proto__`，直到原型链末尾（`null`）。
3. 如果找到了匹配的原型，则返回 `true`，否则返回 `false`。