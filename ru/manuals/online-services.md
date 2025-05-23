---
brief: Данное руководство объясняет как подключаться к различным игровым и бэкенд-сервисам.
github: https://github.com/defold/doc
language: ru
layout: manual
title: Игровые онлайн сервисы
toc:
- Игровые онлайн сервисы
- Общего назначения
- Аутентификация, таблицы рекордов, достижения
- Аналитика
---

# Игровые онлайн сервисы

Использование HTTP запросов и сокет-соединений позволяет вам подключаться и взаимодействовать с тысячами различных сервисов в интернете, но в большинстве случаев, это нечто большее чем просто отправка HTTP запроса. Обычно вам нужна некая аутентификация, данные запроса возможно должны быть отформатированы в специальном виде и ответ также возможно нужно будет распарсить до того, как им можно будет воспользоваться. Конечно, все это может быть проделано вручную, но существуют также расширения и библиотеки, чтобы позаботиться о подобных вещах за вас. Ниже можно найти список некоторых расширений, которые можно применить для более легкого взаимодействия со специфическими бэкенд-сервисами:

## Общего назначения
* [Colyseus](https://defold.com/assets/colyseus/) --- Игровой клиент для мультиплеера
* [Nakama](https://defold.com/assets/nakama/) --- Добавьте аутентификацию, матч-мейкинг, аналитику, облачные сохранения, мультиплеер, чат и многое другое своей игре
* [PlayFab](https://defold.com/assets/playfabsdk/) --- Добавьте аутентификацию, матч-мейкинг, аналитику, облачные сохранения, мультиплеер, чат и многое другое своей игре
* [AWS SDK](https://github.com/britzl/aws-sdk-lua) --- Используйте Amazon Web Services прямо в своей игре

## Аутентификация, таблицы рекордов, достижения
* [Google Play Game Services](https://defold.com/assets/googleplaygameservices/) --- Используйте Игровые Сервисы Google Play для аутентификации и облачных сохранений в своей игре 
* [Steamworks](https://defold.com/assets/steamworks/) --- Добавьте поддержку Steam в своей игре
* [Apple GameKit Game Center](https://defold.com/assets/gamekit/)

## Аналитика
* [Firebase Analytics](https://defold.com/assets/googleanalyticsforfirebase/) --- Добавьте аналитику от Firebase своей игре
* [Game Analytics](https://gameanalytics.com/docs/item/defold-sdk) --- Добавьте аналитику GameAnalytics своей игре
* [Google Analytics](https://defold.com/assets/gameanalytics/) --- Добавьте Google Analytics в свою игру

Посетите [Портал Ассетов](https://www.defold.com/assets/) за еще большим количеством расширений!