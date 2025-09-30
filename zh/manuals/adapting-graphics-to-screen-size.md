---
brief: 本手册解释了如何将游戏和图形适配到不同的屏幕尺寸。
github: https://github.com/defold/doc
language: zh
layout: manual
title: 适配图形以适应不同屏幕尺寸
toc:
- 引言
- 如何更改内容渲染方式
- 复古/8位图形
- 高分辨率图形
- 高DPI设置和视网膜屏幕
- 创建自适应GUI
- 节点属性
- 布局
- 测试不同的屏幕尺寸
---

# 引言

在将游戏和图形适配到不同屏幕尺寸时，需要考虑几个方面：

* 这是一款具有低分辨率像素完美图形的复古游戏，还是具有高清质量图形的现代游戏？
* 在不同屏幕尺寸上以全屏模式玩游戏时，游戏应如何表现？
  * 玩家应该在高分辨率屏幕上看到更多游戏内容，还是图形应该自适应缩放以始终显示相同内容？
* 游戏应如何处理与您在 *game.project* 中设置的宽高比不同的宽高比？
  * 玩家应该看到更多游戏内容？或者应该有黑边？或者调整大小的GUI元素？
* 您需要什么类型的菜单和屏幕GUI组件，它们应如何适应不同的屏幕尺寸和屏幕方向？
  * 当方向改变时，菜单和其他GUI组件是否应该改变布局，还是无论方向如何都保持相同布局？

本手册将解决其中一些问题并提出最佳实践。


## 如何更改内容渲染方式

