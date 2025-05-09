---
title: "static 成员在继承中的表现"
author: "Roser"
date: 2025-01-08
image: "images/content/TypeScript.png"
draft: false
tags:
  - TypeScript
  - OOP
---
父类的 static 成员，在子类可以继承，但不共享。

每个子类都会管理自己的 static 成员，通过子类修改该静态成员不会影响父类和其他子类中该静态成员。

相当于 [C++](../../../C++/static-成员在继承中的表现) 每个派生类都重新定义了 static 成员并隐藏了父类的同名静态成员。