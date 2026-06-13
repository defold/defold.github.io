---
brief: Este manual explica cómo importar y usar gráficos 2D.
github: https://github.com/defold/doc
layout: manual
locale: es
title: Importación y uso de gráficos 2D
toc:
- Importación de gráficos 2D
- Crear assets de Defold
- Usar assets de Defold
---

# Importación de gráficos 2D

Defold admite muchos tipos de componentes visuales que se usan frecuentemente en juegos 2D. Puedes usar Defold para crear sprites estáticos y animados, componentes de interfaz, efectos de partículas, tile maps y fuentes bitmap. Antes de poder crear cualquiera de estos componentes visuales, debes importar archivos de imagen con los gráficos que quieras usar. Para importar archivos de imagen, simplemente arrastra los archivos desde el sistema de archivos de tu computadora y suéltalos en una ubicación adecuada del panel *Assets* del editor Defold.

![Importando archivos](/manuals/images/graphics/import.png)

<div class='sidenote' markdown='1'>
Defold admite imágenes en los formatos PNG y JPEG. Otros formatos de imagen deben convertirse antes de poder usarse.
</div>


## Crear assets de Defold

Cuando las imágenes se importan en Defold, pueden usarse para crear assets específicos de Defold:

![atlas](/manuals/images/icons/atlas.png) Atlas
: Un atlas contiene una lista de archivos de imagen separados, que se combinan automáticamente en una imagen de textura más grande. Los atlas pueden contener imágenes estáticas y *Animation Groups*, conjuntos de imágenes que juntas forman una animación flipbook.

  ![atlas](/manuals/images/graphics/atlas.png)

Aprende más sobre el recurso atlas en el [manual de Atlas](/es/manuals/atlas).

![tile source](/manuals/images/icons/tilesource.png) Tile Source
: Un tile source hace referencia a un archivo de imagen que ya está compuesto por subimágenes más pequeñas ordenadas en una rejilla uniforme. Otro término usado comúnmente para este tipo de imagen compuesta es _sprite sheet_. Los tile sources pueden contener animaciones flipbook, definidas por el primer y el último tile de la animación. También es posible usar una imagen para adjuntar automáticamente formas de colisión a los tiles.

  ![tile source](/manuals/images/graphics/tilesource.png)

Aprende más sobre el recurso tile source en el [manual de Tile source](/es/manuals/tilesource).

![bitmap font](/manuals/images/icons/font.png) Bitmap Font
: Una fuente bitmap tiene sus glifos en una hoja de fuente PNG. Estos tipos de fuentes no ofrecen ninguna mejora de rendimiento frente a fuentes generadas desde archivos de fuente TrueType u OpenType, pero pueden incluir gráficos arbitrarios, coloración y sombras directamente en la imagen.

Aprende más sobre las fuentes bitmap en el [manual de Fuentes](/es/manuals/font/#bitmap-bmfonts).

  ![BMfont](/manuals/images/font/bm_font.png)


## Usar assets de Defold

Cuando hayas convertido las imágenes en archivos Atlas y Tile Source, puedes usarlos para crear varios tipos distintos de componentes visuales:

![sprite](/manuals/images/icons/sprite.png)
: Un sprite es una imagen estática o una animación flipbook que se muestra en pantalla.

  ![sprite](/manuals/images/graphics/sprite.png)

Aprende más sobre sprites en el [manual de Sprite](/es/manuals/sprite).

![tile map](/manuals/images/icons/tilemap.png) Tile map
: Un componente tilemap compone un mapa a partir de tiles (imágenes y formas de colisión) que provienen de un tile source. Los tile maps no pueden usar atlas como fuente.

  ![tilemap](/manuals/images/graphics/tilemap.png)

Aprende más sobre tilemaps en el [manual de Tilemap](/es/manuals/tilemap).

![particle effect](/manuals/images/icons/particlefx.png) Particle fx
: Las partículas que se generan desde un emisor de partículas están compuestas por una imagen estática o una animación flipbook de un atlas o un tile source.

  ![particles](/manuals/images/graphics/particles.png)

Aprende más sobre efectos de partículas en el [manual de Particle fx](/es/manuals/particlefx).

![gui](/manuals/images/icons/gui.png) GUI
: Los nodos caja GUI y los nodos Pie pueden usar imágenes estáticas y animaciones flipbook de atlas y tile sources.

  ![gui](/manuals/images/graphics/gui.png)

Aprende más sobre GUIs en el [manual de GUI](/es/manuals/gui).