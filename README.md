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
