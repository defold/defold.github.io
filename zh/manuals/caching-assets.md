---
brief: 跟教程介绍了如何利用资源缓存提高编译速度.
github: https://github.com/defold/doc
language: zh
layout: manual
title: 资源缓存
toc:
- 资源缓存
- 项目缓存
- 本地缓存
- 远程缓存
---

# 资源缓存

Defold 编译通常需要几秒钟, 但是随着项目和资源的扩大, 耗时也会增加. 对于大项目而言, 编译时间大量消耗在编译字体和压缩纹理上, 所以引入资源缓存功能使得再次编译时只编译改变了的资源, 那些没改变的资源直接从缓存获取以提高编译效率.

Defold 使用了三重缓存:

1. 项目缓存
2. 本地缓存
3. 原创缓存


## 项目缓存

Defold 默认把编译好的资源缓存到项目的 `build/default` 文件夹中. 下次编译时只编译改变了的资源, 未改变的资源从项目缓存中获取. 这种缓存在编辑器和命令行都会开启.

可以手动删除项目目录下 `build/default` 中的文件, 或者使用 [命令行编译工具 Bob](/zh/manuals/bob) 的 `clean` 命令, 达到清除项目缓存的目的.


## 本地缓存

自 Defold 1.2.187 版本引入

本地缓存作为可选功能, 把编译后的资源保存在本机或者云盘上. 这相当于是项目缓存的备份. 本地缓存还可以供项目的合作开发人员共享. 目前该缓存只能使用命令行工具开启. 即命令行参数 `resource-cache-local` 项:

```sh
java -jar bob.jar --resource-cache-local /Users/john.doe/defold_local_cache
```

本地缓存通过基于 Defold 引擎版本, 资源文件, 项目编译参数等计算出的校验码进行访问. 这样做就能保证不同 Defold 版本之间资源缓存的唯一性.

<div class='sidenote' markdown='1'>
本地缓存文件永远存在. 想要清除只能手动删除这些文件.
</div>


## 远程缓存

自 Defold 1.2.187 版本引入

远程缓存作为可选功能, 把编译后的资源保存至服务器然后通过 HTTP 请求进行访问. 目前该缓存只能使用命令行工具开启. 即命令行参数 `resource-cache-remote` 项:

```sh
java -jar bob.jar --resource-cache-remote https://http://192.168.0.100/
```

远程缓存同样通过校验码进行访问. 使用 HTTP 请求的 GET, PUT 方法和 HEAD 获取缓存文件. Defold 不提供远程服务器程序. 开发者可以自行搭建. 比如 [这个使用 Python 做的简单的服务器程序](https://github.com/britzl/httpserver-python).