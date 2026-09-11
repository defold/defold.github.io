---
brief: Un composant de collision peut utiliser plusieurs formes primitives ou une seule forme complexe.
github: https://github.com/defold/doc
layout: manual
locale: fr
title: Formes de collision
toc:
- anchor: collision-shapes
  title: Formes de collision
- anchor: primitive-shapes
  title: Formes primitives
- anchor: box-shape
  title: Forme de boîte
- anchor: sphere-shape
  title: Forme de sphère
- anchor: capsule-shape
  title: Forme de capsule
- anchor: complex-shapes
  title: Formes complexes
- anchor: tilemap-collision-shape
  title: Forme de collision de tilemap
- anchor: convex-hull-shape
  title: Forme denveloppe convexe
- anchor: file-format
  title: Format du fichier
- anchor: external-tools
  title: Outils externes
- anchor: scaling-collision-shapes
  title: Mise à léchelle des formes de collision
- anchor: resizing-collision-shapes
  title: Redimensionnement des formes de collision
- anchor: rotating-collision-shapes
  title: Rotation des formes de collision
- anchor: rotating-collision-shapes-in-3d-physics
  title: Rotation des formes de collision en physique 3D
- anchor: rotating-collision-shapes-in-2d-physics
  title: Rotation des formes de collision en physique 2D
- anchor: debugging
  title: Débogage
---

# Formes de collision {#collision-shapes}

Un composant (component) de collision peut utiliser plusieurs formes primitives ou une seule forme complexe.

### Formes primitives {#primitive-shapes}
Les formes primitives sont la *boîte*, la *sphère* et la *capsule*. Pour ajouter une forme primitive, <kbd>faites un clic droit</kbd> sur l'objet de collision et sélectionnez <kbd>Add Shape</kbd> :

![Ajouter une forme primitive](/manuals/images/physics/add_shape.png)

## Forme de boîte {#box-shape}
Une boîte possède une position, une rotation et des dimensions (largeur, hauteur et profondeur) :

![Forme de boîte](/manuals/images/physics/box.png)

## Forme de sphère {#sphere-shape}
Une sphère possède une position, une rotation et un diamètre :

![Forme de sphère](/manuals/images/physics/sphere.png)

## Forme de capsule {#capsule-shape}
Une capsule possède une position, une rotation, un diamètre et une hauteur :

![Forme de sphère](/manuals/images/physics/capsule.png)

<div class='important' markdown='1'>
Les formes de capsule sont prises en charge uniquement avec la physique 3D (configurée dans la section Physics du fichier *game.project*).
</div>

### Formes complexes {#complex-shapes}
Une forme complexe peut être créée à partir d'un composant tilemap ou d'une forme d'enveloppe convexe.

## Forme de collision de tilemap {#tilemap-collision-shape}
Defold propose une fonctionnalité qui permet de générer facilement des formes physiques pour la source de tuiles utilisée par une tilemap. Le [manuel des sources de tuiles](/fr/manuals/tilesource/#tile-source-collision-shapes) explique comment ajouter des groupes de collision à une source de tuiles et affecter des tuiles à ces groupes ([exemple](/examples/tilemap/collisions/)).

Pour ajouter des collisions à une tilemap :

1. Ajoutez la tilemap à un objet de jeu (game object) en <kbd>faisant un clic droit</kbd> sur l'objet de jeu et en sélectionnant <kbd>Add Component File</kbd>. Sélectionnez le fichier de tilemap.
2. Ajoutez un composant d'objet de collision à l'objet de jeu en <kbd>faisant un clic droit</kbd> sur l'objet de jeu et en sélectionnant <kbd>Add Component ▸ Collision Object</kbd>.
3. Au lieu d'ajouter des formes au composant, définissez la propriété *Collision Shape* sur le fichier *tilemap*.
4. Configurez les *Properties* du composant d'objet de collision comme d'habitude.

![Collision de source de tuiles](/manuals/images/physics/collision_tilemap.png)

<div class='important' markdown='1'>
Notez que la propriété *Group* n'est **pas** utilisée ici, car les groupes de collision sont définis dans la source de tuiles de la tilemap.
</div>

## Forme d'enveloppe convexe {#convex-hull-shape}
Defold propose une fonctionnalité qui permet de créer une forme d'enveloppe convexe à partir de trois points ou plus. 

1. Créez un fichier de forme d'enveloppe convexe (extension de fichier `.convexshape`) à l'aide d'un éditeur externe.
2. Modifiez le fichier manuellement à l'aide d'un éditeur de texte ou d'un outil externe (voir ci-dessous)
3. Au lieu d'ajouter des formes au composant d'objet de collision, définissez la propriété *Collision Shape* sur le fichier de *forme convexe*.

### Format du fichier {#file-format}
Le format de fichier d'enveloppe convexe utilise le même format de données que tous les autres fichiers Defold, à savoir le format texte protobuf. Une forme d'enveloppe convexe définit les points de l'enveloppe. En physique 2D, les points doivent être fournis dans le sens inverse des aiguilles d'une montre. Un nuage de points abstrait est utilisé en mode physique 3D. Exemple en 2D :

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

L'exemple ci-dessus définit les quatre coins d'un rectangle :

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

## Outils externes {#external-tools}

Plusieurs outils externes peuvent être utilisés pour créer des formes de collision :

* [Physics Editor](https://www.codeandweb.com/physicseditor/tutorials/how-to-create-physics-shapes-for-defold) de CodeAndWeb permet de créer des objets de jeu avec des sprites et les formes de collision correspondantes.
* [Defold Polygon Editor](https://rossgrams.itch.io/defold-polygon-editor) permet de créer des formes d'enveloppe convexe.
* [Physics Body Editor](https://selimanac.github.io/physics-body-editor/) permet de créer des formes d'enveloppe convexe.


# Mise à l'échelle des formes de collision {#scaling-collision-shapes}
L'objet de collision et ses formes héritent de l'échelle de l'objet de jeu. Pour désactiver ce comportement, décochez la case [Allow Dynamic Transforms](/fr/manuals/project-settings/#allow-dynamic-transforms) dans la section Physics de *game.project*. Notez que seule la mise à l'échelle uniforme est prise en charge et que la plus petite valeur d'échelle sera utilisée si l'échelle n'est pas uniforme.

# Redimensionnement des formes de collision {#resizing-collision-shapes}
Les formes d'un objet de collision peuvent être redimensionnées à l'exécution à l'aide de `physics.set_shape()`. Exemple :

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
Une forme du type approprié et portant l'identifiant spécifié doit déjà exister sur l'objet de collision.
</div>

# Rotation des formes de collision {#rotating-collision-shapes}

## Rotation des formes de collision en physique 3D {#rotating-collision-shapes-in-3d-physics}
Les formes de collision en physique 3D peuvent être tournées autour de tous les axes.


## Rotation des formes de collision en physique 2D {#rotating-collision-shapes-in-2d-physics}
Les formes de collision en physique 2D ne peuvent être tournées qu'autour de l'axe z. Une rotation autour de l'axe x ou y produira des résultats incorrects et doit être évitée, même pour une rotation de 180 degrés destinée à retourner la forme suivant l'axe x ou y. Pour retourner une forme physique, il est recommandé d'utiliser [`physics.set_hlip(url, flip)`](/ref/stable/physics/?#physics.set_hflip:url-flip) et [`physics.set_vlip(url, flip)`](/ref/stable/physics/?#physics.set_vflip:url-flip).


# Débogage {#debugging}
Vous pouvez [activer le débogage de la physique](/fr/manuals/debugging-game-logic/#debugging-problems-with-physics) pour voir les formes de collision à l'exécution.