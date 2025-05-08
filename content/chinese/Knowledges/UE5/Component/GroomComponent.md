---
title: "GroomComponent"
author: "Roser"
date: 2025-04-24
image: "images/content/UE5.png"
draft: false
tags:
  - UE5
draft: true
---
必须绑定到 Mesh Component 上，一般是 `USkeletalMeshComponent`，使得毛发能与骨骼绑定。

如果绑定到骨骼，**必须指定 `AttachmentName`**，该名称为骨骼的 Socket 名称。如果不绑定，会导致 Groom Component 绑定没有绑定到骨骼插槽，可能会导致错误的显示效果，并且不会跟随骨骼动画。