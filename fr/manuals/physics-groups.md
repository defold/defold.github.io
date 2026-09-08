---
brief: Le moteur physique vous permet de regrouper vos objets physiques et de filtrer la manière dont ils doivent entrer en collision.
github: https://github.com/defold/doc
layout: manual
locale: fr
title: Groupes de collision dans Defold
toc:
- anchor: group-and-mask
  title: Groupe et masque
- anchor: detecting-collisions
  title: Détection des collisions
---

# Groupe et masque {#group-and-mask}

Le moteur physique vous permet de regrouper vos objets physiques et de filtrer la manière dont ils doivent entrer en collision. Ce mécanisme repose sur des _groupes de collision_ nommés. Pour chaque objet de collision que vous créez, deux propriétés contrôlent la manière dont l'objet entre en collision avec les autres objets : *Group* et *Mask*.

Pour qu'une collision entre deux objets soit détectée, chacun des deux objets doit spécifier le groupe de l'autre dans son champ *Mask*.

![Groupe de collision physique](/manuals/images/physics/collision_group.png)

Le champ *Mask* peut contenir plusieurs noms de groupes, ce qui permet des scénarios d'interaction complexes.

## Détection des collisions {#detecting-collisions}
Lorsque deux objets de collision dont les groupes et les masques correspondent entrent en collision, le moteur physique génère des [messages de collision](/fr/manuals/physics-messages) que vous pouvez utiliser dans les jeux pour réagir aux collisions.