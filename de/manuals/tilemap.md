---
brief: Dieses Handbuch beschreibt Defolds Unterstützung für Kachelkarten im Detail.
github: https://github.com/defold/doc
layout: manual
locale: de
title: Defold-Handbuch zu Kachelkarten
toc:
- anchor: tile-map
  title: Kachelkarte
- anchor: creating-a-tile-map
  title: Eine Kachelkarte erstellen
- anchor: adding-a-tile-map-to-your-game
  title: Deinem Spiel eine Kachelkarte hinzufügen
- anchor: runtime-manipulation
  title: Änderungen zur Laufzeit
- anchor: changing-tiles-from-script
  title: Kacheln aus einem Skript ändern
- anchor: tilemap-properties
  title: Eigenschaften von Kachelkarten
- anchor: blend-modes
  title: Mischmodi
- anchor: changing-properties
  title: Eigenschaften ändern
- anchor: material-constants
  title: Materialkonstanten
- anchor: project-configuration
  title: Projektkonfiguration
- anchor: external-tools
  title: Externe Werkzeuge
- Tiled
- Tilesetter
---

# Kachelkarte {#tile-map}

Eine *Kachelkarte* (tile map) ist eine Komponente (component), mit der du Kacheln aus einer *Kachelquelle* (tile source) auf einer großen Rasterfläche anordnen oder aufmalen kannst. Kachelkarten werden häufig verwendet, um die Umgebung von Spielleveln zu gestalten. Du kannst auch die *Kollisionsformen* (collision shapes) aus der Kachelquelle in deinen Karten für die Kollisionserkennung und Physiksimulation verwenden ([Beispiel](/examples/tilemap/collisions/)).

Bevor du eine Kachelkarte erstellen kannst, musst du eine Kachelquelle erstellen. Im [Handbuch zu Kachelquellen](/de/manuals/tilesource) erfährst du, wie du eine Kachelquelle erstellst.

## Eine Kachelkarte erstellen {#creating-a-tile-map}

So erstellst du eine neue Kachelkarte:

- <kbd>Klicke mit der rechten Maustaste</kbd> auf eine Stelle im *Assets*-Browser und wähle dann <kbd>New... ▸ Tile Map</kbd>.
- Gib der Datei einen Namen.
- Die neue Kachelkarte wird automatisch im Kachelkarteneditor geöffnet.

  ![Neue Kachelkarte](/manuals/images/tilemap/tilemap.png)

- Setze die Eigenschaft *Tile Source* auf eine Kachelquellendatei, die du vorbereitet hast.

So malst du Kacheln auf deine Kachelkarte:

1. Wähle eine Ebene (*Layer*) zum Bemalen in der Ansicht *Outline* aus oder erstelle eine.
2. Wähle eine Kachel als Pinsel aus (drücke <kbd>Space</kbd>, um die Kachelpalette anzuzeigen), oder wähle durch Klicken und Ziehen in der Palette mehrere Kacheln aus, um einen rechteckigen Pinsel aus mehreren Kacheln zu erstellen.

   ![Palette](/manuals/images/tilemap/palette.png)

3. Male mit dem ausgewählten Pinsel. Um eine Kachel zu löschen, wähle entweder eine leere Kachel aus und verwende sie als Pinsel oder wähle den Radierer aus (<kbd>Edit ▸ Select Eraser</kbd>).

   ![Kacheln malen](/manuals/images/tilemap/paint_tiles.png)

Du kannst Kacheln direkt aus einer Ebene aufnehmen und die Auswahl als Pinsel verwenden. Halte <kbd>Shift</kbd> gedrückt und klicke auf eine Kachel, um sie als aktuellen Pinsel aufzunehmen. Während du <kbd>Shift</kbd> gedrückt hältst, kannst du auch durch Klicken und Ziehen einen Block aus Kacheln auswählen, den du als größeren Pinsel verwendest. Auf ähnliche Weise kannst du Kacheln ausschneiden, indem du <kbd>Shift+Ctrl</kbd> gedrückt hältst, oder sie löschen, indem du <kbd>Shift+Alt</kbd> gedrückt hältst.

Verwende <kbd>Z</kbd>, um den Pinsel im Uhrzeigersinn zu drehen. Verwende <kbd>X</kbd>, um den Pinsel horizontal zu spiegeln, und <kbd>Y</kbd>, um ihn vertikal zu spiegeln.

![Kacheln aufnehmen](/manuals/images/tilemap/pick_tiles.png)

