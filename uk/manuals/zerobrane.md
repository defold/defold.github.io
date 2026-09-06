---
brief: Цей посібник пояснює, як використовувати ZeroBrane Studio для налагодження коду Lua в Defold.
github: https://github.com/defold/doc
layout: manual
locale: uk
title: Налагодження за допомогою ZeroBrane Studio
toc:
- anchor: debugging-lua-scripts-with-zerobrane-studio
  title: Налагодження скриптів Lua за допомогою ZeroBrane Studio
- anchor: zerobrane-configuration
  title: Конфігурація ZeroBrane
- anchor: to-set-up-zerobrane
  title: Налаштування ZeroBrane
- anchor: starting-the-debugging-server
  title: Запуск сервера налагодження
- anchor: connecting-your-application-to-the-debugger
  title: Підключення застосунку до налагоджувача
- anchor: remote-debugging
  title: Віддалене налагодження
- anchor: other-recommended-zerobrane-setting
  title: Інше рекомендоване налаштування ZeroBrane
---

# Налагодження скриптів Lua за допомогою ZeroBrane Studio {#debugging-lua-scripts-with-zerobrane-studio}

Defold містить вбудований налагоджувач, але як зовнішній налагоджувач також можна використовувати безкоштовне середовище розробки Lua з відкритим вихідним кодом _ZeroBrane Studio_. Щоб користуватися функціями налагодження, потрібно встановити ZeroBrane Studio. Програма є кросплатформною та працює як на macOS, так і на Windows.

Завантажте «ZeroBrane Studio» з http://studio.zerobrane.com

## Конфігурація ZeroBrane {#zerobrane-configuration}

Щоб ZeroBrane міг знаходити файли вашого проєкту, потрібно вказати шлях до каталогу проєкту Defold. Зручний спосіб дізнатися цей шлях — скористатися пунктом <kbd>Show in Desktop</kbd> для файлу в корені проєкту Defold.

1. Клацніть правою кнопкою миші на *game.project*
2. Виберіть <kbd>Show in Desktop</kbd>

![Показати у Finder](/manuals/images/zerobrane/show_in_desktop.png)

## Налаштування ZeroBrane {#to-set-up-zerobrane}

Щоб налаштувати ZeroBrane, виберіть <kbd>Project ▸ Project Directory ▸ Choose...</kbd>:

![Налаштування](/manuals/images/zerobrane/setup.png)

Коли ви вкажете каталог поточного проєкту Defold, у ZeroBrane має з’явитися дерево каталогів проєкту Defold, у якому можна переходити між каталогами та відкривати файли.

Інші рекомендовані, але необов’язкові зміни конфігурації наведено далі в цьому документі.

## Запуск сервера налагодження {#starting-the-debugging-server}

Перш ніж почати сеанс налагодження, потрібно запустити вбудований сервер налагодження ZeroBrane. Відповідний пункт розташований у меню <kbd>Project</kbd>. Просто виберіть <kbd>Project ▸ Start Debugger Server</kbd>:

![Запуск налагоджувача](/manuals/images/zerobrane/startdebug.png)

## Підключення застосунку до налагоджувача {#connecting-your-application-to-the-debugger}

Налагодження можна розпочати будь-коли протягом роботи застосунку Defold, але його потрібно явно ініціювати зі скрипту Lua. Код Lua для початку сеансу налагодження має такий вигляд:

<div class='sidenote' markdown='1'>
Якщо гра завершує роботу під час виклику `dbg.start()`, можливо, ZeroBrane виявив проблему й надсилає грі команду завершення роботи. З якоїсь причини ZeroBrane потребує відкритого файлу для початку сеансу налагодження, інакше він виведе:
"Can't start debugging without an opened file or with the current file not being saved 'untitled.lua')."
Щоб виправити цю помилку, відкрийте в ZeroBrane файл, до якого ви додали `dbg.start()`.
</div>

```lua
dbg = require "builtins.scripts.mobdebug"
dbg.start()
```

Після вставлення наведеного вище коду застосунок підключиться до сервера налагодження ZeroBrane (типово через "localhost") і призупинить виконання перед наступною інструкцією.

```txt
Debugger server started at localhost:8172.
Mapped remote request for '/' to '/Users/my_user/Documents/Projects/Defold_project/'.
Debugging session started in '/Users/my_user/Documents/Projects/Defold_project'.
```

Тепер можна користуватися функціями налагодження ZeroBrane: виконувати код покроково, інспектувати його, додавати й видаляти точки зупину тощо.

<div class='sidenote' markdown='1'>
Налагодження буде ввімкнено лише для того контексту Lua, з якого його ініційовано. Якщо ввімкнути "shared_state" у *game.project*, можна налагоджувати весь застосунок незалежно від того, звідки ви почали.
</div>

![Покрокове виконання](/manuals/images/zerobrane/code.png)

Якщо спроба підключення не вдасться (наприклад, через те, що сервер налагодження не запущено), після цієї спроби застосунок продовжить працювати у звичайному режимі.

## Віддалене налагодження {#remote-debugging}

Оскільки налагодження відбувається через звичайні мережеві з’єднання (TCP), його можна виконувати віддалено. Це означає, що ви можете налагоджувати застосунок, коли він працює на мобільному пристрої.

Змінити потрібно лише команду, що запускає налагодження. Типово `start()` намагається підключитися до localhost, але для віддаленого налагодження потрібно вручну вказати адресу сервера налагодження ZeroBrane, як показано нижче:

```lua
dbg = require "builtins.scripts.mobdebug"
dbg.start("192.168.5.101")
```

Також важливо переконатися, що віддалений пристрій має мережеве з’єднання із сервером, а всі брандмауери чи подібне програмне забезпечення пропускають TCP-з’єднання через порт 8172. Інакше застосунок може зависнути під час запуску, намагаючись підключитися до сервера налагодження.

## Інше рекомендоване налаштування ZeroBrane {#other-recommended-zerobrane-setting}

ZeroBrane можна налаштувати так, щоб він автоматично відкривав файли скриптів Lua під час налагодження. Це дає змогу під час покрокового виконання заходити у функції в інших вихідних файлах без потреби відкривати їх вручну.

Спершу потрібно відкрити файл конфігурації редактора. Рекомендовано змінювати користувацьку версію цього файлу.

- Виберіть <kbd>Edit ▸ Preferences ▸ Settings: User</kbd>
- Додайте до файлу конфігурації:

  ```txt
  - to automatically open files requested during debugging
  editor.autoactivate = true
  ```

- Перезапустіть ZeroBrane

![Інші рекомендовані налаштування](/manuals/images/zerobrane/otherrecommended.png)