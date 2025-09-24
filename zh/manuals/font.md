---
brief: 本手册描述了 Defold 如何处理字体以及如何在游戏中将字体显示在屏幕上。
github: https://github.com/defold/doc
language: zh
layout: manual
title: Defold 处理字体手册
toc:
- 字体文件
- 创建字体
- 属性
- 距离场字体
- 位图BMFonts
- 伪影和最佳实践
- 字体缓存
- 运行时生成
- 预热字形缓存
- 字体脚本
---

# 字体文件

字体用于在标签组件和GUI文本节点上渲染文本。Defold支持多种字体文件格式：

- TrueType
- OpenType
- BMFont

添加到项目中的字体会自动转换为Defold可以渲染的纹理格式。有两种字体渲染技术可用，每种都有其特定的优点和缺点：

- 位图
- 距离场

## 创建字体

要在Defold中创建字体，请从菜单中选择<kbd>文件 ▸ 新建...</kbd>，然后选择<kbd>字体</kbd>。您也可以在*资源*浏览器中<kbd>右键点击</kbd>一个位置，然后选择<kbd>新建... ▸ 字体</kbd>。

![New font name](/manuals/images/font/new_font_name.png)

给新字体文件命名并点击<kbd>确定</kbd>。新字体文件现在在编辑器中打开。

![New font](/manuals/images/font/new_font.png)

将您想要使用的字体拖放到*资源*浏览器中，并将其放在合适的位置。

将*字体*属性设置为您想要使用的字体文件，并根据需要设置字体属性。

## 属性

*字体*
: 用于生成字体数据的TTF、OTF或*`.fnt`*文件。

*材质*
: 渲染此字体时使用的材质。确保为距离场和BMFonts更改此材质（详见下文）。

*输出格式*
: 生成的字体数据类型。

  - `TYPE_BITMAP` 将导入的OTF或TTF文件转换为字体表纹理，其中位图数据用于渲染文本节点。颜色通道用于编码字体形状、轮廓和阴影。对于*`.fnt`*文件，直接使用源纹理位图。
  - `TYPE_DISTANCE_FIELD` 导入的字体被转换为字体表纹理，其中像素数据表示的不是屏幕像素，而是到字体边缘的距离。详见下文。

*渲染模式*
: 用于字形渲染的渲染模式。

  - `MODE_SINGLE_LAYER` 为每个字符生成一个四边形。
  - `MODE_MULTI_LAYER` 分别为字形形状、轮廓和阴影生成单独的四边形。层按从后到前的顺序渲染，这可以防止字符在轮廓比字形之间的距离更宽时遮挡先前渲染的字符。此渲染模式还支持通过字体资源中的阴影X/Y属性指定的正确阴影偏移。

*大小*
: 字形的目标大小，以像素为单位。

*抗锯齿*
: 字体在烘焙到目标位图时是否应该抗锯齿。如果您想要像素完美的字体渲染，请设置为0。

*透明度*
: 字形的透明度。0.0--1.0，其中0.0表示透明，1.0表示不透明。

*轮廓透明度*
: 生成的轮廓的透明度。0.0--1.0。

*轮廓宽度*
: 生成的轮廓的宽度，以像素为单位。设置为0表示无轮廓。

*阴影透明度*
: 生成的阴影的透明度。0.0--1.0。

<div class='sidenote' markdown='1'>
阴影支持由内置字体材质着色器启用，并处理单层和多层渲染模式。如果您不需要分层字体渲染或阴影支持，最好使用更简单的着色器，如*`builtins/font-singlelayer.fp`*。
</div>

*阴影模糊*
: 对于位图字体，此设置表示将小模糊核应用于每个字体字形的次数。对于距离场字体，此设置等于模糊的实际像素宽度。

*阴影X/Y*
: 生成的阴影的水平和垂直偏移，以像素为单位。此设置仅在渲染模式设置为`MODE_MULTI_LAYER`时才会影响字形阴影。

*字符*
: 字体中包含哪些字符。默认情况下，此字段包含ASCII可打印字符（字符代码32-126）。您可以从此字段添加或删除字符，以在字体中包含更多或更少的字符。

