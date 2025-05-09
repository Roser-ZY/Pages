---
title: "Actor 生命周期触发函数及功能"
author: "Roser"
date: 2025-04-23
image: "images/content/UE5.png"
draft: false
tags:
  - UE5
draft: true
---
下表按照 [Actor 生命周期](../../Basic/Actor-生命周期)调用顺序排列，只是大概列一下，没有区分具体路径：

| 函数名                                       | 功能描述                                                                                       | 编码频率 |
| ----------------------------------------- | ------------------------------------------------------------------------------------------ | ---- |
| `AActor::Constructor()`                   | 构造函数，创建时调用，此时世界尚未存在，不能访问其他 Actor。<br>构造函数在编辑和运行期间可能会多次调用，不建议在构造函数中执行复杂操作，最多就是属性初始化和默认值设置等。 | 常用   |
| `PostInitProperties()`                    | 初始化完 `UPROPERTY` 后调用，可以用于初始化逻辑，但不建议写复杂代码。                                                  | 不常用  |
| `OnConstruction(const Transform&)`        | 核心**编辑器构建函数**，在放置、修改属性、移动位置、重编译蓝图时都会执行，用于根据属性生成组件、子 Actor 等。                               | 非常常用 |
| `PostEditMove()`                          | 拖动、移动 Actor 时调用，用于限制位置，自动对齐等逻辑。                                                            | 不常用  |
| `CheckForErrors()`                        | 用于构建时的报错检查，输出警告或错误消息到编辑器。                                                                  | 不常用  |
| `EditorApplyTranslation/Rotation/Scale()` | 编辑器拖动 Actor 时变换操作回调（尽在特定自定义行为时使用）                                                          | 极不常用 |