Defold渲染脚本为您提供了对整个渲染管道的完全控制。渲染脚本决定了绘制顺序以及绘制内容和方式。渲染脚本的默认行为是始终绘制由*game.project*文件中的宽度和高度定义的相同像素区域，无论窗口是否调整大小或实际屏幕分辨率是否匹配。如果宽高比改变，这将导致内容被拉伸，如果窗口大小改变，内容将被放大或缩小。在某些游戏中，这可能是可以接受的，但更有可能的是，如果屏幕分辨率或宽高比不同，您希望显示更多或更少的游戏内容，或者至少确保在不改变宽高比的情况下缩放内容。默认的拉伸行为可以轻松更改，您可以阅读[渲染手册](https://www.defold.com/zh/manuals/render/#default-view-projection)了解更多关于如何执行此操作的信息。


## 复古/8位图形

复古/8位图形通常指模拟老式游戏机或计算机图形风格的游戏，具有低分辨率和有限的调色板。例如，任天堂娱乐系统（NES）的屏幕分辨率为256x240，Commodore 64为320x200，Gameboy为160x144，这些都只是现代屏幕尺寸的一小部分。为了使模拟这种图形风格和屏幕分辨率的游戏在现代高分辨率屏幕上可玩，图形必须被放大或缩放数次。实现这一点的一个简单方法是，以您希望模拟的低分辨率和风格绘制所有图形，并在渲染时缩放图形。这可以在Defold中使用渲染脚本和[固定投影](/zh/manuals/render/#fixed-projection)设置为合适的缩放值轻松实现。

让我们使用这个图块集和玩家角色（[来源](https://ansimuz.itch.io/grotto-escape-game-art-pack)）来制作一个分辨率为320x200的8位复古游戏：

![](/manuals/images/screen_size/retro-player.png)

![](/manuals/images/screen_size/retro-tiles.png)

在*game.project*文件中设置320x200并启动游戏，看起来会是这样：

![](/manuals/images/screen_size/retro-original_320x200.png)

在现代高分辨率屏幕上，这个窗口绝对太小了！将窗口大小增加到四倍到1280x800，使其更适合现代屏幕：

![](/manuals/images/screen_size/retro-original_1280x800.png)

现在窗口大小更合理了，我们还需要对图形做一些处理。它太小了，很难看清游戏中发生的事情。我们可以使用渲染脚本来设置固定和缩放的投影：

```Lua
msg.post("@render:", "use_fixed_projection", { zoom = 4 })
```

<div class='sidenote' markdown='1'>
相同的结果也可以通过将[相机组件](/zh/manuals/camera/)附加到游戏对象并勾选*正交投影*，将*正交缩放*设置为4.0来实现：

![](/manuals/images/screen_size/retro-camera_zoom.png)
</div>

这将产生以下结果：

![](/manuals/images/screen_size/retro-zoomed_1280x800.png)

这样更好。窗口和图形都有合适的大小，但如果我们仔细观察，会发现一个明显的问题：

![](/manuals/images/screen_size/retro-zoomed_linear.png)

图形看起来模糊了！这是由GPU渲染时从纹理中采样放大的图形的方式引起的。*game.project*文件中Graphics部分下的默认设置是*linear*：

![](/manuals/images/screen_size/retro-settings_linear.png)

将其更改为*nearest*将得到我们想要的结果：

![](/manuals/images/screen_size/retro-settings_nearest.png)

![](/manuals/images/screen_size/retro-zoomed_nearest.png)

现在我们的复古游戏有了清晰的像素完美图形。还有更多事情需要考虑，例如在*game.project*中禁用精灵的子像素：

![](/manuals/images/screen_size/retro-subpixels.png)

当子像素选项被禁用时，精灵将永远不会在半个像素上渲染，而是始终对齐到最近的完整像素。

## 高分辨率图形

处理高分辨率图形时，我们需要采用与复古/8位图形不同的项目设置和内容设置方法。对于位图图形，您需要以这样的方式创建内容，使其在高分辨率屏幕上以1:1比例显示时看起来良好。

就像复古/8位图形一样，您需要更改渲染脚本。在这种情况下，您希望图形随屏幕尺寸缩放，同时保持原始宽高比：

```Lua
msg.post("@render:", "use_fixed_fit_projection")
```

这将确保屏幕将调整大小以始终显示与*game.project*文件中指定的相同数量的内容，可能会根据宽高比是否不同而在上方和下方或两侧显示额外内容。

您应该在*game.project*文件中将宽度和高度配置为允许您在不缩放的情况下显示游戏内容的尺寸。

### 高DPI设置和视网膜屏幕

如果您还希望支持高分辨率的视网膜屏幕，可以在*game.project*文件的Display部分启用此功能：

![](/manuals/images/screen_size/highdpi-enabled.png)

这将在支持高DPI的显示器上创建高DPI的后台缓冲区。游戏将以宽度和高度设置中设置的双倍分辨率渲染，这些设置仍将是脚本和属性中使用的逻辑分辨率。这意味着所有测量值保持不变，任何以1x比例渲染的内容看起来都一样。但是，如果您导入高分辨率图像并将它们缩放到0.5x，它们在屏幕上将是高DPI的。


## 创建自适应GUI

创建GUI组件的系统围绕许多基本构建块或[节点](/zh/manuals/gui/#node-types)构建，虽然看起来可能过于简单，但它可以用来创建从按钮到复杂菜单和弹出窗口的任何内容。您创建的GUI可以配置为自动适应屏幕尺寸和方向的变化。例如，您可以将节点锚定在屏幕的顶部、底部或侧面，节点可以保持其大小或拉伸。节点之间的关系以及它们的大小和外观也可以配置为在屏幕尺寸或方向变化时发生变化。

### 节点属性

GUI中的每个节点都有一个枢轴点、水平和垂直锚点以及调整模式。

* 枢轴点定义节点的中心点。
* 锚点模式控制当场景边界或父节点边界被拉伸以适应物理屏幕大小时，节点的垂直和水平位置如何改变。
* 调整模式设置控制当场景边界或父节点边界被调整以适应物理屏幕大小时，节点会发生什么变化。

您可以在[GUI手册](/zh/manuals/gui/#node-properties)中了解更多关于这些属性的信息。

### 布局

Defold支持GUI在移动设备上自动适应屏幕方向变化。通过使用此功能，您可以设计一个能够适应一系列屏幕尺寸的方向和宽高比的GUI。也可以创建匹配特定设备型号的布局。您可以在[GUI布局手册](/zh/manuals/gui-layouts/)中了解更多关于此系统的信息。


## 测试不同的屏幕尺寸

调试菜单包含一个选项，用于模拟特定设备型号分辨率或自定义分辨率。当应用程序运行时，您可以选择<kbd>Debug->Simulate Resolution</kbd>并从列表中选择一个设备型号。运行的应用程序窗口将调整大小，您将能够看到您的游戏在不同分辨率或不同宽高比下的外观。

![](/manuals/images/screen_size/simulate-resolution.png)