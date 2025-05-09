---
title: "Cursor"
author: "Roser"
date: 2025-05-09
image: "images/content/IndexedDB.png"
draft: false
tags:
  - IndexedDB
  - DBAccess
---
除了[基础访问方法](../创建与访问-Object-Store)外，还可以通过 Cursor 访问数据库。Cursor 类似迭代器，通过调用 `openCursor()` 成员方法，或者 [Index](../Index) 通过 [IDBKeyRange](../IDBKeyRange) 的方式获取数据时会用到。

获取到的 `cursor` 有两个属性：`key` 和 `value`。其中 `key` 是当前数据的主键，`value` 是存储的数据对象，可通过 `value` 获取数据对象的属性。每个 `cursor` 只能读取一个数据，通过调用 `cursor` 的 `continue()` 成员方法便可以按顺序访问下一个成员。这里的顺序可以通过 `openCursor()` 方法的参数指定。

```typescript
function displayData() {
  const keyRangeValue = IDBKeyRange.only("A");

  const transaction = db.transaction(["fThings"], "readonly");
  const objectStore = transaction.objectStore("fThings");

  objectStore.openCursor(keyRangeValue).onsuccess = (event) => {
    const cursor = event.target.result;
    if (cursor) {
      const listItem = document.createElement("li");
      listItem.textContent = `${cursor.value.fThing}, ${cursor.value.fRating}`;
      list.appendChild(listItem);

      cursor.continue();
    } else {
      console.log("Entries all displayed.");
    }
  };
}

```

上述代码就是通过索引和 `IDBKeyRange` 获取 Cursor 并遍历的例子。注意在 `onsuccess` 中遍历 Cursor 用的是 `if(cursor)` 而不是 `while(cursor)`，这是因为调用 `cursor.continue()` 之后会再次触发 `onsuccess`，本质上这个循环是在 `onsuccess` 之上的循环。

当 Cursor 到达末尾时，依旧会触发 `onsuccess`，但此时 `event.target.result` 为 `undefined`。
# TODO

- 指定范围和方向。