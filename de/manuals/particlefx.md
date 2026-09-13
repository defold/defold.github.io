---
brief: Dieses Handbuch erklärt, wie die Partikeleffektkomponente funktioniert und wie du sie bearbeitest, um visuelle Partikeleffekte zu erstellen.
github: https://github.com/defold/doc
layout: manual
locale: de
title: Partikeleffekte in Defold
toc:
- anchor: particle-fx
  title: Partikeleffekte
- anchor: creating-an-effect
  title: Einen Effekt erstellen
- anchor: previewing-an-effect
  title: Vorschau eines Effekts
- anchor: emitter-properties
  title: Emittereigenschaften
- anchor: blend-modes
  title: Mischmodi
- anchor: keyable-emitter-properties
  title: Über Kurven animierbare Emittereigenschaften
- anchor: modifiers
  title: Modifikatoren
- anchor: modifier-properties
  title: Modifikatoreigenschaften
- anchor: controlling-a-particle-effect
  title: Einen Partikeleffekt steuern
- anchor: material-constants
  title: Materialkonstanten
- anchor: project-configuration
  title: Projektkonfiguration
---

# Partikeleffekte {#particle-fx}

Partikeleffekte (particle effects) werden verwendet, um Spiele visuell aufzuwerten. Du kannst damit Explosionen, Blutspritzer, Spuren, Wetter oder beliebige andere Effekte erzeugen.

![Partikeleffekt-Editor](/manuals/images/particlefx/editor.png)

Partikeleffekte bestehen aus mehreren Emittern und optionalen Modifikatoren (modifiers):

Emitter
: Ein Emitter ist eine positionierte Form, die gleichmäßig über die Form verteilte Partikel erzeugt. Der Emitter enthält Eigenschaften, die die Partikelerzeugung sowie das Bild oder die Animation, die Lebensdauer, Farbe, Form und Geschwindigkeit der einzelnen Partikel steuern.

Modifikator
: Ein Modifikator beeinflusst die Geschwindigkeit erzeugter Partikel, sodass sie in eine bestimmte Richtung beschleunigen oder langsamer werden, sich radial bewegen oder um einen Punkt wirbeln. Modifikatoren können die Partikel eines einzelnen Emitters oder einen bestimmten Emitter beeinflussen.

## Einen Effekt erstellen {#creating-an-effect}

