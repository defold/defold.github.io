---
brief: Данное руководство объясняет как можно подключаться к удаленным серверам и выполнять другие виды сетевых соединений.
github: https://github.com/defold/doc
language: ru
layout: manual
title: Работа с сетью
toc:
- Работа с сетью
- Технические подробности
- IPv4 и IPv6
- Безопасные соединения
---

# Работа с сетью

Для игр сейчас вполне не редкость иметь некое сетевое взаимодействие с бэкенд сервисами, для возможной отправки очков, управления матч-мейкингом или сохранения игры в облаке. Многие игры также имеют соединения в одноранговых сетях где игровые клиенты общаются напрямую друг с другом, без привлечения центрального сервера. Сетевые соединения и обмен данными может быть сделан с использованием нескольких разных протоколов и стандартов. Узнайте больше о различных способах использования сетевых соединений в Defold:

* [HTTP Запросы](/ru/manuals/http-requests)
* [Сокеты](/ru/manuals/socket-connections)
* [Соединения по веб-сокету](/manuals/websocket-connections)
* [Онлайн сервисы](/ru/manuals/online-services)

## Технические подробности

### IPv4 и IPv6

Defold поддерживает подключения по IPv4 и IPv6 как для сокетов, так и для HTTP-запросов.

### Безопасные соединения

Defold поддерживает защищённые SSL-соединения для сокетов и HTTP-запросов.

Defold может дополнительно проверять SSL-сертификат любого защищённого соединения. Проверка SSL будет включена, если в поле [SSL Certificates setting](/ru/manuals/project-settings/#network) раздела Network в *game.project* указан PEM-файл, содержащий открытые корневые сертификаты CA или открытый ключ самоподписанного сертификата. В `builtins/ca-certificates` включён список корневых сертификатов CA, однако рекомендуется создать новый PEM-файл и скопировать в него нужные корневые сертификаты CA в зависимости от серверов, к которым подключается игра.