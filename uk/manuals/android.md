---
brief: У цьому посібнику описано, як збирати й запускати застосунки Defold на пристроях Android
github: https://github.com/defold/doc
layout: manual
locale: uk
title: Розробка в Defold для платформи Android
toc:
- anchor: android-development
  title: Розробка для Android
- anchor: android-and-google-play-signing-process
  title: Процес підписування для Android і Google Play
- anchor: creating-a-keystore
  title: Створення сховища ключів
- anchor: creating-an-android-application-bundle
  title: Створення пакета застосунку Android
- anchor: installing-an-android-application-bundle
  title: Установлення пакета застосунку Android
- anchor: permissions
  title: Дозволи
- anchor: androidpermissioninternet-and-androidpermissionaccess_network_state-protection-level-normal
  title: 'android.permission.INTERNET і android.permission.ACCESS_NETWORK_STATE (рівень захисту: normal)'
- anchor: androidpermissionwake_lock-protection-level-normal
  title: 'android.permission.WAKE_LOCK (рівень захисту: normal)'
- anchor: using-androidx
  title: Використання AndroidX
- anchor: faq
  title: Поширені запитання
---

# Розробка для Android {#android-development}

На пристроях Android можна вільно запускати власні застосунки. Зібрати версію гри та скопіювати її на пристрій Android дуже просто. У цьому посібнику пояснено кроки пакування гри для Android. Під час розробки часто зручніше запускати гру через [застосунок для розробки](/uk/manuals/dev-app), оскільки він дає змогу виконувати гаряче перезавантаження вмісту й коду безпосередньо на пристрої.

## Процес підписування для Android і Google Play {#android-and-google-play-signing-process}

