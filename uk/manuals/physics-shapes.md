---
brief: Компонент колізії може використовувати кілька примітивних форм або одну складну форму.
github: https://github.com/defold/doc
layout: manual
locale: uk
title: Форми колізій
toc:
- anchor: collision-shapes
  title: Форми колізій
- anchor: primitive-shapes
  title: Примітивні форми
- anchor: box-shape
  title: Форма прямокутного паралелепіпеда
- anchor: sphere-shape
  title: Форма сфери
- anchor: capsule-shape
  title: Форма капсули
- anchor: complex-shapes
  title: Складні форми
- anchor: tilemap-collision-shape
  title: Форма колізії карти плиток
- anchor: convex-hull-shape
  title: Форма опуклої оболонки
- anchor: file-format
  title: Формат файлу
- anchor: external-tools
  title: Зовнішні інструменти
- anchor: scaling-collision-shapes
  title: Масштабування форм колізій
- anchor: resizing-collision-shapes
  title: Змінення розмірів форм колізій
- anchor: rotating-collision-shapes
  title: Повертання форм колізій
- anchor: rotating-collision-shapes-in-3d-physics
  title: Повертання форм колізій у 3D-фізиці
- anchor: rotating-collision-shapes-in-2d-physics
  title: Повертання форм колізій у 2D-фізиці
- anchor: debugging
  title: Налагодження
---

# Форми колізій {#collision-shapes}

Компонент колізії (collision component) може використовувати кілька примітивних форм або одну складну форму.

### Примітивні форми {#primitive-shapes}
Примітивні форми — це *прямокутний паралелепіпед*, *сфера* та *капсула*. Щоб додати примітивну форму, <kbd>клацніть правою кнопкою миші</kbd> об’єкт колізії та виберіть <kbd>Add Shape</kbd>:

![Додавання примітивної форми](/manuals/images/physics/add_shape.png)

## Форма прямокутного паралелепіпеда {#box-shape}
Прямокутний паралелепіпед має позицію, поворот і розміри (ширину, висоту та глибину):

![Форма прямокутного паралелепіпеда](/manuals/images/physics/box.png)

## Форма сфери {#sphere-shape}
Сфера має позицію, поворот і діаметр:

![Форма сфери](/manuals/images/physics/sphere.png)

## Форма капсули {#capsule-shape}
Капсула має позицію, поворот, діаметр і висоту:

![Форма сфери](/manuals/images/physics/capsule.png)

<div class='important' markdown='1'>
Форми капсули підтримуються лише під час використання 3D-фізики (налаштовується в розділі Physics файлу *game.project*).
</div>

### Складні форми {#complex-shapes}
Складну форму можна створити з компонента карти плиток або з форми опуклої оболонки.

