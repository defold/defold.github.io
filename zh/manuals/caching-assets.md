---
brief: 本手册解释了如何使用资源缓存来加速构建.
github: https://github.com/defold/doc
language: zh
layout: manual
title: 缓存资源
toc:
- 缓存资源
- 项目缓存
- 本地缓存
- 远程缓存
---

# 缓存资源

使用Defold创建的游戏通常在几秒钟内就能构建完成，但随着项目的增长，资源量也会增加。在大型项目中，编译字体和压缩纹理可能需要大量时间，而资源缓存的存在是为了通过只重新构建已更改的资源来加速构建，同时从缓存中使用已编译的资源来处理未更改的资源。

Defold使用三层缓存：

1. 项目缓存
2. 本地缓存
3. 远程缓存


## 项目缓存

Defold默认将编译的资源缓存在Defold项目的`build/default`文件夹中。项目缓存将加速后续构建，因为只有修改过的资源需要重新编译，而没有更改的资源将从项目缓存中使用。此缓存始终启用，编辑器和命令行工具都会使用它。

可以通过删除`build/default`中的文件或通过[命令行构建工具Bob](/zh/manuals/bob)发出`clean`命令来手动删除项目缓存。


## 本地缓存

Defold 1.2.187版本新增

本地缓存是一个可选的第二层缓存，其中编译的资源存储在同一台机器上的外部文件位置或网络驱动器上。由于其外部位置，缓存内容在清理项目缓存后仍然存在。它也可以由在同一项目上工作的多个开发人员共享。该缓存目前仅在使用命令行工具构建时可用。它通过`resource-cache-local`选项启用：

```sh
java -jar bob.jar --resource-cache-local /Users/john.doe/defold_local_cache
```

从本地缓存访问编译资源是基于计算的校验和，该校验和考虑了Defold引擎版本、源资源的名称和内容以及项目构建选项。这将保证缓存的资源是唯一的，并且缓存可以在多个Defold版本之间共享。

<div class='sidenote' markdown='1'>
存储在本地缓存中的文件将无限期存储。由开发人员手动删除旧/未使用的文件。
</div>


## 远程缓存

Defold 1.2.187版本新增

远程缓存是一个可选的第三层缓存，其中编译的资源存储在服务器上并通过HTTP请求访问。该缓存目前仅在使用命令行工具构建时可用。它通过`resource-cache-remote`选项启用：

```sh
java -jar bob.jar --resource-cache-remote http://192.168.0.100/
```

与本地缓存一样，所有资源都是基于计算的校验和从远程缓存访问的。缓存的资源通过HTTP请求方法GET、PUT和HEAD访问。Defold不提供远程缓存服务器。这取决于每个开发人员来设置它。[一个基本的Python服务器示例可以在这里看到](https://github.com/britzl/httpserver-python)。