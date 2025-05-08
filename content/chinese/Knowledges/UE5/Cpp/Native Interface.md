---
title: "Native Interface"
author: "Roser"
date: 2025-04-29
image: "images/content/UE5.png"
draft: false
tags:
  - UE5
draft: true
---
普通接口的函数只能在 C++ 中重写，如果想在 Blueprint 中也可以重写，需要改为 Native Interface。

UFUNCTION(BlueprintNativeEvent) 不需要自己添加 virtual 相关。

重写的时候，需要添加 _Implementation 后缀重写（这是虚函数重写）。

调用的时候，需要调用添加 Execute_ 前缀的版本。