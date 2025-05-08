---
title: "using 作用域"
author: "Roser"
date: 2024-12-30
image: "images/content/C++.png"
draft: false
tags:
  - Cpp
---
`using` 可以在类中使用，从而将该 `using` 语句限定在类作用域。

`using` 类型别名，会被类的访问控制符限制，例如 `using StringVector = std::vector<string>;` 如果是 `private`，则只有该类的成员才能访问该别名。如果是 `public`，则外部可以通过类名限定作用域来访问该别名。

`using namdspace` 则不会被类的访问控制符限制，例如 `using namespace std;` 或 `using std::vector;` 都不会受访问控制符限制，但他们的作用域仅限用于类内部。