---
image: "images/content/C++.png"
draft: false
date: 2025-04-14
tags:
  - Cpp
  - EffectiveCpp
  - Review
title: 条款02：尽量使用 const，enum，inline 代替 define 宏
author: Roser Han
---
`#define` 是预处理指令，编译器会在预处理时将其替换，相应的符号不会添加到符号表。在 C++ 中不建议使用 `#define`。

- 使用 `const` 和 `constexpr` 来声明常量。
- 借助 `enum` 来声明常量。
- 使用 `inline` 函数代替宏函数。e
### `enum` 声明常量

使用 `const` 声明的常量虽然不可变，但编译器不会在编译期确定值，因此无法用于指定数组大小。这种情况下，可以使用 `enum` 来声明常量，此类常量可在编译期确定值。

 > 个人理解：C++11 之后，有了 `constexpr`，完全可以代替 `enum` 的方式。
 
```cpp
class GamePlayer{
private:
	enum {NumTurns = 5};
	int scores[NumTurns];
} 
```

这种方式会与 `#define` 很接近，因为也无法对 `enum` 取地址，通常可以用来约束禁用取地址。

另外很多代码都会用到这个技巧，需要知道。甚至在模板元编程中，enum hack 的技术是基础。
### `inline` 代替宏函数

`inline` 是一个比较强大的语言特性，关于它需要有很多篇幅详细介绍。这里只需要知道它的其中一个用途，就是能够保留函数特性的基础上，实现与 `#define` 宏函数类似的效果，即代码替换。

但是这种代码替换是不确定的，真正是否进行替换由编译器决定。例如 `inline` 函数如果出现递归，则实际编译后不会对其进行展开。