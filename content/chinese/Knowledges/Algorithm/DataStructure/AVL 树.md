---
title: "AVL 树"
author: "Roser"
date: 2025-05-09
image: "images/content/Algorithm.png"
draft: false
tags:
  - DataStructure
  - Tree
  - Todo
---
AVL 树是**一种**平衡二叉搜索树， 1962 年 G. M. Adelson-Velsky 和 E. M. Landis 在论文 *“An algorithm for the organization of information”* 提出。

普通的二叉搜索树经过多次插入和删除操作后，可能会退化为链表，此时所有操作的时间复杂度从 $O(log\ n)$ 退化为 $O(n)$。AVL 树在经过一些列操作后不会退化，能够始终保持各种操作的时间复杂度保持 $O(log\ n)$，在需要频繁增删改的场景中，AVL 树能够保持高效的操作性能。

需要注意，AVL 树是对平衡二叉搜索树的一种实现，平衡二叉搜索树是一个广义的概念。

其他比较常见的平衡二叉搜索树还有红黑树。