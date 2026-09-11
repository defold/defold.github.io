---
brief: Ви можете додати власні шаблони проєктів до вікна New Project.
github: https://github.com/defold/doc
layout: manual
locale: uk
title: Шаблони редактора
toc:
- anchor: editor-templates
  title: Шаблони редактора
---

# Шаблони редактора {#editor-templates}

Ви можете додати власні шаблони проєктів до вікна New Project:

![власні шаблони проєктів](/manuals/images/editor/custom_project_templates.png)

Щоб додати одну або кілька нових вкладок із власними шаблонами проєктів, потрібно додати файл `welcome.edn` до папки `.defold` у домашній папці користувача:

* Створіть папку з назвою `.defold` у домашній папці користувача.
  * У Windows `C:\Users\**Your Username**\.defold`
  * У macOS `/Users/**Your Username**/.defold`
  * У Linux `~/.defold`
* Створіть файл `welcome.edn` у папці `.defold`

Файл `welcome.edn` використовує формат Extensible Data Notation. Приклад:

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

Це створить список шаблонів, показаний на знімку екрана вище.

<div class='sidenote' markdown='1'>
Можна використовувати лише зображення шаблонів, [що постачаються з редактором](https://github.com/defold/defold/tree/dev/editor/resources/welcome/images).
</div>