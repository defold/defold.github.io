---
brief: 本手册介绍了如何导入模型组件使用的3D模型。
github: https://github.com/defold/doc
language: zh
layout: manual
title: Defold模型导入
toc:
- 导入3D模型
- 导入到Defold
- 使用模型
- 导出为glTF和Collada
- 要求
- 导出纹理
- 使用Blender导出
---

# 导入3D模型
Defold目前支持GL传输格式*.glTF*和Collada*.dae*格式的模型、骨骼和动画。您可以使用Maya、3D Max、Sketchup和Blender等工具来创建和/或将3D模型转换为glTF和Collada格式。Blender是一款功能强大且流行的3D建模、动画和渲染程序。它可在Windows、macOS和Linux上运行，并可从http://www.blender.org免费下载。

![Model in Blender](/manuals/images/model/blender.png)


## 导入到Defold
要导入模型，只需将*.gltf*文件或*.dae*文件以及相应的纹理图像拖放到*Assets*面板中的某个位置。

![导入模型资源](/manuals/images/model/assets.png)


## 使用模型
将模型导入Defold后，您可以在[模型组件](/zh/manuals/model)中使用它。


## 导出为glTF和Collada
导出的*.gltf*或*.dae*文件包含构成模型的所有顶点、边和面，以及_UV坐标_（如果已定义，则表示纹理图像的哪部分映射到网格的特定部分）、骨架中的骨骼和动画数据。

* 关于多边形网格的详细描述可以在http://en.wikipedia.org/wiki/Polygon_mesh找到。

* UV坐标和UV映射在http://en.wikipedia.org/wiki/UV_mapping中有描述。

Defold对导出的动画数据施加了一些限制：

* Defold目前只支持烘焙动画。动画需要为每个关键帧的每个动画骨骼提供矩阵，而不是将位置、旋转和缩放作为单独的键。

* 动画也是线性插值的。如果您进行更高级的曲线插值，动画需要从导出器预烘焙。

* 不支持Collada中的动画剪辑。要为每个模型使用多个动画，请将它们导出到单独的*.dae*文件中，然后在Defold中将这些文件收集到一个*.animationset*文件中。


### 要求
当您导出模型时，最好知道我们还不支持所有功能。
目前glTF格式中已知的问题/不支持的功能：

* 变形目标动画
* 材质属性
* 嵌入纹理

虽然我们的目标是完全支持glTF格式，但我们还没有完全实现。
如果缺少某个功能，请在[我们的仓库](https://github.com/defold/defold/issues)中为其提出功能请求。


### 导出纹理
如果您还没有模型的纹理，可以使用Blender生成一个。您应该在从模型中移除额外材质之前执行此操作。首先选择网格及其所有顶点：

![Select all](/manuals/images/model/blender_select_all_vertices.png)

当所有顶点被选中后，您可以展开网格以获取UV布局：

![Unwrap mesh](/manuals/images/model/blender_unwrap_mesh.png)

然后您可以继续将UV布局导出为可用作纹理的图像：

![Export UV layout](/manuals/images/model/blender_export_uv_layout.png)

![Export UV layout settings](/manuals/images/model/blender_export_uv_layout_settings.png)

![Export UV layout result](/manuals/images/model/blender_export_uv_layout_result.png)


### 使用Blender导出
您使用导出菜单选项导出模型。在选择导出菜单选项之前选择模型，并勾选"Selection Only"以仅导出模型。

![Exporting using Blender](/manuals/images/model/blender_export.png)