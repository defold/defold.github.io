---
brief: Ta instrukcja wyjaśnia, jak używać węzłów GUI typu box.
github: https://github.com/defold/doc
layout: manual
locale: pl
title: Węzły GUI typu box w Defold
toc:
- Węzły GUI typu box
- Dodawanie węzłów box
- Odtwarzanie animacji
---

# Węzły GUI typu box

Węzeł GUI typu box to prostokąt wypełniony kolorem, teksturą lub animacją.

## Dodawanie węzłów box

Dodaj nowe węzły box, klikając prawym przyciskiem myszy w *Outline* i wybierając <kbd>Add ▸ Box</kbd>, albo naciśnij <kbd>A</kbd> i wybierz <kbd>Box</kbd>.

Możesz używać obrazów i animacji z atlasów lub źródeł kafelków dodanych do GUI. Aby dodać tekstury, kliknij prawym przyciskiem myszy ikonę folderu *Textures* w *Outline* i wybierz <kbd>Add ▸ Textures...</kbd>. Następnie ustaw właściwość *Texture* węzła box:

![Tekstury](/manuals/images/gui-box/create.png)

Zwróć uwagę, że kolor węzła box zabarwia grafikę. Kolor zabarwienia jest mnożony przez dane obrazu, więc jeśli ustawisz kolor na biały (domyślny), nie zostanie zastosowane zabarwienie.

![Teksturowany obraz](/manuals/images/gui-box/tinted.png)

Węzły box są zawsze renderowane, nawet jeśli nie mają przypisanej tekstury, mają ustawioną alfę na `0` albo mają rozmiar `0, 0, 0`. Węzły box powinny zawsze mieć przypisaną teksturę, aby renderer mógł je poprawnie grupować i zmniejszać liczbę wywołań rysowania.

## Odtwarzanie animacji

Węzły box mogą odtwarzać animacje z atlasów lub źródeł kafelków. Więcej informacji znajdziesz w [instrukcji animacji flipbook](/pl/manuals/flipbook-animation).

{% include shared/pl/slice-9-texturing.md %}