<div class='sidenote' markdown='1'>
ASCII可打印字符是：
space ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ \` a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~
</div>

*所有字符*
: 如果您选中此属性，源文件中所有可用的字形都将包含在输出中。

*缓存宽度/高度*
: 限制字形缓存位图的大小。当引擎渲染文本时，它从缓存位图中查找字形。如果它不存在于缓存位图中，它将在渲染之前添加到缓存中。如果缓存位图太小而无法包含引擎被要求渲染的所有字形，则会发出错误信号（`ERROR:RENDER: Out of available cache cells! Consider increasing cache_width or cache_height for the font.`）。

  如果设置为0，缓存大小将自动设置，最大增长到2048x4096。

## 距离场字体

距离场字体在纹理中存储到字形边缘的距离，而不是位图数据。当引擎渲染字体时，需要特殊的着色器来解释距离数据并使用它来绘制字形。距离场字体比位图字体更消耗资源，但允许更大的尺寸灵活性。

![Distance field font](/manuals/images/font/df_font.png)

确保在创建字体时将字体的*材质*属性更改为*`builtins/fonts/font-df.material`*（或任何其他可以处理距离场数据的材质）---否则字体在渲染到屏幕时将不会使用正确的着色器。

## 位图BMFonts

除了生成的位图外，Defold还支持预烘焙的位图"BMFont"格式字体。这些字体由包含所有字形的PNG字体表组成。此外，*`.fnt`*文件包含有关在表上可以找到每个字形的位置以及大小和字距调整信息的信息。（请注意，Defold不支持Phaser和其他一些工具使用的*`.fnt`*格式的XML版本）

这些类型的字体与从TrueType或OpenType字体文件生成的位图字体相比没有性能改进，但可以在图像中直接包含任意图形、颜色和阴影。

将生成的*`.fnt`*和*`.png`*文件添加到您的Defold项目中。这些文件应该位于同一文件夹中。创建一个新的字体文件，并将*字体*属性设置为*`.fnt`*文件。确保*output_format*设置为`TYPE_BITMAP`。Defold不会生成位图，而是使用PNG中提供的位图。

<div class='sidenote' markdown='1'>
要创建BMFont，您需要使用能够生成适当文件的工具。存在几个选项：

* [Bitmap Font Generator](http://www.angelcode.com/products/bmfont/)，AngelCode提供的仅限Windows的工具。
* [Shoebox](http://renderhjs.net/shoebox/)，免费的基于Adobe Air的应用程序，适用于Windows和macOS。
* [Hiero](https://libgdx.com/wiki/tools/hiero)，基于Java的开源工具。
* [Glyph Designer](https://71squared.com/glyphdesigner)，71 Squared的商业macOS工具。
* [bmGlyph](https://www.bmglyph.com)，Sovapps的商业macOS工具。
</div>

![BMfont](/manuals/images/font/bm_font.png)

为了使字体正确渲染，不要忘记在创建字体时将材质属性设置为*`builtins/fonts/font-fnt.material`*。

## 伪影和最佳实践

通常，当字体在没有缩放的情况下渲染时，位图字体是最好的。它们比距离场字体渲染到屏幕的速度更快。

距离场字体对放大效果非常好。另一方面，位图字体只是像素化图像，随着字体缩放，大小会增加，像素会增长，导致块状伪影。以下是字体大小48像素，放大4倍的示例：

![Fonts scaled up](/manuals/images/font/scale_up.png)

缩小时，位图纹理可以被GPU很好地有效地缩小和抗锯齿。位图字体比距离场字体更好地保持其颜色。以下是相同示例字体在48像素大小下的放大视图，缩小到原始大小的1/5：

![Fonts scaled down](/manuals/images/font/scale_down.png)

距离场字体需要渲染到足够大的目标大小，以保存能够表达字体字形曲线的距离信息。这是与上面相同的字体，但在18像素大小下放大10倍。很明显，这太小而无法编码这种字体的形状：

![Distance field artifacts](/manuals/images/font/df_artifacts.png)

如果您不需要阴影或轮廓支持，请将它们各自的alpha值设置为零。否则，阴影和轮廓数据仍将生成，占用不必要的内存。

## 字体缓存
Defold中的字体资源在运行时会产生两个东西，一个纹理和字体数据。

* 字体数据由字形条目列表组成，每个条目包含一些基本的字距调整信息和该字形的位图数据。
* 纹理在内部称为"字形缓存纹理"，它将在为特定字体渲染文本时使用。

在运行时渲染文本时，引擎将首先循环遍历要渲染的字形，以检查纹理缓存中有哪些字形可用。字形纹理缓存中缺少的每个字形都将触发从字体数据中存储的位图数据进行纹理上传。

每个字形根据字体基线在内部放置在缓存中，这使得能够在着色器中计算字形在其相应缓存单元内的局部纹理坐标。这意味着您可以动态实现某些文本效果，如渐变或纹理叠加。引擎通过一个名为`texture_size_recip`的特殊着色器常量将缓存的度量标准暴露给着色器，该常量在向量组件中包含以下信息：

* `texture_size_recip.x` 是缓存宽度的倒数
* `texture_size_recip.y` 是缓存高度的倒数
* `texture_size_recip.z` 是缓存单元宽度与缓存宽度的比率
* `texture_size_recip.w` 是缓存单元高度与缓存高度的比率

例如 - 要在着色器片段中生成渐变，只需编写：

`float horizontal_gradient = fract(var_texcoord0.y / texture_size_recip.w);`

有关着色器uniform的更多信息，请参阅[着色器手册](/zh/manuals/shader)。

## 运行时生成

可以对SDF类型字体使用运行时生成，当使用TrueType (.ttf)字体时。
这种方法可以大大减少Defold游戏的下载大小和运行时内存消耗。
小小的缺点是为每个在运行时生成的字形会有非常小的延迟。

通过设置`font.runtime_generation`在game.project中启用此功能。

<div class='sidenote' markdown='1'>
此功能目前是实验性的，但打算在未来用作默认工作流程。
</div>

<div class='important' markdown='1'>
此设置影响项目中的所有.ttf字体。
</div>

### 预热字形缓存

为了使运行时字体更易于使用，它们支持预热字形缓存。
这意味着字体将生成字体中列出的*字符*中的字形。

<div class='sidenote' markdown='1'>
如果选择了`所有字符`，将不会有预热，因为这违背了不必同时生成所有字形的目的。
</div>

### 字体脚本

对于运行时字体，可以添加或删除子字体。
当大字体已被拆分为多个文件用于不同字符集时（例如CJK），这很有用。

<div class='important' markdown='1'>
添加子字体不会自动加载或渲染所有字形。
</div>

```lua
-- 将范围A-Z添加到.fontc
local font_hash = hash("/assets/fonts/roboto.fontc")
local ttf_hash = hash("/assets/fonts/Roboto/Roboto-Bold.ttf")
local codepoint_min = 0x00000041 -- A
local codepoint_max = 0x0000005A -- Z
font.add_source(font_hash, ttf_hash, codepoint_min, codepoint_max)
```

```lua
-- 删除关联的ttf资源
local font_hash = hash("/assets/fonts/roboto.fontc")
local ttf_hash = hash("/assets/fonts/Roboto/Roboto-Bold.ttf")
font.remove_source(font_hash, ttf_hash)
```

要将字形加载到字体中，您需要调用`font.add_glyphs()`。
这是一个异步操作，一旦完成，就可以安全地继续显示包含字形的任何消息。

```lua
local function add_glyph_callback(self, id, result, errmsg)
  if not result then
    print("Request " .. id .." finished with error:", errmsg)
  else
    msg.post(some_url, "show_dialog")
  end
end

-- 将字形加载到字体中
local font_hash = hash("/assets/fonts/roboto.fontc")
local glyphs = "Some text to be shown!" -- 为了最佳性能，使其成为唯一字形列表
local request_id = font.add_glyphs(font_hash, ttf_hash, add_glyph_callback)
```

而且，当不再需要字符时，您可以丢弃该内存：
```lua
-- 删除关联的ttf资源
local font_hash = hash("/assets/fonts/roboto.fontc")
font.remove_glyphs(font_hash, "All the characters in the set")
```