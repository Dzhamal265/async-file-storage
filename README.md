Асинхронное распределенное файловое хранилище
============================================

Нужно написать демона с использованием `aiohttp`, который раздает файлы по HTTP из заранее назначенной директории
(без вложенностей), а за отсутствующими файлами пробует обратиться к другим таким же демонам.

Общая схема
-----------

Запускается несколько копий демона, каждый со своим конфигом. Например `A`, `B`, `C`.
`A` раздает файлы из `/tmp/a`, `B` – из `/tmp/b/`, `С` — из `/tmp/c/`.
Когда пользователь запрашивает файл `x` с ноды `A`, она ищет `/tmp/a/x`.
Если такой файл есть, его содержимое отдается пользователю.
Если такого файла нет, `A` делает запрос на `B` и `C`.
Если такого файла нет и там, пользователю возвращается код ошибки 404.
Если такой файл есть, то `A` получает его, отдает пользователю и сохраняет в `/tmp/a`
(последнее зависит от конфигурации).

Запросы
-------

Чтобы получить файл `x`, пользователь делает GET-запрос на `http://hostname:port/x`.

Демоны между собой тоже общаются по HTTP, запрос можно использовать любой.

Конфигурация
------------

При запуске демону указывается путь до yaml-файла с конфигурацией, в которой указано:

* Какой порт слушать;
* Из какой директории раздавать файлы;
* Где искать другие ноды (хост, порт);
* Нужно ли сохранять файл, найденный на другой ноде, локально.

