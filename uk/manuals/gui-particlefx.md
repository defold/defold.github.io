---
brief: Цей посібник пояснює, як ефекти частинок працюють у GUI Defold.
github: https://github.com/defold/doc
layout: manual
locale: uk
title: Ефекти частинок у GUI Defold
toc:
- anchor: gui-particlefx-nodes
  title: Вузли ParticleFX у GUI
- anchor: adding-particle-fx-nodes
  title: Додавання вузлів Particle FX
- anchor: controlling-the-effect
  title: Керування ефектом
---

# Вузли ParticleFX у GUI {#gui-particlefx-nodes}

Вузол ефекту частинок використовується для відтворення систем ефектів частинок в екранному просторі GUI.

## Додавання вузлів Particle FX {#adding-particle-fx-nodes}

Щоб додати нові вузли частинок, <kbd>клацніть правою кнопкою миші</kbd> у панелі *Outline* і виберіть <kbd>Add ▸ ParticleFX</kbd> або натисніть <kbd>A</kbd> і виберіть <kbd>ParticleFX</kbd>.

Джерелом ефекту можуть бути ефекти частинок, які ви додали до GUI. Щоб додати ефекти частинок, <kbd>клацніть правою кнопкою миші</kbd> піктограму папки *Particle FX* у панелі *Outline* і виберіть <kbd>Add ▸ Particle FX...</kbd>. Потім задайте для вузла властивість *Particlefx*:

![Ефект частинок](/manuals/images/gui-particlefx/create.png)

## Керування ефектом {#controlling-the-effect}

Ви можете запускати та зупиняти ефект, керуючи вузлом зі скрипту:

```lua
-- start the particle effect
local particles_node = gui.get_node("particlefx")
gui.play_particlefx(particles_node)
```

```lua
-- stop the particle effect
local particles_node = gui.get_node("particlefx")
gui.stop_particlefx(particles_node)
```

Докладніше про роботу ефектів частинок дивіться в [посібнику з ефектів частинок](/uk/manuals/particlefx).