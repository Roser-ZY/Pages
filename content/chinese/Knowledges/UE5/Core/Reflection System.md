---
title: "Reflection System"
author: "Roser"
date: 2025-04-23
image: "images/content/UE5.png"
draft: false
tags:
  - UE5
  - Review
draft: true
---
反射是一种能力，使得应用程序可以在运行时检查自己的状态。在 UE5 中，这是非常核心的能力，用于各方面的功能，例如序列化，垃圾回收，网络相应，蓝图/C++ 交流等。C++ 不具备反射功能，因此 UE5 有自己的一套反射系统。

代码中使用的 `UENUM()`，[PROPERTY()](../Cpp/PROPERTY().md) 等宏就是用来在头文件声明不同类型和成员，并将它们标记为需要使用反射系统。

[Unreal Property System(Reflection)](https://www.unrealengine.com/en-US/blog/unreal-property-system-reflection)