## Deinem Spiel eine Kachelkarte hinzufügen {#adding-a-tile-map-to-your-game}

So fügst du deinem Spiel eine Kachelkarte hinzu:

1. Erstelle ein Spielobjekt (game object), das die Kachelkartenkomponente aufnehmen soll. Das Spielobjekt kann sich in einer Datei befinden oder direkt in einer Sammlung (collection) erstellt werden.
2. Klicke mit der rechten Maustaste auf den Wurzeleintrag des Spielobjekts und wähle <kbd>Add Component File</kbd>.
3. Wähle die Kachelkartendatei aus.

![Kachelkarte verwenden](/manuals/images/tilemap/use_tilemap.png)

## Änderungen zur Laufzeit {#runtime-manipulation}

Du kannst Kachelkarten zur Laufzeit über verschiedene Funktionen und Eigenschaften verändern (Informationen zur Verwendung findest du in der [API-Dokumentation](/ref/tilemap/)).

### Kacheln aus einem Skript ändern {#changing-tiles-from-script}

Du kannst den Inhalt einer Kachelkarte dynamisch lesen und schreiben, während dein Spiel läuft. Verwende dazu die Funktionen [`tilemap.get_tile()`](/ref/tilemap/#tilemap.get_tile) und [`tilemap.set_tile()`](/ref/tilemap/#tilemap.set_tile):

```lua
local tile = tilemap.get_tile("/level#map", "ground", x, y)

if tile == 2 then
    -- Replace grass-tile (2) with dangerous hole tile (number 4).
    tilemap.set_tile("/level#map", "ground", x, y, 4)
end
```

## Eigenschaften von Kachelkarten {#tilemap-properties}

Neben den Eigenschaften *Id*, *Position*, *Rotation* und *Scale* gibt es die folgenden komponentenspezifischen Eigenschaften:

*Tile Source*
: Die Kachelquellenressource, die für die Kachelkarte verwendet werden soll.

*Material*
: Das Material, das zum Rendern der Kachelkarte verwendet werden soll.

*Blend Mode*
: Der Mischmodus, der beim Rendern der Kachelkarte verwendet werden soll.

### Mischmodi {#blend-modes}
{% include shared/de/blend-modes.md %}

### Eigenschaften ändern {#changing-properties}

Eine Kachelkarte verfügt über verschiedene Eigenschaften, die mit `go.get()` und `go.set()` verändert werden können:

`tile_source`
: Die Kachelquelle der Kachelkarte (`hash`). Du kannst sie mit einer Ressourceneigenschaft für Kachelquellen und `go.set()` ändern. Ein Beispiel findest du in der [API-Referenz](/ref/tilemap/#tile_source).

`material`
: Das Material der Kachelkarte (`hash`). Du kannst es mit einer Ressourceneigenschaft für Materialien und `go.set()` ändern. Ein Beispiel findest du in der [API-Referenz](/ref/tilemap/#material).

### Materialkonstanten {#material-constants}

{% include shared/de/material-constants.md component='tilemap' variable='tint' %}

`tint`
: Die Einfärbung der Kachelkarte (`vector4`). Der `vector4` stellt die Einfärbung dar, wobei x, y, z und w den Anteilen für Rot, Grün, Blau und Alpha entsprechen.

## Projektkonfiguration {#project-configuration}

Die Datei *game.project* enthält einige [Projekteinstellungen](/de/manuals/project-settings#tilemap) für Kachelkarten.

## Externe Werkzeuge {#external-tools}

Es gibt externe Karten- und Leveleditoren, die direkt in Defold-Kachelkarten exportieren können:

### Tiled

[Tiled](https://www.mapeditor.org/) ist ein bekannter und weitverbreiteter Karteneditor für orthogonale, isometrische und hexagonale Karten. Tiled unterstützt eine breite Palette an Funktionen und kann [direkt nach Defold exportieren](https://doc.mapeditor.org/en/stable/manual/export-defold/). Mehr über den Export von Kachelkartendaten und zusätzlichen Metadaten erfährst du in [diesem Blogbeitrag des Defold-Nutzers „goeshard“](https://goeshard.org/2025/01/01/using-tiled-object-layers-with-defold-tilemaps/)


### Tilesetter

Mit [Tilesetter](https://www.tilesetter.org/docs/exporting#defold) kannst du automatisch vollständige Kachelsätze aus einfachen Basiskacheln erstellen. Außerdem enthält es einen Karteneditor, der direkt nach Defold exportieren kann.