Wähle <kbd>New... ▸ Particle FX</kbd> im Kontextmenü des Browsers *Assets*. Gib der neuen Partikeleffektdatei einen Namen. Der Editor öffnet die Datei nun im [Szeneneditor](/de/manuals/editor/#the-scene-editor).

Der Bereich *Outline* zeigt den standardmäßig angelegten Emitter. Wähle den Emitter aus, um seine Eigenschaften im darunterliegenden Bereich *Properties* anzuzeigen.

![Standardpartikel](/manuals/images/particlefx/default.png)

Um dem Effekt einen neuen Emitter hinzuzufügen, <kbd>klicke mit der rechten Maustaste</kbd> auf die Wurzel in *Outline* und wähle <kbd>Add Emitter ▸ [type]</kbd> im Kontextmenü. Beachte, dass du den Typ des Emitters in den Emittereigenschaften ändern kannst.

Um einen neuen Modifikator hinzuzufügen, <kbd>klicke mit der rechten Maustaste</kbd> auf die Position des Modifikators in *Outline* (die Effektwurzel oder einen bestimmten Emitter) und wähle <kbd>Add Modifier</kbd>. Wähle anschließend den Modifikatortyp.

![Modifikator hinzufügen](/manuals/images/particlefx/add_modifier.png)

![Modifikator zum Hinzufügen auswählen](/manuals/images/particlefx/add_modifier_select.png)

Ein Modifikator an der Effektwurzel (der keinem Emitter untergeordnet ist) beeinflusst alle Partikel des Effekts.

Ein Modifikator, der einem Emitter als untergeordnetes Objekt hinzugefügt wird, beeinflusst nur diesen Emitter.

## Vorschau eines Effekts {#previewing-an-effect}

* Wähle <kbd>View ▸ Play</kbd> im Menü, um eine Vorschau des Effekts anzuzeigen. Möglicherweise musst du mit der Kamera herauszoomen, um den Effekt richtig zu sehen.
* Wähle erneut <kbd>View ▸ Play</kbd>, um den Effekt anzuhalten.
* Wähle <kbd>View ▸ Stop</kbd>, um den Effekt zu stoppen. Wenn du ihn erneut abspielst, beginnt er wieder in seinem Ausgangszustand.

Wenn du einen Emitter oder Modifikator bearbeitest, ist das Ergebnis sofort im Editor sichtbar, auch wenn der Effekt angehalten ist:

![Partikel bearbeiten](/manuals/images/particlefx/rotate.gif)

## Emittereigenschaften {#emitter-properties}

Id
: Bezeichner des Emitters (wird beim Setzen von Renderkonstanten für bestimmte Emitter verwendet).

Position/Rotation
: Transformation des Emitters relativ zur Partikeleffektkomponente (component).

Play Mode
: Steuert, wie der Emitter abgespielt wird:
  - `Once` stoppt den Emitter nach Ablauf seiner Dauer.
  - `Loop` startet den Emitter nach Ablauf seiner Dauer neu.

Size Mode
: Steuert, wie die Größe von Flipbook-Animationen festgelegt wird:
  - `Auto` behält für jedes Einzelbild der Flipbook-Animation die Größe des Quellbilds bei.
  - `Manual` legt die Partikelgröße anhand der Größeneigenschaft fest.

Emission Space
: Das geometrische Koordinatensystem, in dem die erzeugten Partikel existieren:
  - `World` bewegt die Partikel unabhängig vom Emitter.
  - `Emitter` bewegt die Partikel relativ zum Emitter.

Duration
: Die Anzahl der Sekunden, für die der Emitter Partikel erzeugen soll.

Start Delay
: Die Anzahl der Sekunden, die der Emitter warten soll, bevor er Partikel erzeugt.

Start Offset
: Die Anzahl der Sekunden innerhalb der Partikelsimulation, bei der der Emitter starten soll. Anders ausgedrückt: wie lange der Emitter den Effekt im Voraus simulieren soll.

Image
: Die Bilddatei (Kachelquelle oder Atlas), die zum Texturieren und Animieren der Partikel verwendet wird.

Animation
: Die Animation aus der Datei unter *Image*, die für die Partikel verwendet wird.

Material
: Das Material für das Shading der Partikel.

Blend Mode
: Die verfügbaren Mischmodi sind `Alpha`, `Add` und `Multiply`.

Max Particle Count
: Wie viele Partikel dieses Emitters gleichzeitig existieren können.

Emitter Type
: Die Form des Emitters
  - `Circle` erzeugt Partikel an einer zufälligen Position innerhalb eines Kreises. Die Partikel sind vom Mittelpunkt nach außen gerichtet. Der Kreisdurchmesser wird durch *Emitter Size X* festgelegt.

  - `2D Cone` erzeugt Partikel an einer zufälligen Position innerhalb eines flachen Kegels (eines Dreiecks). Die Partikel sind durch die Oberseite des Kegels nach außen gerichtet. *Emitter Size X* legt die Breite der Oberseite fest und *Y* die Höhe.

  - `Box` erzeugt Partikel an einer zufälligen Position innerhalb eines Quaders. Die Partikel sind entlang der lokalen Y-Achse des Quaders nach oben gerichtet. *Emitter Size X*, *Y* und *Z* legen jeweils Breite, Höhe und Tiefe fest. Für ein 2D-Rechteck lässt du die Z-Größe auf null.

  - `Sphere` erzeugt Partikel an einer zufälligen Position innerhalb einer Kugel. Die Partikel sind vom Mittelpunkt nach außen gerichtet. Der Kugeldurchmesser wird durch *Emitter Size X* festgelegt.

  - `Cone` erzeugt Partikel an einer zufälligen Position innerhalb eines 3D-Kegels. Die Partikel sind durch die obere Kreisscheibe des Kegels nach außen gerichtet. *Emitter Size X* legt den Durchmesser der oberen Kreisscheibe fest und *Y* die Höhe des Kegels.

  ![Emittertypen](/manuals/images/particlefx/emitter_types.png)

Particle Orientation
: Die Ausrichtung der erzeugten Partikel:
  - `Default` setzt die Ausrichtung auf die Einheitsausrichtung
  - `Initial Direction` behält die anfängliche Ausrichtung der erzeugten Partikel bei.
  - `Movement Direction` passt die Ausrichtung der Partikel an ihre Geschwindigkeit an.

Inherit Velocity
: Ein Skalierungsfaktor, der angibt, wie viel von der Geschwindigkeit des Emitters die Partikel übernehmen sollen. Dieser Wert ist nur verfügbar, wenn *Space* auf `World` gesetzt ist. Die Geschwindigkeit des Emitters wird in jedem Frame geschätzt.

Stretch With Velocity
: Aktiviere diese Option, um jede Partikelstreckung in Bewegungsrichtung zu skalieren.

### Mischmodi {#blend-modes}
{% include shared/de/blend-modes.md %}

## Über Kurven animierbare Emittereigenschaften {#keyable-emitter-properties}

Diese Eigenschaften haben zwei Felder: einen Wert und eine Streuung. Die Streuung ist eine Variation, die für jeden erzeugten Partikel zufällig angewendet wird. Wenn der Wert beispielsweise 50 und die Streuung 3 beträgt, erhält jeder erzeugte Partikel einen Wert zwischen 47 und 53 (50 +/- 3).

![Eigenschaft](/manuals/images/particlefx/property.png)

Wenn du die Schaltfläche mit dem Schlüsselsymbol aktivierst, wird der Eigenschaftswert über die Dauer des Emitters durch eine Kurve gesteuert. Um eine über eine Kurve gesteuerte Eigenschaft zurückzusetzen, deaktiviere die Schaltfläche mit dem Schlüsselsymbol.

![Eigenschaft mit Kurvensteuerung](/manuals/images/particlefx/key.png)

Der *Curve Editor* (verfügbar unter den Registerkarten in der unteren Ansicht) dient zum Bearbeiten der Kurve. Eigenschaften mit Kurvensteuerung können nicht in der Ansicht *Properties* bearbeitet werden, sondern nur im *Curve Editor*. Verändere die Form der Kurve, indem du die Punkte und Tangenten <kbd>anklickst und ziehst</kbd>. Füge durch <kbd>Doppelklicken</kbd> auf die Kurve Kontrollpunkte hinzu. Um einen Kontrollpunkt zu entfernen, <kbd>doppelklicke</kbd> darauf.

![Kurveneditor für Partikeleffekte](/manuals/images/particlefx/curve_editor.png)

Um den Zoom im Curve Editor automatisch so anzupassen, dass alle Kurven angezeigt werden, drücke <kbd>F</kbd>.

Die folgenden Eigenschaften können über die Wiedergabedauer des Emitters durch Kurven gesteuert werden:

Spawn Rate
: Die Anzahl der Partikel, die pro Sekunde erzeugt werden sollen.

Emitter Size X/Y/Z
: Die Abmessungen der Emitterform, siehe *Emitter Type* oben.

Particle Life Time
: Die Lebensdauer jedes erzeugten Partikels in Sekunden.

Initial Speed
: Die Anfangsgeschwindigkeit jedes erzeugten Partikels.

Initial Size
: Die Anfangsgröße jedes erzeugten Partikels. Wenn du *Size Mode* auf `Automatic` setzt und eine Flipbook-Animation als Bildquelle verwendest, wird diese Eigenschaft ignoriert.

Initial Red/Green/Blue/Alpha
: Die anfänglichen Werte der Farbkomponenten zur Einfärbung der Partikel.

Initial Rotation
: Die anfänglichen Drehungswerte (in Grad) der Partikel.

Initial Stretch X/Y
: Die anfänglichen Streckungswerte (in Einheiten) der Partikel.

Initial Angular Velocity
: Die anfängliche Winkelgeschwindigkeit (in Grad/Sekunde) jedes erzeugten Partikels.

Die folgenden Eigenschaften können über die Lebensdauer der Partikel durch Kurven gesteuert werden:

Life Scale
: Der Skalierungsfaktor über die Lebensdauer jedes Partikels.

Life Red/Green/Blue/Alpha
: Der Wert der Farbkomponente zur Einfärbung über die Lebensdauer jedes Partikels.

Life Rotation
: Der Drehungswert (in Grad) über die Lebensdauer jedes Partikels.

Life Stretch X/Y
: Der Streckungswert (in Einheiten) über die Lebensdauer jedes Partikels.

Life Angular Velocity
: Die Winkelgeschwindigkeit (in Grad/Sekunde) über die Lebensdauer jedes Partikels.

## Modifikatoren {#modifiers}

Es stehen vier Arten von Modifikatoren zur Verfügung, die die Geschwindigkeit der Partikel beeinflussen:

`Acceleration`
: Beschleunigung in eine allgemeine Richtung.

`Drag`
: Verringert die Beschleunigung der Partikel proportional zur Partikelgeschwindigkeit.

`Radial`
: Zieht Partikel entweder zu einer Position hin oder stößt sie von ihr ab.

`Vortex`
: Beeinflusst Partikel in einer kreisförmigen oder spiralförmigen Richtung um seine Position.

  ![Modifikatoren](/manuals/images/particlefx/modifiers.png)

## Modifikatoreigenschaften {#modifier-properties}

Position/Rotation
: Die Transformation des Modifikators relativ zu seinem übergeordneten Objekt.

Magnitude
: Die Stärke des Einflusses, den der Modifikator auf die Partikel hat.

Max Distance
: Die maximale Entfernung, innerhalb derer dieser Modifikator Partikel überhaupt beeinflusst. Wird nur für Radial und Vortex verwendet.

## Einen Partikeleffekt steuern {#controlling-a-particle-effect}

So startest und stoppst du einen Partikeleffekt aus einem Skript:

```lua
-- start the effect component "particles" in the current game object
particlefx.play("#particles")

-- stop the effect component "particles" in the current game object
particlefx.stop("#particles")
```

Weitere Informationen zum Starten und Stoppen eines Partikeleffekts aus einem GUI-Skript findest du im [Handbuch zu GUI-Partikeleffekten](/de/manuals/gui-particlefx#controlling-the-effect).

<div class='sidenote' markdown='1'>
Ein Partikeleffekt erzeugt weiterhin Partikel, auch wenn das Spielobjekt (game object), zu dem die Partikeleffektkomponente gehörte, gelöscht wird.
</div>
Weitere Informationen findest du in der [Referenzdokumentation zu Partikeleffekten](/ref/particlefx).

## Materialkonstanten {#material-constants}

Das Standardmaterial für Partikeleffekte hat die folgenden Konstanten, die du mit `particlefx.set_constant()` ändern und mit `particlefx.reset_constant()` zurücksetzen kannst (weitere Einzelheiten findest du im [Handbuch zu Materialien](/de/manuals/material/#vertex-and-fragment-constants)):

`tint`
: Die Einfärbung des Partikeleffekts (`vector4`). Der vector4 stellt die Einfärbung dar, wobei x, y, z und w den Rot-, Grün-, Blau- und Alphaanteilen der Einfärbung entsprechen. Ein Beispiel findest du in der [API-Referenz](/ref/particlefx/#particlefx.set_constant:url-constant-value).


## Projektkonfiguration {#project-configuration}

Die Datei *game.project* enthält einige [Projekteinstellungen](/de/manuals/project-settings#particle-fx) für Partikel.