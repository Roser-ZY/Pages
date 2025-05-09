---
title: "不要在头文件中使用 using namespace"
author: "Roser"
date: 2024-12-30
image: "images/content/C++.png"
draft: false
tags:
  - Cpp
  - EffectiveCpp
---
虽然 `using` 有[作用域](../using-作用域)限制，但不建议将 `using namespace` 用于头文件，而是应该放在源文件中，避免项目规模扩大时，出现命名冲突问题。 