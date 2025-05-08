---
title: "创建与访问 Object Store"
author: "Roser"
date: 2025-01-10
image: "images/content/IndexedDB.png"
draft: false
tags:
  - IndexedDB
  - DBAccess
---
在使用 Object Store 之前，要检查 Object Store 是否存在：

```typescript
if (!db.objectStoreNames.contains(objectStoreName)) {
    db.createObjectStore(objectStoreName, { keyPath: this.annotationKeyPath });
    console.log('IDBDatabase' + this.dbName + ' create a new object store.');
}
```

如果不存在，则需要创建 Object Store，如果在访问 Object Store 时 Object Store 不存在，则会抛出异常。

只有在更新数据库的时候才能创建 Object Store，创建方法需要先 [打开数据库](创建与打开数据库.md)，然后调用 `IDBDatabase.createObjectStore()` 方法。该方法的第二个参数用于指定一些可选配置项，包含 [Key](数据库结构.md) 生成规则等。

访问 Object Store 时，需要借助[事务](创建与使用事务.md)来完成，创建事务后，可通过事务的成员函数 `objectStore()` 获取指定名称的 ObjectStore。后续数据库操作的对象是 [Object Store](数据库结构.md)，如果没有指明，则该知识点所说的成员方法，均为 Object Store 的成员方法。

数据库的基础操作就是四类：增、删、改、查。分别对应 Object Store 的 `add()`，`delete()`，`put()` 和 `get()` 四个成员方法。

此外还可以通过 [Cursor](Cursor.md) 和 