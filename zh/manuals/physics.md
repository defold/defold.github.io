---
brief: Defold 包含 2D 和 3D 的物理引擎. 它们可以基于牛顿物理定律模拟各种物体运动碰撞时的物理效果.
github: https://github.com/defold/doc
language: zh
layout: manual
title: Defold 中的物理系统
toc:
- 物理
- 物理模拟数量单位
- 物理循环更新
- 注意事项
---

# 物理

Defold 包含一个修改版的 [Box2D](http://www.box2d.org) 物理引擎 (版本 2.2.1) 用于模拟2D物理效果和一个 Bullet physics 引擎 (版本 2.77) 用来模拟3D物理效果. 物理引擎可以基于牛顿物理定律模拟各种 _碰撞物体_ 运动碰撞时的物理效果. 本教程介绍了物理引擎的使用方法.

Defold 中的物理相关教程如下:

* **碰撞对象** - 碰撞对象是用于使游戏物体产生物理效果的组件. 碰撞对象组件含有一系列物理属性比如重量, 摩擦和形状. 详见 [碰撞对象教程](/zh/manuals/physics-objects).
* **碰撞形状** - 碰撞对象可由多个简单形状或者一个复杂形状构成. 详见 [物理形状教程](/zh/manuals/physics-shapes).
* **碰撞组** - 碰撞对象用组划分一遍确定碰撞关系. 详见 [碰撞组教程](/zh/manuals/physics-groups).
* **碰撞消息** - 两个碰撞对象接触时引擎会自动向二者的游戏对象发送物理碰撞消息. 详见 [碰撞消息教程](/zh/manuals/physics-messages)

另外还可以向物理碰撞对象施加 **约束**, 称为 **关节**, 用以向碰撞对象进行物理约束或者力的施加. 详见 [物理关节教程](/zh/manuals/physics-joints).

还可以通过向物理世界发出射线以便了解各个物体的位置情况, 称为 **投射**. 详见 [物理投射教程](/zh/manuals/physics-ray-casts).


## 物理模拟数量单位

设计上按照牛顿物理学单位米, 千克和秒 (MKS) 的标准单位. 模拟物尺寸 0.1 到 10 米范围 (静态对象可以更大) 效果较好, 默认一像素 (pixel) 当作 1 米. 这种转换比例是物理模拟器层次上的, 对游戏来说并不适用.
默认一个200像素的物体在物理世界相当于200米超过了最佳模拟范围. 一般需要对游戏里的物体进行物理上的缩放. 可以在 *game.project* 里的 [物理缩放设置](/zh/manuals/project-settings/#Physics) 处指定缩放值.
比如设置为 0.02 意味着 1:50, 那么200像素就是 4 米. 注意重力 (也在 *game.project* 里进行设定) 也需要基于缩放值进行调整.


## 物理循环更新

推荐以固定帧率更新物理引擎 (而不是依据游戏不稳定的更新频率) 以模拟稳定的物理效果. 可以在 *game.project* 文件的 Physics 部分中勾选 [Use Fixed Timestep setting](/zh/manuals/project-settings/#physics) 以启用固定帧率物理更新. 帧率由 *game.project* 文件的 Engine 部分中的 [Fixed Update Frequency setting](/zh/manuals/project-settings/#engine) 配置决定. 当物理引擎使用固定帧率更新时推荐使用 `fixed_update(self, dt)` 生命周期函数来对游戏中的物体的交互进行处理, 例如对物体施加一个力.


## 注意事项

碰撞代理
: 通过碰撞代理可以支持多个物理集合, 或称 *游戏世界*. 但是要记住每个集合都是一个单独的物理世界. 物理现象 (碰撞, 触发, 射线) 之发生在同一世界中. 两个不同集合的物体就算放到一块儿, 也不会发生物理碰撞.

碰撞漏检
: 如果发现碰撞未检测或未处理请先阅读 [调试教程的物理调试部分](/zh/manuals/debugging-game-logic/#物理引擎调试).