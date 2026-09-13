---
brief: Dieses Handbuch beschreibt, wie du 2D-Grafiken importierst und verwendest.
github: https://github.com/defold/doc
layout: manual
locale: de
title: 2D-Grafiken importieren und verwenden
toc:
- anchor: importing-2d-graphics
  title: 2D-Grafiken importieren
- anchor: creating-defold-assets
  title: Defold-Assets erstellen
- anchor: using-defold-assets
  title: Defold-Assets verwenden
---

# 2D-Grafiken importieren {#importing-2d-graphics}

Defold unterstützt viele Arten visueller Komponenten (components), die häufig in 2D-Spielen verwendet werden. Mit Defold kannst du statische und animierte Sprites, UI-Komponenten, Partikeleffekte, Kachelkarten (tile maps) und Bitmap-Schriften erstellen. Bevor du eine dieser visuellen Komponenten erstellen kannst, musst du Bilddateien mit den gewünschten Grafiken importieren. Ziehe dazu einfach die Dateien aus dem Dateisystem deines Computers an eine geeignete Stelle im Bereich *Assets* des Defold-Editors und lege sie dort ab.

![Dateien importieren](/manuals/images/graphics/import.png)

<div class='sidenote' markdown='1'>
Defold unterstützt Bilder in den Formaten PNG und JPEG. Andere Bildformate musst du vor der Verwendung konvertieren.
</div>


## Defold-Assets erstellen {#creating-defold-assets}

Nachdem du die Bilder in Defold importiert hast, kannst du daraus Defold-spezifische Assets erstellen:

![Atlas](/manuals/images/icons/atlas.png) Atlas
: Ein Atlas enthält eine Liste einzelner Bilddateien, die automatisch zu einem größeren Texturbild zusammengefügt werden. Atlanten können unbewegte Bilder und *Animationsgruppen (Animation Groups)* enthalten. Das sind Bildfolgen, die zusammen eine Flipbook-Animation bilden.

  ![Atlas](/manuals/images/graphics/atlas.png)

Mehr über die Atlas-Ressource erfährst du im [Atlas-Handbuch](/de/manuals/atlas).

![Kachelquelle](/manuals/images/icons/tilesource.png) Kachelquelle
: Eine Kachelquelle (tile source) verweist auf eine Bilddatei, die bereits aus kleineren Teilbildern besteht, die in einem gleichmäßigen Raster angeordnet sind. Ein weiterer gebräuchlicher Begriff für diese Art zusammengesetzter Bilder ist _Sprite-Bogen (sprite sheet)_. Kachelquellen können Flipbook-Animationen enthalten, die durch die erste und letzte Kachel der Animation definiert werden. Du kannst außerdem ein Bild verwenden, um Kacheln automatisch Kollisionsformen zuzuordnen.

  ![Kachelquelle](/manuals/images/graphics/tilesource.png)

Mehr über die Kachelquellen-Ressource erfährst du im [Handbuch zu Kachelquellen](/de/manuals/tilesource).

![Bitmap-Schrift](/manuals/images/icons/font.png) Bitmap-Schrift
: Bei einer Bitmap-Schrift (bitmap font) befinden sich die Glyphen in einem PNG-Schriftbogen. Diese Schriftarten bieten keinen Leistungsvorteil gegenüber Schriftarten, die aus TrueType- oder OpenType-Schriftdateien erzeugt werden. Sie können jedoch beliebige Grafiken, Farben und Schatten direkt im Bild enthalten.

Mehr über Bitmap-Schriften erfährst du im [Handbuch zu Schriftarten](/de/manuals/font/#bitmap-bmfonts).

  ![BMfont](/manuals/images/font/bm_font.png)


## Defold-Assets verwenden {#using-defold-assets}

Wenn du die Bilder in Atlas- und Kachelquellendateien umgewandelt hast, kannst du daraus verschiedene Arten visueller Komponenten erstellen:

![Sprite](/manuals/images/icons/sprite.png)
: Ein Sprite ist entweder ein statisches Bild oder eine Flipbook-Animation, die auf dem Bildschirm angezeigt wird.

  ![Sprite](/manuals/images/graphics/sprite.png)

Mehr über Sprites erfährst du im [Sprite-Handbuch](/de/manuals/sprite).

![Kachelkarte](/manuals/images/icons/tilemap.png) Kachelkarte
: Eine Kachelkartenkomponente setzt eine Karte aus Kacheln (Bild und Kollisionsformen) zusammen, die aus einer Kachelquelle stammen. Kachelkarten können keine Atlanten als Quelle verwenden.

  ![Kachelkarte](/manuals/images/graphics/tilemap.png)

Mehr über Kachelkarten erfährst du im [Handbuch zu Kachelkarten](/de/manuals/tilemap).

![Partikeleffekt](/manuals/images/icons/particlefx.png) Partikeleffekt
: Partikel, die ein Partikelemitter erzeugt, bestehen aus einem unbewegten Bild oder einer Flipbook-Animation aus einem Atlas oder einer Kachelquelle.

  ![Partikel](/manuals/images/graphics/particles.png)

Mehr über Partikeleffekte erfährst du im [Handbuch zu Partikeleffekten](/de/manuals/particlefx).

![GUI](/manuals/images/icons/gui.png) GUI
: Box-Knoten und Kreissektor-Knoten einer GUI können unbewegte Bilder und Flipbook-Animationen aus Atlanten und Kachelquellen verwenden.

  ![GUI](/manuals/images/graphics/gui.png)

Mehr über GUIs erfährst du im [GUI-Handbuch](/de/manuals/gui).