Android вимагає, щоб усі APK були підписані цифровим підписом із використанням сертифіката перед установленням або оновленням на пристрої. Якщо ви використовуєте Android App Bundles, потрібно підписати лише пакет застосунку перед завантаженням у Play Console, а про решту подбає [Play App Signing](https://developer.android.com/studio/publish/app-signing#app-signing-google-play). Однак ви також можете вручну підписати застосунок для завантаження в Google Play, інші магазини застосунків або для розповсюдження поза магазинами.

Коли ви створюєте пакет застосунку Android у редакторі Defold або за допомогою [засобу командного рядка](/uk/manuals/bob), можна вказати сховище ключів (keystore), що містить ваш сертифікат і ключ, та пароль до нього. Їх буде використано для підписування застосунку. Якщо цього не зробити, Defold створить налагоджувальне сховище ключів і використає його для підписування пакета застосунку.

<div class='important' markdown='1'>
**Ніколи** не завантажуйте застосунок у Google Play, якщо його підписано за допомогою налагоджувального сховища ключів. Завжди використовуйте окреме сховище ключів, яке ви створили самостійно.
</div>

## Створення сховища ключів {#creating-a-keystore}

<div class='sidenote' markdown='1'>
Defold використовує сховище ключів для підписування застосунків Android. [Докладнішу інформацію наведено в цьому дописі на форумі](https://forum.defold.com/t/upcoming-change-to-the-android-build-pipeline/66084).
</div>

Сховище ключів можна створити [за допомогою Android Studio](https://developer.android.com/studio/publish/app-signing#generate-key) або в терміналі чи командному рядку:

```bash
keytool -genkey -v -noprompt -dname "CN=John Smith, OU=Area 51, O=US Air Force, L=Unknown, ST=Nevada, C=US" -keystore mykeystore.keystore -storepass 5Up3r_53cR3t -alias myAlias -keyalg RSA -validity 9125
```

Ця команда створить файл сховища ключів із назвою `mykeystore.keystore`, що міститиме ключ і сертифікат. Доступ до ключа й сертифіката буде захищено паролем `5Up3r_53cR3t`. Ключ і сертифікат будуть дійсними протягом 25 років (9125 днів). Створені ключ і сертифікат матимуть псевдонім `myAlias`.

<div class='important' markdown='1'>
Обов’язково зберігайте сховище ключів і відповідний пароль у безпечному місці. Якщо ви самостійно підписуєте й завантажуєте застосунки в Google Play та втратите сховище ключів або пароль до нього, ви не зможете оновити застосунок у Google Play. Щоб уникнути цього, можна скористатися Google Play App Signing і доручити Google підписувати ваші застосунки.
</div>


## Створення пакета застосунку Android {#creating-an-android-application-bundle}

У редакторі можна легко створити самостійний пакет застосунку для вашої гри. Перед пакуванням можна вказати піктограми застосунку, задати код версії тощо у [файлі налаштувань проєкту](/uk/manuals/project-settings/#android) *game.project*.

Щоб створити пакет, виберіть у меню <kbd>Project ▸ Bundle... ▸ Android Application...</kbd>.

Якщо ви хочете, щоб редактор автоматично створював випадкові налагоджувальні сертифікати, залиште поля *Keystore* і *Keystore password* порожніми:

![Підписування пакета Android](/manuals/images/android/sign_bundle.png)

Якщо ви хочете підписати пакет за допомогою певного сховища ключів, укажіть *Keystore* і *Keystore password*. Файл *Keystore* повинен мати розширення `.keystore`, а пароль має зберігатися в текстовому файлі з розширенням `.txt`. Також можна вказати *Key password*, якщо ключ у сховищі має інший пароль, ніж саме сховище:

![Підписування пакета Android](/manuals/images/android/sign_bundle2.png)

Defold підтримує створення файлів APK і AAB. Виберіть APK або AAB у розкривному списку *Bundle Format*.

Після налаштування пакета застосунку натисніть <kbd>Create Bundle</kbd>. Після цього вам буде запропоновано вказати місце на комп’ютері, де буде створено пакет.

![Файл пакета застосунку Android](/manuals/images/android/apk_file.png)

{% include shared/uk/build-variants.md %}

### Установлення пакета застосунку Android {#installing-an-android-application-bundle}

#### Установлення APK {#installing-an-apk}

Файл *`.apk`* можна скопіювати на пристрій за допомогою засобу `adb` або завантажити в Google Play через [консоль розробника Google Play](https://play.google.com/apps/publish/).

{% include shared/uk/android-adb.md %}

```
$ adb install Defold\ examples.apk
4826 KB/s (18774344 bytes in 3.798s)
  pkg: /data/local/tmp/my_app.apk
Success
```

#### Установлення APK за допомогою редактора {#installing-an-apk-using-editor}

Ви можете встановити й запустити файл *`.apk`* за допомогою прапорців «Install on connected device» і «Launch installed app» у діалоговому вікні Bundle редактора:

![Установлення та запуск APK](/manuals/images/android/install_and_launch.png)

Для роботи цієї функції потрібно встановити *ADB* й увімкнути *USB debugging* на під’єднаному пристрої. Якщо редактор не може визначити місце встановлення засобу командного рядка ADB, його потрібно вказати в [Preferences](/uk/manuals/editor-preferences/#tools).

#### Установлення AAB {#installing-an-aab}

Файл *.aab* можна завантажити в Google Play через [консоль розробника Google Play](https://play.google.com/apps/publish/). Також можна створити файл *`.apk`* із файлу *.aab* для локального встановлення за допомогою [Android bundletool](https://developer.android.com/studio/command-line/bundletool).

## Дозволи {#permissions}

Для роботи всіх функцій рушію Defold потрібна низка дозволів. Дозволи визначено в `AndroidManifest.xml`, указаному у [файлі налаштувань проєкту](/uk/manuals/project-settings/#android) *game.project*. Докладніше про дозволи Android можна прочитати в [офіційній документації](https://developer.android.com/guide/topics/permissions/overview). Стандартний маніфест запитує такі дозволи:

### android.permission.INTERNET і android.permission.ACCESS_NETWORK_STATE (рівень захисту: normal) {#androidpermissioninternet-and-androidpermissionaccess_network_state-protection-level-normal}
Дають застосункам змогу відкривати *мережеві сокети* й отримувати інформацію про мережі. Ці дозволи потрібні для доступу до інтернету. ([Офіційна документація Android](https://developer.android.com/reference/android/Manifest.permission#INTERNET)) і ([Офіційна документація Android](https://developer.android.com/reference/android/Manifest.permission#ACCESS_NETWORK_STATE)).

### android.permission.WAKE_LOCK (рівень захисту: normal) {#androidpermissionwake_lock-protection-level-normal}
Дає змогу використовувати PowerManager WakeLocks, щоб запобігати переходу процесора в режим сну або затемненню екрана. Цей дозвіл потрібний, щоб тимчасово запобігати переходу пристрою в режим сну під час отримання push-сповіщення. ([Офіційна документація Android](https://developer.android.com/reference/android/Manifest.permission#WAKE_LOCK))


## Використання AndroidX {#using-androidx}
AndroidX — це значне вдосконалення початкової бібліотеки Android Support Library, яка більше не підтримується. Пакети AndroidX повністю замінюють Support Library, забезпечуючи ті самі можливості та пропонуючи нові бібліотеки. Більшість розширень Android на [порталі ресурсів](/assets) підтримують AndroidX. Якщо ви не хочете використовувати AndroidX, ви можете явно вимкнути його на користь старої Android Support Library, установивши прапорець `Use Android Support Lib` у [маніфесті застосунку](https://defold.com/uk/manuals/app-manifest/).

![](/manuals/images/android/enable_supportlibrary.png)

## Поширені запитання {#faq}
{% include shared/uk/android-faq.md %}