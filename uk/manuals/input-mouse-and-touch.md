---
brief: Цей посібник пояснює, як працює введення мишею та дотиками.
github: https://github.com/defold/doc
layout: manual
locale: uk
title: Введення мишею та дотиками в Defold
toc:
- anchor: mouse-triggers
  title: Тригери миші
- anchor: mouse-buttons
  title: Кнопки миші
- anchor: mouse-wheel
  title: Коліщатко миші
- anchor: mouse-movement
  title: Рух миші
- anchor: touch-triggers
  title: Тригери дотиків
- anchor: single-touch
  title: Одиночний дотик
- anchor: multi-touch
  title: Множинні дотики
- anchor: detecting-click-or-tap-on-objects
  title: Виявлення клацання або дотику на об’єктах
- anchor: detecting-interaction-with-gui-nodes
  title: Виявлення взаємодії з вузлами GUI
- anchor: detecting-interaction-with-game-objects
  title: Виявлення взаємодії з ігровими об’єктами
---

<div class='sidenote' markdown='1'>
Рекомендуємо ознайомитися із загальними принципами роботи введення в Defold, тим, як отримувати введення та в якому порядку воно надходить до ваших файлів скриптів. Докладніше про систему введення читайте в [посібнику з оглядом введення](/uk/manuals/input).
</div>

# Тригери миші {#mouse-triggers}
Тригери миші дають змогу прив’язати введення від кнопок миші та коліщаток прокручування до ігрових дій.

![](/manuals/images/input/mouse_bindings.png)

<div class='sidenote' markdown='1'>
Введення від кнопок миші `MOUSE_BUTTON_LEFT`, `MOUSE_BUTTON_RIGHT` і `MOUSE_BUTTON_MIDDLE` еквівалентне введенню від `MOUSE_BUTTON_1`, `MOUSE_BUTTON_2` і `MOUSE_BUTTON_3`.
</div>

<div class='important' markdown='1'>
У наведених нижче прикладах використовуються дії, показані на зображенні вище. Як і для будь-якого введення, ви можете називати свої дії введення як завгодно.
</div>

## Кнопки миші {#mouse-buttons}
Кнопки миші генерують події `pressed`, `released` і `repeated`. Приклад, що показує, як виявляти введення від лівої кнопки миші (натискання або відпускання):

```lua
function on_input(self, action_id, action)
    if action_id == hash("mouse_button_left") then
        if action.pressed then
            -- left mouse button pressed
        elseif action.released then
            -- left mouse button released
        end
    end
end
```

<div class='important' markdown='1'>
Дії введення `MOUSE_BUTTON_LEFT` (або `MOUSE_BUTTON_1`) надсилаються також для одиночних дотиків.
</div>

## Коліщатко миші {#mouse-wheel}
Введення від коліщатка миші виявляє дії прокручування. Поле `action.value` дорівнює `1`, якщо коліщатко прокручується, і `0` в іншому разі. (Дії прокручування обробляються як натискання кнопок. Наразі Defold не підтримує введення з точним відстеженням прокручування на сенсорних панелях.)

```lua
function on_input(self, action_id, action)
    if action_id == hash("mouse_wheel_up") then
        if action.value == 1 then
            -- mouse wheel is scrolled up
        end
    end
end
```

## Рух миші {#mouse-movement}
Рух миші обробляється окремо. Події руху миші не надходять, якщо у ваших прив’язках введення не налаштовано хоча б один тригер миші.

Рух миші не прив’язується у прив’язках введення: натомість `action_id` набуває значення `nil`, а таблиця `action` заповнюється позицією миші та зміною цієї позиції.

```lua
function on_input(self, action_id, action)
    if action.x and action.y then
        -- let game object follow mouse/touch movement
        local pos = vmath.vector3(action.x, action.y, 0)
        go.set_position(pos)
    end
end
```

# Тригери дотиків {#touch-triggers}
Тригери одиночних і множинних дотиків доступні на пристроях iOS і Android у нативних застосунках і пакетах HTML5.

![](/manuals/images/input/touch_bindings.png)

