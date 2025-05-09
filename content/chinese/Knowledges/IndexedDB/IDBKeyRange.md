---
title: "IDBKeyRange"
author: "Roser"
date: 2025-01-17
image: "images/content/IndexedDB.png"
draft: false
tags:
  - IndexedDB
---
调用 `IDBKeyRange` 的接口可以创建一个用于 `openCursor()` 等操作的对象。

需要注意的是，该类的静态接口传入的 `value`，可以是主键（Key）也可以是索引（Index），具体需要根据是通过 `objectStore.openCursor()` 打开还是 `index.openCursor()` 打开。