---
title: "static 成员在继承中的表现"
author: "Roser"
date: 2025-05-09
image: "images/content/C++.png"
draft: false
tags:
  - Cpp
  - OOP
---
父类定义的 static 成员，在所有子类中都是共享的。

如果子类重新定义了 static 成员，则该成员会隐藏父类的成员，并且其派生类共享这个新的 static 成员，可以通过显式访问父类的 static 成员来访问被隐藏的父类成员。