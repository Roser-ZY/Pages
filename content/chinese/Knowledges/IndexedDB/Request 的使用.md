---
title: "Request 的使用"
author: "Roser"
date: 2025-03-10
image: "images/content/IndexedDB.png"
draft: false
tags:
  - IndexedDB
---
在 IndexedDB 中，一切操作都需要**请求**（*Request*）。几乎所有的数据库操作都会返回一个 Request 对象，后续对该次操作的错误处理或成功处理都需要通过绑定回调函数，或者添加事件监听器来实现。

IndexedDB 的异步实际上是依赖 JS 的[事件循环](../../JavaScript/事件循环)来实现的。

```typescript
// Let us open our database
const request = window.indexedDB.open("MyTestDatabase", 3);

request.onerror = (event) => {
  // Do something with request.error!
};
request.onsuccess = (event) => {
  // Do something with request.result!
};
```

IndexedDB Request 的基类为 `IDBRequest`，继承自 `EventTarget`。该基类除了继承  `EventTarget` 属性外，还有以下几个属性：
- [`IDBRequest.error`](https://developer.mozilla.org/en-US/docs/Web/API/IDBRequest/error) Read only
- [`IDBRequest.result`](https://developer.mozilla.org/en-US/docs/Web/API/IDBRequest/result) Read only
-  [`IDBRequest.source`](https://developer.mozilla.org/en-US/docs/Web/API/IDBRequest/source) Read only
- [`IDBRequest.readyState`](https://developer.mozilla.org/en-US/docs/Web/API/IDBRequest/readyState) Read only
- [`IDBRequest.transaction`](https://developer.mozilla.org/en-US/docs/Web/API/IDBRequest/transaction) Read only

可以看到每一个回调函数都会接收一个 `event` 参数，实际上 `event.target` 就是 `request`，因此上述代码的回调函数中，既可以通过 `event.target` 访问上述属性，也可以通过 `request` 闭包访问。

下表给出了各个属性在 `onsuccess`，`onupgradeneeded` 和 `onerror` 中可能的值。

| **属性**                    | **回调函数**          | **值**                                            | **描述**                                           |
| ------------------------- | ----------------- | ------------------------------------------------ | ------------------------------------------------ |
| **`request.result`**      | `onsuccess`       | `IDBDatabase` 或与操作相关的值                           | 成功打开的数据库实例或操作结果（如 `get` 的数据）。                    |
|                           | `onupgradeneeded` | `IDBDatabase`                                    | 当前数据库实例，用于升级模式迁移（如创建对象存储）。                       |
|                           | `onerror`         | `undefined`                                      | 错误时没有结果，`result` 不返回任何值。                         |
| **`request.error`**       | `onsuccess`       | `null`                                           | 成功时没有错误。                                         |
|                           | `onupgradeneeded` | `null`                                           | 升级过程中未发生错误时没有错误。                                 |
|                           | `onerror`         | `DOMException`                                   | 具体的错误对象，包含 `name` 和 `message` 描述错误信息。            |
| **`request.source`**      | `onsuccess`       | `null` 或对象存储 (`IDBObjectStore`) 或索引 (`IDBIndex`) | 发起请求的来源（例如操作的对象存储或索引），对 `open` 操作为 `null`。       |
|                           | `onupgradeneeded` | `null`                                           | 打开数据库的 `source` 始终为 `null`。                      |
|                           | `onerror`         | 同上                                               | 同 `onsuccess` 或 `onupgradeneeded`。               |
| **`request.transaction`** | `onsuccess`       | `null`                                           | 数据库操作成功时不在事务上下文中，因此为 `null`。                     |
|                           | `onupgradeneeded` | `IDBTransaction`                                 | 升级操作的事务对象，用于迁移模式（如创建或删除对象存储）。                    |
|                           | `onerror`         | `null`                                           | 错误发生时可能没有事务上下文，因此为 `null`。                       |
| **`request.readyState`**  | `onsuccess`       | `'done'`                                         | 请求已成功完成。                                         |
|                           | `onupgradeneeded` | `'pending'`                                      | 升级过程中请求处于挂起状态。                                   |
|                           | `onerror`         | `'done'`                                         | 请求已失败完成。                                         |
| **`request.event`**       | `onsuccess`       | 触发的 `Event` 对象                                   | 表示请求的成功事件对象，可从 `event.target` 获取 `request`。      |
|                           | `onupgradeneeded` | 同上                                               | 表示请求的升级事件对象，可获取 `oldVersion` 和 `newVersion` 等信息。 |
|                           | `onerror`         | 同上                                               | 表示请求的错误事件对象，可从 `event.target.error` 获取错误信息。      |