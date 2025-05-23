---
brief: Ta instrukcja jak działają grupy i maski silnika fizyki.
github: https://github.com/defold/doc
language: pl
layout: manual
title: Grupy kolizji w Defoldzie
toc:
- Grupy i maski kolizji
- Wykrywanie kolizji
---

# Grupy i maski kolizji

Silnik fizyczny pozwala na grupowanie obiektów fizycznych i określanie, jak powinny ze sobą kolidować. Jest to możliwe dzięki zdefiniowanym grupom kolizji. Dla każdego obiektu kolizji (ang. collision object) tworzysz dwie właściwości (ang. properties), które kontrolują, jak obiekt koliduje z innymi obiektami, a mianowicie *Group* i *Mask*.

Aby kolizja między dwoma obiektami została zarejestrowana, oba obiekty muszą wzajemnie określić grupy, do których należą (określone w *Group*), w swoim polu *Mask*.

![Physics collision group](/manuals/images/physics/collision_group.png)

Pole *Mask* może zawierać wiele nazw grup, co pozwala na różne scenariusze interakcji.

## Wykrywanie kolizji

Gdy dwa obiekty kolizji o takich samych grupach i maskach kolidują, silnik fizyczny generuje [wiadomości o kolizji](/pl/manuals/physics-messages), które można wykorzystać w grach do odpowiedniej reakcji na kolizje.