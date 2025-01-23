---
layout: manual
language: ru
github: https://github.com/defold/doc
toc: ["Анимация свойств","Применение анимации свойств","Анимация свойств GUI-нод"]
title: Анимации свойств
brief: Данное руководство объясняет как использовать анимацию свойств в Defold.
---

# Анимация свойств

Все свойства выражаемые числовыми типами (числа, vector3, vector4 и кватернионы), а также шейдерные константы могут быть анимированны встроенной системой анимации, с помощью функции `go.animate()`. Движок автоматически делает "твининг" свойств согласно переданному режиму воспроизведения и функции смягчения. К тому же имеется возможность задать пользовательские функции смягчения.

  ![Property animation](/manuals/images/animation/property_animation.png)
  ![Bounce loop](/manuals/images/animation/bounce.gif)

## Применение анимации свойств

Чтобы анимировать свойство игрового объекта или компонента, используйте функцию `go.animate()`. Для свойств GUI-нод, соответствующей функцией будет `gui.animate()`.

```lua
-- Установить координату позиции по "y" в 200
go.set(".", "position.y", 200)
-- Затем анимировать ее
go.animate(".", "position.y", go.PLAYBACK_LOOP_PINGPONG, 100, go.EASING_OUTBOUNCE, 2)
```

Для остановки всех анимаций заданного свойства, вызовите `go.cancel_animations()`, или, в случае с GUI-нодами, `gui.cancel_animation()`: 

```lua
-- Остановить анимацию эйлерова вращения по Z для текущего игрового объекта 
go.cancel_animations(".", "euler.z")
```

При отмене анимации составного свойства, такого как например `position`, вся анимация его составляющих компонент (`position.x`, `position.y` и `position.z`) будет также отменена.

[Руководство по свойствам](/ru/manuals/properties) содержит все доступные свойства игровых объектов, компонентов и GUI-нод.

## Анимация свойств GUI-нод

Почти все свойства GUI-нод можно анимировать. Например, можно сделать ноду невидимой, установив ее свойство `color` в полную прозрачность, а затем заново проявить ноду в видимую, анимируя цвет к белому (или другими словами --- без оттенка).

```lua
local node = gui.get_node("button")
local color = gui.get_color(node)
-- Анимировать цвет к белому
gui.animate(node, gui.PROP_COLOR, vmath.vector4(1, 1, 1, 1), gui.EASING_INOUTQUAD, 0.5)
-- Анимировать красный компонент цвета контура
gui.animate(node, "outline.x", 1, gui.EASING_INOUTQUAD, 0.5)
-- И сместить позицию по x на 100
gui.animate(node, hash("position.x"), 100, gui.EASING_INOUTQUAD, 0.5)
```

## Завершающие функции обратного вызова

Функции анимирования свойств `go.animate()` и `gui.animate()` поддерживают опциональные функции обратного вызова в качестве последнего переданного аргумента. Такие переданные функции будут вызваны когда анимация проиграется до конца. Функции никогда не будут вызваны для зацикленной анимации, а также для анимации, которая была отменена вручную вызовом `go.cancel_animations()` или `gui.cancel_animation()`. Функция обратного вызова может быть использована для активации других событий по завершению анимации или для склеивания нескольких анимаций в одну цепочку.

## Смягчение

Смягчение определяет характер изменения анимируемого значения во времени. Изображения ниже описывают функции применяемые во времени для создания смягчения.

Ниже приведены следующие валидные значения смягчения для функции `go.animate()`:

|---|---|
| go.EASING_LINEAR | |
| go.EASING_INBACK | go.EASING_OUTBACK |
| go.EASING_INOUTBACK | go.EASING_OUTINBACK |
| go.EASING_INBOUNCE | go.EASING_OUTBOUNCE |
| go.EASING_INOUTBOUNCE | go.EASING_OUTINBOUNCE |
| go.EASING_INELASTIC | go.EASING_OUTELASTIC |
| go.EASING_INOUTELASTIC | go.EASING_OUTINELASTIC |
| go.EASING_INSINE | go.EASING_OUTSINE |
| go.EASING_INOUTSINE | go.EASING_OUTINSINE |
| go.EASING_INEXPO | go.EASING_OUTEXPO |
| go.EASING_INOUTEXPO | go.EASING_OUTINEXPO |
| go.EASING_INCIRC | go.EASING_OUTCIRC |
| go.EASING_INOUTCIRC | go.EASING_OUTINCIRC |
| go.EASING_INQUAD | go.EASING_OUTQUAD |
| go.EASING_INOUTQUAD | go.EASING_OUTINQUAD |
| go.EASING_INCUBIC | go.EASING_OUTCUBIC |
| go.EASING_INOUTCUBIC | go.EASING_OUTINCUBIC |
| go.EASING_INQUART | go.EASING_OUTQUART |
| go.EASING_INOUTQUART | go.EASING_OUTINQUART |
| go.EASING_INQUINT | go.EASING_OUTQUINT |
| go.EASING_INOUTQUINT | go.EASING_OUTINQUINT |

Ниже приведены следующие валидные значения смягчения для функции `gui.animate()`:

