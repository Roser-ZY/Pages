---
title: "Tree Shaking"
author: "Roser"
date: 2025-02-08
image: "images/content/Webpack.png"
draft: false
tags:
  - Webpack
  - Dependency
  - Optimization
---
Tree Shaking 是一种代码优化技术，用于移除 JS/TS 未使用的代码（即死代码，包括已导入但未使用的代码）。常见于模块化开发，例如 ES6 的 `import/export`，通过静态分析代码的依赖关系，将未被实际使用的部分从打包的结果中剔除。

Tree Shaking 优化针对的是顶层执行部分，例如全局变量，函数调用等，对于类定义不会走 Tree Shaking 优化，因为该类定义没有使用过，从一开始就不会被 Webpack 添加到依赖图中。

> 注意
> Tree Shaking 优化的是死代码已经建立模块依赖的内容，如果某个模块的代码并没有进入依赖图（例如没有 `import` 过），则从一开始就不会被 Webpack 考虑，更不会走 Tree Shaking 优化。
> 这一点需要注意，必须是已经通过 `import` 建立依赖关系后才会被 Webpack 识别。

由于这项技术使用的是静态分析，因此当使用 TS 中使用[多态](../../TypeScript/多态)时，可能会导致一些类被误检测为死代码从而被踢出。这就会导致运行时出现类继承关系错误或多态失效的问题。

为了解决上面的问题，必须进行以下两步操作（有先后顺序）：
1. 在依赖链中引入需要的类（例如在某个文件里导入需要的这些类），使得静态分析时建立依赖关系，从而避免优化。
2. 在 `package.json` 中添加 `sideEffects: ["*.ts"]` 标记有副作用的文件。
	- 或者在 Webpack 配置文件中为特定规则启用 `sideEffects`，避免被 Tree Shaking 优化，这两个方法是相同的原理。

或者改成动态导入，动态导入不会被 Tree Shaking 优化。

Tree Shaking 不会优化被标记有副作用（Side Effects）的文件进行优化，也就是说，只要 `import` 导入了，即使没有使用导入的内容，也不会被优化。