# Furniture Store API (Test Task)

REST API для мебельного магазина: каталог мебели и создание заказов.

## Tech stack
- Python, Django, Django REST Framework
- PostgreSQL
- Docker, docker-compose

## Features
- Просмотр каталога мебели
- Получение товара по ID
- Создание заказа (email + список товаров)
- Получение списка заказов по email

## Requirements
- Docker Desktop

## Setup & Run (Docker)
1) Создайте файл `.env` в корне проекта (или используйте свой):
```env
DEBUG=1
SECRET_KEY=super-secret-key

POSTGRES_DB=furniture_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

ALLOWED_HOSTS=127.0.0.1,localhost
```

2) Запуск проекта:

```bash
docker-compose up --build
```

3) Применить миграции (в отдельном терминале):

```bash
docker-compose exec web python manage.py migrate
```

4) Создать суперпользователя:

```bash
docker-compose exec web python manage.py createsuperuser
```

После запуска:
- Admin: http://127.0.0.1:8000/admin/
- API root: http://127.0.0.1:8000/api/

## API Endpoints

### Furniture
- `GET /api/furniture/` — список мебели
- `GET /api/furniture/<id>/` — товар по ID

### Orders
- `POST /api/orders/` — создать заказ  
  Body (JSON):

```json
{
  "email": "client_1@gmail.com",
  "items": [1, 2]
}
```

- `GET /api/orders/list/?email=client_1@gmail.com` — список заказов по email

## Notes
- Сумма заказа (`total_price`) рассчитывается на backend (Python).
- Аутентификация не требуется по условиям тестового задания.