## Форма колізії карти плиток {#tilemap-collision-shape}
Defold містить функцію, яка дає змогу легко генерувати фізичні форми для джерела плиток, що використовується картою плиток. У [посібнику з джерел плиток](/uk/manuals/tilesource/#tile-source-collision-shapes) пояснено, як додавати групи колізій до джерела плиток і призначати плитки групам колізій ([приклад](/examples/tilemap/collisions/)).

Щоб додати колізії до карти плиток:

1. Додайте карту плиток до ігрового об’єкта (game object): <kbd>клацніть правою кнопкою миші</kbd> ігровий об’єкт і виберіть <kbd>Add Component File</kbd>. Виберіть файл карти плиток.
2. Додайте компонент об’єкта колізії до ігрового об’єкта: <kbd>клацніть правою кнопкою миші</kbd> ігровий об’єкт і виберіть <kbd>Add Component ▸ Collision Object</kbd>.
3. Замість додавання форм до компонента задайте файл *карти плиток* у властивості *Collision Shape*.
4. Налаштуйте *Properties* компонента об’єкта колізії як зазвичай.

![Колізії джерела плиток](/manuals/images/physics/collision_tilemap.png)

<div class='important' markdown='1'>
Зауважте, що властивість *Group* тут **не** використовується, оскільки групи колізій визначено в джерелі плиток карти плиток.
</div>

## Форма опуклої оболонки {#convex-hull-shape}
Defold містить функцію, яка дає змогу створити форму опуклої оболонки (convex hull shape) із трьох або більше точок. 

1. Створіть файл форми опуклої оболонки (розширення файлу `.convexshape`) за допомогою зовнішнього редактора.
2. Відредагуйте файл вручну за допомогою текстового редактора або зовнішнього інструмента (див. нижче)
3. Замість додавання форм до компонента об’єкта колізії задайте файл *опуклої форми* у властивості *Collision Shape*.

### Формат файлу {#file-format}
Формат файлу опуклої оболонки використовує той самий формат даних, що й усі інші файли Defold, тобто текстовий формат protobuf. Форма опуклої оболонки визначає точки оболонки. У 2D-фізиці точки слід задавати в порядку проти годинникової стрілки. У режимі 3D-фізики використовується абстрактна хмара точок. Приклад для 2D:

```
shape_type: TYPE_HULL
data: 200.000
data: 100.000
data: 0.0
data: 400.000
data: 100.000
data: 0.0
data: 400.000
data: 300.000
data: 0.0
data: 200.000
data: 300.000
data: 0.0
```

Наведений вище приклад визначає чотири кути прямокутника:

```
 200x300   400x300
    4---------3
    |         |
    |         |
    |         |
    |         |
    1---------2
 200x100   400x100
```

## Зовнішні інструменти {#external-tools}

Для створення форм колізій можна використовувати різні зовнішні інструменти:

* [Physics Editor](https://www.codeandweb.com/physicseditor/tutorials/how-to-create-physics-shapes-for-defold) від CodeAndWeb можна використовувати для створення ігрових об’єктів зі спрайтами та відповідними формами колізій.
* [Defold Polygon Editor](https://rossgrams.itch.io/defold-polygon-editor) можна використовувати для створення форм опуклої оболонки.
* [Physics Body Editor](https://selimanac.github.io/physics-body-editor/) можна використовувати для створення форм опуклої оболонки.


# Масштабування форм колізій {#scaling-collision-shapes}
Об’єкт колізії та його форми успадковують масштаб ігрового об’єкта. Щоб вимкнути цю поведінку, зніміть прапорець [Allow Dynamic Transforms](/uk/manuals/project-settings/#allow-dynamic-transforms) у розділі Physics файлу *game.project*. Зауважте, що підтримується лише рівномірне масштабування, а якщо масштаб нерівномірний, використовуватиметься найменше значення масштабу.

# Змінення розмірів форм колізій {#resizing-collision-shapes}
Розміри форм об’єкта колізії можна змінювати під час виконання за допомогою `physics.set_shape()`. Приклад:

```lua
-- set capsule shape data
local capsule_data = {
  type = physics.SHAPE_TYPE_CAPSULE,
  diameter = 10,
  height = 20,
}
physics.set_shape("#collisionobject", "my_capsule_shape", capsule_data)

-- set sphere shape data
local sphere_data = {
  type = physics.SHAPE_TYPE_SPHERE,
  diameter = 10,
}
physics.set_shape("#collisionobject", "my_sphere_shape", sphere_data)

-- set box shape data
local box_data = {
  type = physics.SHAPE_TYPE_BOX,
  dimensions = vmath.vector3(10, 10, 5),
}
physics.set_shape("#collisionobject", "my_box_shape", box_data)
```

<div class='sidenote' markdown='1'>
Форма відповідного типу із зазначеним ідентифікатором має вже існувати в об’єкті колізії.
</div>

# Повертання форм колізій {#rotating-collision-shapes}

## Повертання форм колізій у 3D-фізиці {#rotating-collision-shapes-in-3d-physics}
Форми колізій у 3D-фізиці можна повертати навколо всіх осей.


## Повертання форм колізій у 2D-фізиці {#rotating-collision-shapes-in-2d-physics}
Форми колізій у 2D-фізиці можна повертати лише навколо осі z. Повертання навколо осі x або y дасть неправильні результати, і його слід уникати навіть у разі повертання на 180 градусів, щоб фактично віддзеркалити форму вздовж осі x або y. Для віддзеркалення фізичної форми рекомендовано використовувати [`physics.set_hlip(url, flip)`](/ref/stable/physics/?#physics.set_hflip:url-flip) і [`physics.set_vlip(url, flip)`](/ref/stable/physics/?#physics.set_vflip:url-flip).


# Налагодження {#debugging}
Ви можете [увімкнути налагодження фізики](/uk/manuals/debugging-game-logic/#debugging-problems-with-physics), щоб бачити форми колізій під час виконання.