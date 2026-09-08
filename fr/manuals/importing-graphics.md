---
brief: Ce manuel explique comment importer et utiliser des graphismes 2D.
github: https://github.com/defold/doc
layout: manual
locale: fr
title: Importation et utilisation de graphismes 2D
toc:
- anchor: importing-2d-graphics
  title: Importation de graphismes 2D
- anchor: creating-defold-assets
  title: Création de ressources Defold
- anchor: using-defold-assets
  title: Utilisation des ressources Defold
---

# Importation de graphismes 2D {#importing-2d-graphics}

Defold prend en charge de nombreux types de composants (components) visuels fréquemment utilisés dans les jeux 2D. Vous pouvez utiliser Defold pour créer des sprites statiques et animés, des composants d'interface utilisateur, des effets de particules, des cartes de tuiles et des polices bitmap. Avant de pouvoir créer l'un de ces composants visuels, vous devez importer des fichiers image contenant les graphismes que vous souhaitez utiliser. Pour importer des fichiers image, il vous suffit de faire glisser les fichiers depuis le système de fichiers de votre ordinateur et de les déposer à l'emplacement approprié dans le *panneau Assets* de l'éditeur Defold.

![Importation de fichiers](/manuals/images/graphics/import.png)

<div class='sidenote' markdown='1'>
Defold prend en charge les images aux formats PNG et JPEG. Les autres formats d'image doivent être convertis avant de pouvoir être utilisés.
</div>


## Création de ressources Defold {#creating-defold-assets}

Une fois importées dans Defold, les images peuvent servir à créer des ressources propres à Defold :

![atlas](/manuals/images/icons/atlas.png) Atlas
: Un atlas contient une liste de fichiers image distincts, qui sont automatiquement réunis dans une image de texture plus grande. Les atlas peuvent contenir des images fixes et des *Animation Groups*, des ensembles d'images qui forment une animation image par image.

  ![atlas](/manuals/images/graphics/atlas.png)

Pour en savoir plus sur la ressource atlas, consultez le [manuel des atlas](/fr/manuals/atlas).

![source de tuiles](/manuals/images/icons/tilesource.png) Source de tuiles
: Une source de tuiles référence un fichier image déjà composé de sous-images plus petites disposées sur une grille régulière. Ce type d'image composite est aussi couramment appelé _planche de sprites_. Les sources de tuiles peuvent contenir des animations image par image, définies par la première et la dernière tuile de l'animation. Il est également possible d'utiliser une image pour associer automatiquement des formes de collision aux tuiles.

  ![source de tuiles](/manuals/images/graphics/tilesource.png)

Pour en savoir plus sur la ressource source de tuiles, consultez le [manuel des sources de tuiles](/fr/manuals/tilesource).

![police bitmap](/manuals/images/icons/font.png) Police bitmap
: Les glyphes d'une police bitmap sont regroupés dans une planche au format PNG. Ces types de polices n'améliorent pas les performances par rapport aux polices générées à partir de fichiers TrueType ou OpenType, mais peuvent inclure des graphismes, des couleurs et des ombres arbitraires directement dans l'image.

Pour en savoir plus sur les polices bitmap, consultez le [manuel des polices](/fr/manuals/font/#bitmap-bmfonts).

  ![BMfont](/manuals/images/font/bm_font.png)


## Utilisation des ressources Defold {#using-defold-assets}

Lorsque vous avez converti les images en fichiers d'atlas et de source de tuiles, vous pouvez les utiliser pour créer plusieurs types de composants visuels :

![sprite](/manuals/images/icons/sprite.png)
: Un sprite est une image statique ou une animation image par image qui s'affiche à l'écran.

  ![sprite](/manuals/images/graphics/sprite.png)

Pour en savoir plus sur les sprites, consultez le [manuel des sprites](/fr/manuals/sprite).

![carte de tuiles](/manuals/images/icons/tilemap.png) Tilemap
: Un composant tilemap assemble une carte à partir de tuiles (image et formes de collision) provenant d'une source de tuiles. Les tilemaps ne peuvent pas utiliser d'atlas comme source.

  ![tilemap](/manuals/images/graphics/tilemap.png)

Pour en savoir plus sur les tilemaps, consultez le [manuel des tilemaps](/fr/manuals/tilemap).

![effet de particules](/manuals/images/icons/particlefx.png) Effet de particules
: Les particules générées par un émetteur de particules sont constituées d'une image fixe ou d'une animation image par image provenant d'un atlas ou d'une source de tuiles.

  ![particules](/manuals/images/graphics/particles.png)

Pour en savoir plus sur les effets de particules, consultez le [manuel des effets de particules](/fr/manuals/particlefx).

![interface graphique](/manuals/images/icons/gui.png) GUI
: Les nœuds box et pie des interfaces graphiques peuvent utiliser des images fixes et des animations image par image provenant d'atlas et de sources de tuiles.

  ![interface graphique](/manuals/images/graphics/gui.png)

Pour en savoir plus sur les interfaces graphiques, consultez le [manuel des interfaces graphiques](/fr/manuals/gui).