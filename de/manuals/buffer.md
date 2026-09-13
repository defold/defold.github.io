---
brief: Dieses Handbuch erklärt, wie Pufferressourcen in Defold funktionieren.
github: https://github.com/defold/doc
layout: manual
locale: de
title: Handbuch zu Puffern
toc:
- anchor: buffer
  title: Puffer
---

# Puffer {#buffer}

Die Pufferressource (Buffer resource) beschreibt einen oder mehrere Datenströme von Werten, beispielsweise Positionen oder Farben. Jeder Datenstrom enthält einen Namen, einen Datentyp, eine Anzahl sowie die Daten selbst. Beispiel:

```
[
  {
    "name": "position",
    "type": "float32",
    "count": 3,
    "data": [
      -1.0,
      -1.0,
      -1.0,
      -1.0,
      -1.0,
      1.0,
      ...
    ]
  }
]
```

Das obige Beispiel beschreibt einen Datenstrom von Positionen in drei Dimensionen, dargestellt als 32-Bit-Gleitkommazahlen. Eine Pufferdatei verwendet das JSON-Format und die Dateierweiterung `.buffer`.

Pufferressourcen werden üblicherweise mit externen Werkzeugen oder Skripten erstellt, beispielsweise beim Export aus Modellierungswerkzeugen wie Blender. 

Du kannst eine Pufferressource als Eingabe für eine [Mesh-Komponente (mesh component)](/de/manuals/mesh) verwenden. Pufferressourcen können auch zur Laufzeit mit `buffer.create()` und [verwandten API-Funktionen](/ref/stable/buffer/#buffer.create:element_count-declaration) erstellt werden.