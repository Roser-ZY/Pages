---
title: "ACID"
author: "Roser"
date: 2025-05-09
image: "images/content/Database.png"
draft: false
tags:
  - Database
  - Todo
---
ACID 是数据库事务的四个特性，分别是原子性（Atomicity），一致性（Consistency），隔离性（Isolation）和持久性（Durability）。
# Atomicity

事务是数据库操作的最小单元，事务中的所有操作要么全部成功，要么全部失败，不会出现部分执行的情况。

# Consistency

事务执行前后，数据库必须保持一致的状态，即数据库的完整性约束不会被破坏。
# Isolation

多个事务并发执行时，每个事务不会影响其他事务，数据库管理系统提供隔离级别来控制并发事务之间的相互影响。
# Durability

事务一旦提交，数据就会永久保存，即使系统崩溃，数据也不会丢失。