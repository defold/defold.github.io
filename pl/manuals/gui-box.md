---
brief: Ta instrukcja wyjaśnia jak używać węzłów typu box.
github: https://github.com/defold/doc
language: pl
layout: manual
title: Węzły prostokątne - box w Defoldzie
toc:
- Węzeł GUI typu box
- Dodawanie węzłów box
- Odtwarzanie animacji
---

# Węzeł GUI typu box

Węzeł prostokątny box to prostokąt wypełniony kolorem, teksturą lub animacją.

## Dodawanie węzłów box

Dodaj nowe węzły box, <kbd>klikając prawym przyciskiem myszy</kbd> w widoku "Outline" i wybierając <kbd>Add ▸ Box</kbd>, lub naciśnij klawisz <kbd>A</kbd> i wybierz <kbd>Box</kbd>.

Możesz używać obrazów i animacji z atlasów lub źródeł kafelków, które zostały dodane do GUI. Dodaj tekstury, klikając prawym przyciskiem myszy na ikonę folderu "Textures" w widoku "Outline" i wybierając <kbd>Add ▸ Textures...</kbd>. Następnie ustaw właściwość *Texture* węzłu box na daną teksturę:

![Textures](/manuals/images/gui-box/create.png)

Należy zauważyć, że kolor węzła box będzie barwił (ang. tint) grafikę. Kolor barwienia jest mnożony przez dane obrazu, co oznacza, że jeśli ustawisz kolor na biały (domyślny), w praktyce nie zostanie zastosowane barwienie.

![Tinted texture](/manuals/images/gui-box/tinted.png)

Węzły box są zawsze renderowane, nawet jeśli nie mają przypisanej tekstury, mają ustawioną wartość alfa na `0` lub mają rozmiar `0, 0, 0`. Węzły box powinny zawsze mieć przypisaną do nich teksturę, aby renderer mógł je właściwie grupować i zmniejszać liczbę wywołań rysowania (ang. draw calls).

## Odtwarzanie animacji

Węzły pudełkowe mogą odtwarzać animacje z atlasów lub źródeł kafelków. Aby dowiedzieć się więcej, zajrzyj do [instrukcji do animacji flipbook](/pl/manuals/flipbook-animation).

{% include shared/pl/slice-9-texturing.md %}