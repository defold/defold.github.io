## 九宫格纹理

GUI 框节点和精灵组件有时会包含对其大小敏感的元素：需要调整大小以适应所包含内容的面板和对话框，或者需要调整大小以显示敌人剩余生命值的生命条。当您将纹理应用到调整大小后的节点或精灵时，这些可能会导致视觉问题。

通常，引擎会将纹理缩放以适应矩形边界，但通过定义九宫格边缘区域，可以限制纹理中应该缩放的部分：

![GUI 缩放](/shared/images/gui_slice9_scaling.png)

*九宫格* 框节点由 4 个数字组成，指定左、上、右和下边缘不应常规缩放的像素数：

![九宫格属性](/shared/images/gui_slice9_properties.png)

边缘是顺时针设置的，从左边缘开始：

![九宫格部分](/shared/images/gui_slice9.png)

- 角落部分从不缩放。
- 边缘部分沿单个轴缩放。左右边缘部分垂直缩放。上下边缘部分水平缩放。
- 中央纹理区域根据需要水平和垂直缩放。

上述 *九宫格* 纹理缩放仅在您更改框节点或精灵的大小时应用：

![GUI 框节点大小](/shared/images/gui_slice9_size.png)

![精灵大小](/shared/images/sprite_slice9_size.png)

<div class='important' markdown='1'>
如果您更改框节点或精灵的缩放参数（或游戏对象上的缩放参数）- 节点或精灵以及纹理将被缩放而不应用 *九宫格* 参数。
</div>

<div class='important' markdown='1'>
在精灵上使用九宫格纹理时，[图像的精灵修剪模式](https://defold.com/manuals/atlas/#image-properties)必须设置为关闭。
</div>


### Mipmap 和九宫格
由于渲染器中 mipmap 的工作方式，纹理段的缩放有时可能会出现伪影。当您将纹理段 _缩小_ 到原始纹理大小以下时会发生这种情况。然后渲染器为该段选择较低分辨率的 mipmap，导致视觉伪影。

![九宫格 mipmap](/shared/images/gui_slice9_mipmap.png)

为避免此问题，请确保将要缩放的纹理段足够小，永远不会被缩小，只会被放大。