## Одиночний дотик {#single-touch}
Тригери одиночних дотиків не налаштовуються в розділі Touch Triggers прив’язок введення. Натомість **тригери одиночних дотиків налаштовуються автоматично, коли ви налаштовуєте введення від кнопки миші `MOUSE_BUTTON_LEFT` або `MOUSE_BUTTON_1`**.

## Множинні дотики {#multi-touch}
Тригери множинних дотиків заповнюють таблицю `touch` усередині таблиці дії. Елементи цієї таблиці мають цілочислові індекси від `1` до `N`, де `N` — кількість точок дотику. Кожен елемент таблиці містить поля з даними введення:

```lua
function on_input(self, action_id, action)
    if action_id == hash("touch_multi") then
        -- Spawn at each touch point
        for i, touchdata in ipairs(action.touch) do
            local pos = vmath.vector3(touchdata.x, touchdata.y, 0)
            factory.create("#factory", pos)
        end
    end
end
```

<div class='important' markdown='1'>
Множинним дотикам не можна призначати ту саму дію, що й введенню від кнопки миші `MOUSE_BUTTON_LEFT` або `MOUSE_BUTTON_1`. Призначення тієї самої дії фактично перевизначить одиночні дотики й унеможливить отримання будь-яких подій одиночного дотику.
</div>

<div class='sidenote' markdown='1'>
[Ресурс Defold-Input](https://defold.com/assets/defoldinput/) дає змогу легко налаштувати віртуальні екранні елементи керування, як-от кнопки й аналогові стіки, з підтримкою множинних дотиків.
</div>


## Виявлення клацання або дотику на об’єктах {#detecting-click-or-tap-on-objects}
Виявлення клацання або дотику користувача на візуальному компоненті (component) — дуже поширена операція, потрібна в багатьох іграх. Це може бути взаємодія користувача з кнопкою чи іншим елементом інтерфейсу або з ігровим об’єктом (game object), наприклад керованим гравцем юнітом у стратегічній грі, скарбом на рівні гри з дослідженням підземель або персонажем, який дає завдання в RPG. Вибір підходу залежить від типу візуального компонента.

### Виявлення взаємодії з вузлами GUI {#detecting-interaction-with-gui-nodes}
Для елементів інтерфейсу є функція `gui.pick_node(node, x, y)`, яка повертає `true` або `false` залежно від того, чи перебуває задана координата в межах вузла GUI. Докладніше дивіться в [документації API](/ref/gui/#gui.pick_node:node-x-y), [прикладі наведення вказівника](/examples/gui/pointer_over/) або [прикладі кнопки](/examples/gui/button/).

### Виявлення взаємодії з ігровими об’єктами {#detecting-interaction-with-game-objects}
Для ігрових об’єктів виявляти взаємодію складніше, оскільки на потрібні обчислення впливають такі чинники, як переміщення камери та проєкція у скрипті рендерингу. Є два загальні підходи до виявлення взаємодії з ігровими об’єктами:

  1. Відстежуйте позицію та розміри ігрових об’єктів, з якими користувач може взаємодіяти, і перевіряйте, чи перебуває координата миші або дотику в межах будь-якого з цих об’єктів.
  2. Приєднайте об’єкти колізій до ігрових об’єктів, з якими користувач може взаємодіяти, а також створіть один об’єкт колізії, що слідує за мишею або пальцем, і перевіряйте колізії між ними.

<div class='sidenote' markdown='1'>
Готове рішення, що використовує об’єкти колізій для виявлення введення користувача й підтримує перетягування та клацання, можна знайти в [ресурсі Defold-Input](https://defold.com/assets/defoldinput/).
</div>

В обох випадках потрібно виконувати перетворення між координатами події миші або дотику в екранному просторі та координатами ігрових об’єктів у світовому просторі. Це можна зробити кількома способами:

  * Вручну відстежуйте, які перетворення виду та проєкції використовує скрипт рендерингу, і використовуйте їх для перетворення координат у світовий простір і назад. Дивіться [приклад у посібнику з камери](/uk/manuals/camera/#converting-mouse-to-world-coordinates).
  * Використовуйте [стороннє рішення для камери](/uk/manuals/camera/#third-party-camera-solutions) та надані ним функції перетворення координат з екранного простору у світовий.