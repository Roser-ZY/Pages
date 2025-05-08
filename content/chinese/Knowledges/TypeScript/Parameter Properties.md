---
title: "Parameter Properties"
author: "Roser"
date: 2025-02-08
image: "images/content/TypeScript.png"
draft: false
tags:
  - TypeScript
  - OOP
---
TS 提供了一个特殊语法，可以将构造函数 `constructor` 同名参数和值转换为类成员属性。这些属性称为 *Parameter Properties*，即参数属性。

参数属性通过提供一些可见性和可修改性前缀来声明，包括 `public/private/protected/readonly`，注意与常规属性声明不同，参数属性必须提供 `public` 如果希望该参数可见性为 `public`。

```typescript
class Params {
constructor(
public readonly x: number,
protected y: number,
private z: number
) {
// No body necessary
}
}
const a = new Params(1, 2, 3);
console.log(a.x);
```