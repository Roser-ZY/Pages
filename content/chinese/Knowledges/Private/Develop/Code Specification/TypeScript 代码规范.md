---
tags:
  - CodeSpecification
  - TypeScript
---

| 修改日期 | 修改内容 |
| ---- | ---- |
|      |      |
# 源文件组织结构

代码文件应按顺序包含：

1. Copyright 信息，如果有；
2. 使用 `@fileoverview` 标记的 JSDoc 信息，如果有；
3. 导入模块，如果有；
4. 文件实现。

上述每一部分都应该**由一个且仅一个空行**分隔。
## JSDoc 信息

```typescript
/**
 * @fileoverview Description of file. Lorem ipsum dolor sit amet, consectetur
 * adipiscing elit, sed do eiusmod tempor incididunt.
 */
```
## Imports

导入的所有格式都可以使用的，但是如果模块是同一个项目内的，则文件路径必须采用**相对路径**。

**禁止使用 `require()` 导入模块！！！**

## Exports

所有导出代码**只允许使用名称导出**，不允许使用**默认导出（Default Exports）**。这可以保证所有的导入都有统一的格式。

因为默认导出不提供规范名称，因此会降低代码可读性，并且默认导出可能会产生非常难以察觉的问题。名称导出可以保证后续导入一定是某个模块已经导出的名称。

导出时，要控制导出数量，因为未导出的名称仅在模块内可见，因此一定程度上可以减少耦合的可能性。

**不要多次导出！！！**

### 命名空间容器类

不要为了**命名空间**而创建只有静态方法和属性的容器类。

```typescript
// Bad.
export class Container {
  static FOO = 1;
  static bar() { return 1; }
}
```

模块（文件）本身已经提供了命名空间的功能，直接导出这些方法和属性即可。

```typescript
export const FOO = 1;
export function bar() { return 1; }
```

此外，组织代码时，禁止使用 `namespace`，正如前面所说，`module` 已经包含了命名空间的功能，`namespace` 只可能在使用外部接口，第三方库时出现。
# 语言特性

本节讨论某些语言特性是否应该使用，以及一些使用时的额外限制。

本节没有讨论的语言特性即为不推荐使用的特性。
## 本地变量声明

总是使用 `const` 和 `let` 声明变量，默认情况下总是使用 `const`，除非变量会被重新赋值。

禁止使用 `var` 声明变量，因为 `var` 声明变量的作用域比较复杂，很可能导致问题。

每个变量应该有单独的声明语句，不要在一行声明多个变量。
## Array

不要使用 `Array` 构造函数，不论是否使用 `new` 构造。因为构造函数有一些重载，会导致可读性下降。

总是使用方括号形式初始化数组，或者使用 `Array.from` 初始化数组。

不要在数组上定义或使用任何**非数字属性***（`length` 除外），使用 `Map` 或 `Object` 代替。
## Object

不要使用 `Object` 构造函数，使用花括号代替。

使用 `for(... in ...)` 容易出错，因为该语句会包含原型链上的其他属性。在使用该语句时，必须对属性进行过滤，或者遍历 `Object.keys(someObj)`。

```typescript
for (const x in someObj) {
  if (!someObj.hasOwnProperty(x)) continue;
  // now x was definitely defined on someObj
}
for (const x of Object.keys(someObj)) { // note: for _of_!
  // now x was definitely defined on someObj
}
for (const [key, value] of Object.entries(someObj)) { // note: for _of_!
  // now key was definitely defined on someObj
}
```
## Class

`Class` 声明不要用分号结尾，但是包含类声明的语句要有分号结尾。

类成员方法之间的声明应该由一个空行分隔。

`toScring` 方法应该被重写，并且总是成功，永远不要有可见的副作用。
### Static 方法

禁止声明 `private static` 方法。

调用静态方法时，一定要在定义的基类上调用，不要通过对象调用静态方法。

在静态方法的实现中，不要使用 `this` 对象访问其他静态成员，而是使用类名访问。

> TS 中的静态成员是可以被重写的？
### Constructor

构造函数使用时必须带括号。

如果类的构造函数可以采用默认构造函数，不需要显式添加一个空的构造函数，即使传入参数并且调用父类构造函数（ES2015 提供了默认实现）。但是如果有参数属性，构造函数可见性修改或者参数注解，则即使构造函数体为空，也要显式声明。
### 成员

使用 `protected` 和 `private`，不需要使用 `public` 来修饰可见性。

如果变量在构造函数之外不会被修改，应当使用 `readonly` 修饰。

对于一些只能在构造时提供值的属性，使用[参数属性](../../../TypeScript/Parameter%20Properties.md)。
对于可以在声明时赋初值的属性则在声明时赋初值，而不是在构造函数中赋初值。

成员的可见性应当尽量限制。

不要直接操作 `prototype`。

## Function

优先使用函数声明而不是命名函数：

```typescript
// Good.
function foo() {
  return 42;
}

// Bad.
const foo = () => 42;
```
### 箭头函数的使用

显式函数类型注解已经存在时，可以使用箭头函数。

允许函数嵌套，并优先使用箭头函数。箭头函数建议使用 Block 形式，即使用 `{}` 作为作用域。

在传递 Callback 函数时，优先使用箭头函数。

通常不应使用箭头函数用作属性，尤其是使用 `this` 访问箭头函数属性时，因为一些 Callback 需要调用函数理解 `this` 的含义，很多时候需要绑定，但是这种情况比较难以察觉。

对于 Event Handler 来说，可以使用箭头函数作为属性，用于 Uninstall，如果不需要 Unisntall，则优先使用箭头函数。
### 默认参数

默认参数应该遵循两个原则：

- 没有副作用；
- 不要依赖其他变量（只读变量）。

### 格式要求

在函数体开头和结尾不允许出现空行。空行只会出现在函数体内部，用于分割逻辑步骤。

## 基本数据类型

### String

使用单引号，并且不要使用多行文本连接，而是使用 `+` 连接多行文本。

如果字符串存在单引号，或者有很多转义字符，使用模板语法。
## 控制语句

控制语句的左花括号 `{` 应该与控制语句在同一行，`}` 单独一行。
## 异常处理

优先使用异常处理，而不是其他形式错误处理。

总是使用 `new Error()` 来实例化错误信息，如果需要 Reject a Promise，则可以派生 Error 并在派生类上提供 `reject()` 方法实现。

捕获异常时，应该假设所有的错误都继承自 `Error`，其他非继承自 `Error` 的错误异常信息应当继续向外抛出，除非当前处理函数认识该错误。

减少在 `try` 中的无效语句，让每个块更专注于特定的工作。
## Switch 语句

每个 `case` 必须包含 `break` 或 `return` 或抛出异常，不允许粘连多个非空 `case`。
## 相等比较

总是使用 `===/!==` 来作比较。

> 如果是比较 `null` 和 `undefined`，则可以使用 `==/!=`。
## 类型和非空断言

对于不确定的外部对象，不要使用类型和非空断言（`a as Type` 和 `y!`），而是通过 `instance of` 和空值判断来代替。

对于能够完全确定正确的对象，则可以使用。

类型断言必须使用 `as`。

对于对象签名，使用类型标注（`: Foo`）而不是类型断言（`as Foo`）。