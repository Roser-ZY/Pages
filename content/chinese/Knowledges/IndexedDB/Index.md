---
title: "Index"
author: "Roser"
date: 2025-05-09
image: "images/content/IndexedDB.png"
draft: false
tags:
  - IndexedDB
  - DBAccess
---
除了[基础访问方法](../创建与访问-Object-Store)外，还可以通过 [Index](../数据库结构) 获取数据库对象。

使用 Index 索引之前，要先在 [`onupgradeneeded`](../数据迁移) 中调用 Object Store 的成员函数 [`createIndex()`](https://developer.mozilla.org/en-US/docs/Web/API/IDBObjectStore/createIndex) 创建索引，索引可以是唯一索引，也可以不是唯一索引。该函数一般传入三参数，第一个参数为索引名称，第二个参数为索引字段，第三个为配置项，例如标记的当前索引是否为唯一索引。

> Index 同样只能在 `onupgradeneeded` 中创建。

创建索引后，才可以通过 Object Store 的 `index()` 成员方法，指定 Index 名称并获取 `index` 对象，调用 `index` 的成员方法 `get()` 获取存储数据并处理请求，`event.target.result` 即为数据对象。

索引不仅可以选取一个字段，也可以选取多个字段来创建组合索引，并且可以将组合索引标记为一个唯一索引，只需要在创建时为第二个参数传入一个字符串数组，每个元素为一个字段名称即可。

由于 Index 不一定为唯一索引，上述方法获取到的是 Key 最小的数据对象（如果是唯一索引则获取到的就是唯一数据）。

如果想访问多个对象，可以借助 [Cursor](../Cursor) 来实现。需**调用 `index` 的** `openCursor()` 或 `openKeyCursor` 成员方法来获取 `cursor`。

- `openCursor()` 会创建一个普通 Cursor，它有 `key` 属性和 `value` 属性，其中 `key` 并不是主键，而是指定的 `index`，`value` 则是对象数据。
- `openKeyCursor()` 会创建一个 Key Cursor，它有 `key` 属性和 `primaryKey` 属性，其中 `key` 是指定的 `index`，而 `primaryKey` 为主键。