---
brief: Цей посібник описує, як оптимізувати споживання заряду батареї у грі на Defold.
github: https://github.com/defold/doc
layout: manual
locale: uk
title: Оптимізація споживання заряду батареї у грі на Defold
toc:
- anchor: optimize-battery-usage
  title: Оптимізація споживання заряду батареї
- anchor: disable-accelerometer
  title: Вимкнення акселерометра
- anchor: platform-specific-optimizations
  title: Оптимізація для окремих платформ
- anchor: android-device-performance-framework
  title: Android Device Performance Framework
---

# Оптимізація споживання заряду батареї {#optimize-battery-usage}
Споживання заряду батареї має значення насамперед тоді, коли ви розробляєте гру для мобільних або портативних пристроїв. Високе навантаження на CPU або GPU швидко розряджає батарею та спричиняє перегрів пристрою.

Зверніться до посібників про [оптимізацію продуктивності гри під час виконання](/uk/manuals/optimization-speed), щоб дізнатися, як зменшити навантаження на CPU та GPU.

## Вимкнення акселерометра {#disable-accelerometer}
Якщо ви створюєте мобільну гру, яка не використовує акселерометр пристрою, рекомендовано [вимкнути його в *game.project*](/uk/manuals/project-settings/#use-accelerometer), щоб зменшити кількість генерованих подій введення.

# Оптимізація для окремих платформ {#platform-specific-optimizations}

## Android Device Performance Framework {#android-device-performance-framework}

Android Dynamic Performance Framework — це набір API, які дають іграм змогу безпосередніше взаємодіяти із системами живлення та керування температурою пристроїв Android. Можна відстежувати динамічну поведінку систем Android і оптимізувати продуктивність гри, підтримуючи її на рівні, що не спричиняє перегріву пристроїв. Використовуйте [розширення Android Dynamic Performance Framework](https://defold.com/extension-adpf/), щоб відстежувати та оптимізувати продуктивність вашої гри на Defold для пристроїв Android.