---
brief: У цьому посібнику описано, як оптимізувати використання пам’яті в грі на Defold.
github: https://github.com/defold/doc
layout: manual
locale: uk
title: Оптимізація використання пам’яті в грі на Defold
toc:
- anchor: optimizing-memory-usage
  title: Оптимізація використання пам’яті
- anchor: texture-compression
  title: Стиснення текстур
- anchor: dynamic-loading
  title: Динамічне завантаження
- anchor: optimize-component-counters
  title: Оптимізація лічильників компонентів
- anchor: optimize-gui-node-count
  title: Оптимізація кількості вузлів GUI
---

# Оптимізація використання пам’яті {#optimizing-memory-usage}

## Стиснення текстур {#texture-compression}
Стиснення текстур не лише зменшить розмір ресурсів в архіві вашої гри, але й може зменшити обсяг пам’яті GPU, потрібний для зберігання текстур.

## Динамічне завантаження {#dynamic-loading}
У більшості ігор є принаймні певний вміст, який використовується нечасто. З погляду використання пам’яті немає сенсу постійно тримати такий вміст у пам’яті — краще завантажувати й вивантажувати його за потреби. Звісно, це компроміс між негайною доступністю вмісту ціною використання пам’яті під час виконання та завантаженням вмісту ціною витрат часу на завантаження.

У Defold є кілька способів динамічного завантаження вмісту:

* [Проксі колекції (collection proxy)](/uk/manuals/collection-proxy/)
* [Динамічні фабрики колекцій (collection factory)](/uk/manuals/collection-factory/#dynamic-loading-of-factory-resources)
* [Динамічні фабрики (factory)](/uk/manuals/factory/#dynamic-loading-of-factory-resources)
* [Live Update](/uk/manuals/live-update/)

## Оптимізація лічильників компонентів {#optimize-component-counters}
Defold одноразово виділяє пам’ять для компонентів (component) і ресурсів під час створення колекції (collection), щоб зменшити фрагментацію пам’яті. Обсяг виділеної пам’яті залежить від налаштувань різних лічильників компонентів у *game.project*. Скористайтеся [профайлером](/uk/manuals/profiling/), щоб отримати точні дані про використання компонентів і ресурсів, та налаштуйте гру так, щоб максимальні значення були ближчими до фактичної кількості компонентів і ресурсів. Це зменшить обсяг пам’яті, який використовує ваша гра (див. інформацію про [оптимізацію максимальної кількості компонентів](/uk/manuals/project-settings/#component-max-count-optimizations)).

## Оптимізація кількості вузлів GUI {#optimize-gui-node-count}
Оптимізуйте кількість вузлів GUI, установивши у файлі GUI максимальну кількість вузлів відповідно до потреб. Поле `Current Nodes` у [властивостях компонента GUI](https://defold.com/uk/manuals/gui/#gui-properties) показує кількість вузлів, які використовує компонент GUI.

{% include shared/uk/optimization-memory-html5.md %}