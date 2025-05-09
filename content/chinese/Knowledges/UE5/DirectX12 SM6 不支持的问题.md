---
title: "DirectX12 SM6 不支持的问题"
author: "Roser"
date: 2025-05-09
image: "images/content/UE5.png"
draft: false
tags:
  - UE5
  - Question
---
随便启动一个 UE5 项目，查看 `Save/XXX.log` 同名日志中关于 RHI 初始化的部分日志，查看日志报错原因。

目前遇到过的问题：
###### `DirectX Agility SDK runtime not found.`

这是由于操作系统没有安装相应的 DirectX Agility SDK，可以通过检查 `C:\Windows\system32\D3D12Core.dll` 下是否有该动态库来确认，如果没有，则需要更新 Windows 版本。

本机现在是 Windows 10 1909 18363.592，而 DirectX Agility SDK 需要 Windows 10 1909 18363.1350，并且由于 1909 不再维护，想要更新需要手动下载更新补丁。

前往 [Microsoft 下载网站](https://www.catalog.update.microsoft.com/)搜索 `KB4598298`（1350 的搜索代码），然后选择合适的版本下载即可。