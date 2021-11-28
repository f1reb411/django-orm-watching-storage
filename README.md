# Пульт охраны банка
***
Это внутренний репозиторий для сотрудников банка «Сияние». Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.

Пульт охраны — это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.

## Как установить

Запросите доступ к базе данных у службы безопасности.
Вам понадобятся хост, порт, имя базы данных, имя пользователя базы данных и пароль. В корне проекта необходимо создать
.env файл со следующим содержанием:

```
DB_HOST=<ваши данные>
DB_PORT=<ваши данные>
DB_NAME=<ваши данные>
DB_USER=<ваши данные>
DB_PASSWORD=<ваши данные>
SITE_DEBUG_MODE=True
```

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).
