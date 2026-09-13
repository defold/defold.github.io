---
brief: Du kannst dem Fenster New Project eigene Projektvorlagen hinzufügen.
github: https://github.com/defold/doc
layout: manual
locale: de
title: Editor-Vorlagen
toc:
- anchor: editor-templates
  title: Editor-Vorlagen
---

# Editor-Vorlagen {#editor-templates}

Du kannst dem Fenster New Project eigene Projektvorlagen hinzufügen:

![eigene Projektvorlagen](/manuals/images/editor/custom_project_templates.png)

Um eine oder mehrere neue Registerkarten mit eigenen Projektvorlagen hinzuzufügen, musst du eine Datei `welcome.edn` im Ordner `.defold` in deinem Benutzerverzeichnis anlegen:

* Erstelle einen Ordner namens `.defold` in deinem Benutzerverzeichnis.
  * Unter Windows `C:\Users\**Your Username**\.defold`
  * Unter macOS `/Users/**Your Username**/.defold`
  * Unter Linux `~/.defold`
* Erstelle eine Datei `welcome.edn` im Ordner `.defold`

Die Datei `welcome.edn` verwendet das Format Extensible Data Notation. Beispiel:

```
{:new-project
  {:categories [
    {:label "My Templates"
     :templates [
          {:name "My project"
           :description "My template with everything set up the way I want it."
           :image "empty.svg"
           :zip-url "https://github.com/britzl/template-project/archive/master.zip"
           :skip-root? true},
          {:name "My other project"
           :description "My other template with everything set up the way I want it."
           :image "empty.svg"
           :zip-url "https://github.com/britzl/template-other-project/archive/master.zip"
           :skip-root? true}]
    }]
  }
}
```

Dadurch wird die Liste der Vorlagen erstellt, die du im Screenshot oben siehst.

<div class='sidenote' markdown='1'>
Du kannst nur die Vorlagenbilder verwenden, die [mit dem Editor geliefert werden](https://github.com/defold/defold/tree/dev/editor/resources/welcome/images).
</div>