|---|---|
| gui.EASING_LINEAR | |
| gui.EASING_INBACK | gui.EASING_OUTBACK |
| gui.EASING_INOUTBACK | gui.EASING_OUTINBACK |
| gui.EASING_INBOUNCE | gui.EASING_OUTBOUNCE |
| gui.EASING_INOUTBOUNCE | gui.EASING_OUTINBOUNCE |
| gui.EASING_INELASTIC | gui.EASING_OUTELASTIC |
| gui.EASING_INOUTELASTIC | gui.EASING_OUTINELASTIC |
| gui.EASING_INSINE | gui.EASING_OUTSINE |
| gui.EASING_INOUTSINE | gui.EASING_OUTINSINE |
| gui.EASING_INEXPO | gui.EASING_OUTEXPO |
| gui.EASING_INOUTEXPO | gui.EASING_OUTINEXPO |
| gui.EASING_INCIRC | gui.EASING_OUTCIRC |
| gui.EASING_INOUTCIRC | gui.EASING_OUTINCIRC |
| gui.EASING_INQUAD | gui.EASING_OUTQUAD |
| gui.EASING_INOUTQUAD | gui.EASING_OUTINQUAD |
| gui.EASING_INCUBIC | gui.EASING_OUTCUBIC |
| gui.EASING_INOUTCUBIC | gui.EASING_OUTINCUBIC |
| gui.EASING_INQUART | gui.EASING_OUTQUART |
| gui.EASING_INOUTQUART | gui.EASING_OUTINQUART |
| gui.EASING_INQUINT | gui.EASING_OUTQUINT |
| gui.EASING_INOUTQUINT | gui.EASING_OUTINQUINT |

![Linear interpolation](/manuals/images/properties/easing_linear.png)
![In back](/manuals/images/properties/easing_inback.png)
![Out back](/manuals/images/properties/easing_outback.png)
![In-out back](/manuals/images/properties/easing_inoutback.png)
![Out-in back](/manuals/images/properties/easing_outinback.png)
![In bounce](/manuals/images/properties/easing_inbounce.png)
![Out bounce](/manuals/images/properties/easing_outbounce.png)
![In-out bounce](/manuals/images/properties/easing_inoutbounce.png)
![Out-in bounce](/manuals/images/properties/easing_outinbounce.png)
![In elastic](/manuals/images/properties/easing_inelastic.png)
![Out elastic](/manuals/images/properties/easing_outelastic.png)
![In-out elastic](/manuals/images/properties/easing_inoutelastic.png)
![Out-in elastic](/manuals/images/properties/easing_outinelastic.png)
![In sine](/manuals/images/properties/easing_insine.png)
![Out sine](/manuals/images/properties/easing_outsine.png)
![In-out sine](/manuals/images/properties/easing_inoutsine.png)
![Out-in sine](/manuals/images/properties/easing_outinsine.png)
![In exponential](/manuals/images/properties/easing_inexpo.png)
![Out exponential](/manuals/images/properties/easing_outexpo.png)
![In-out exponential](/manuals/images/properties/easing_inoutexpo.png)
![Out-in exponential](/manuals/images/properties/easing_outinexpo.png)
![In circlic](/manuals/images/properties/easing_incirc.png)
![Out circlic](/manuals/images/properties/easing_outcirc.png)
![In-out circlic](/manuals/images/properties/easing_inoutcirc.png)
![Out-in circlic](/manuals/images/properties/easing_outincirc.png)
![In quadratic](/manuals/images/properties/easing_inquad.png)
![Out quadratic](/manuals/images/properties/easing_outquad.png)
![In-out quadratic](/manuals/images/properties/easing_inoutquad.png)
![Out-in quadratic](/manuals/images/properties/easing_outinquad.png)
![In cubic](/manuals/images/properties/easing_incubic.png)
![Out cubic](/manuals/images/properties/easing_outcubic.png)
![In-out cubic](/manuals/images/properties/easing_inoutcubic.png)
![Out-in cubic](/manuals/images/properties/easing_outincubic.png)
![In quartic](/manuals/images/properties/easing_inquart.png)
![Out quartic](/manuals/images/properties/easing_outquart.png)
![In-out quartic](/manuals/images/properties/easing_inoutquart.png)
![Out-in quartic](/manuals/images/properties/easing_outinquart.png)
![In quintic](/manuals/images/properties/easing_inquint.png)
![Out quintic](/manuals/images/properties/easing_outquint.png)
![In-out quintic](/manuals/images/properties/easing_inoutquint.png)
![Out-in quintic](/manuals/images/properties/easing_outinquint.png)

## Пользовательские функции смягчения

Имеется возможность создать собственные кривые смягчения, задав `vector` с набором значений и подставив этот вектор вместо одной из предопределенных выше констант. Значения вектора выражают кривую от начального значения (`0`) к целевому конечному (`1`). Среда выполнения семплирует значения из вектора и линейно интерполирует значения между точками кривой плавности, выраженными в векторе.

К примеру, данный вектор:

```lua
local values = { 0, 0.4, 0.2, 0.2, 0.5, 1 }
local my_easing = vmath.vector(values)
```

дает следующую кривую:

![Custom curve](/manuals/images/animation/custom_curve.png)

Следующий пример сделает так, что позиция y игрового объекта будет прыгать между текущей позицией и значением 200, согласно кривой квадратной волны:

```lua
local values = { 0, 0, 0, 0, 0, 0, 0, 0,
                 1, 1, 1, 1, 1, 1, 1, 1,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 1, 1, 1, 1, 1, 1, 1, 1,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 1, 1, 1, 1, 1, 1, 1, 1,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 1, 1, 1, 1, 1, 1, 1, 1 }
local square_easing = vmath.vector(values)
go.animate("go", "position.y", go.PLAYBACK_LOOP_PINGPONG, 200, square_easing, 2.0)
```

![Square curve](/manuals/images/animation/square_curve.png)
