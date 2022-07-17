# api_final
api final
### Описание

Финальный проект спринта "API"
Предоставляет доступ к к API проекта Yatube

Выполнил [Алексей Осипов](https://github.com/AlexeiOsipov)

### Установка:

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone git@github.com:AlexeiOsipov/api_final_yatube.git
```

```bash
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```bash
python3 -m venv env
```

```bash
source env/bin/activate
```

```bash
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

Выполнить миграции:

```bash
python3 manage.py migrate
```

Запустить проект:

```bash
python3 manage.py runserver
```
### Примеры

Новый запрос:
GET-запрос http://127.0.0.1:8000/api/v1

Ответ:
```json
{
    "posts": "http://127.0.0.1:8000/api/v1/posts/",
    "groups": "http://127.0.0.1:8000/api/v1/groups/",
    "follow": "http://127.0.0.1:8000/api/v1/follow/"
}
```

Получение токена:
POST-запрос http://127.0.0.1:8000/api/v1/jwt/create/

```json
{
    "username": "string",
    "password": "string"
}
```
Получение списка постов:
GET-запрос http://127.0.0.1:8000/api/v1/posts/

Ответ:
```json
{
  "count": 123,
  "next": "http://127.0.0.1:8000/api/v1/posts/?offset=400&limit=100",
  "previous": "http://127.0.0.1:8000/api/v1/posts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

Добавление комментария к посту
POST-запрос http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

```json
{
    "text": "string"
}
```

Получение информации о группе:
GET-запрос http://127.0.0.1:8000/api/v1/groups/{id}/

Ответ:
```json
{
  "id": 0,
  "title": "string",
  "slug": "string",
  "description": "string"
}
```

Оформление подписки на автора:
GET-запрос http://127.0.0.1:8000/api/v1/follow/

Ответ:
```json
{
  "user": "string",
  "following": "string"
}
