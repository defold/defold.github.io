---
brief: 物理引擎允许您将物理对象分组，并过滤它们应该如何碰撞。
github: https://github.com/defold/doc
language: zh
layout: manual
title: Defold 中的碰撞组
toc:
- 组和掩码
- 检测碰撞
---

# 组和掩码

物理引擎允许您将物理对象分组，并过滤它们应该如何碰撞。这是通过命名的 _碰撞组_ 来处理的。对于您创建的每个碰撞对象，有两个属性控制对象如何与其他对象碰撞，*组(Group)* 和 *掩码(Mask)*。

要使两个对象之间的碰撞被注册，两个对象必须在其 *掩码(Mask)* 字段中相互指定对方的组。

![Physics collision group](/manuals/images/physics/collision_group.png)

*掩码(Mask)* 字段可以包含多个组名，从而允许实现复杂的交互场景。

## 检测碰撞
当两个具有匹配组和掩码的碰撞对象碰撞时，物理引擎将生成[碰撞消息](/zh/manuals/physics-messages)，可以在游戏中使用这些消息来响应碰撞。