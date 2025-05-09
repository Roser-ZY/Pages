---
title: "C++ 修改没有同步到蓝图"
author: "Roser"
date: 2025-05-09
image: "images/content/UE5.png"
draft: false
tags:
  - UE5
  - Blueprint
---
如果蓝图对某个 C++ 中设置的值做了修改，则后续 C++ 对该值的修改都不会反映到蓝图中，蓝图会被标记为已修改状态。

此时，需要对被修改的组件还原到 Defulat，才能与 C++ 的修改同步。C++ 的修改本质上修改的是默认值。

因此，每次修改了 C++ 的一些 PROPERTY 的类型或者数据，一定要手动在蓝图类中还原，否则蓝图会保留原本的