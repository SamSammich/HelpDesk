# HelpDesk — система управления IT-заявками

Веб-приложение для внутренней IT-службы, предназначенное для регистрации, просмотра и управления заявками сотрудников.

## Возможности

* Управление сотрудниками
* Управление категориями заявок
* Создание и управление IT-заявками
* Отслеживание статуса и приоритета заявок
* Фильтрация заявок
* Поиск по названию и описанию
* Авторизация пользователей
* Разделение прав сотрудников и администраторов
* Сотрудник видит только свои заявки
* Сотрудник не может создать заявку от имени другого сотрудника
* Администратор видит и управляет всеми заявками
* Django Admin
* REST API
* Веб-интерфейс на Django Templates
* PostgreSQL
* Docker и Docker Compose

## Технологии

* Python 3.12
* Django 6.1
* Django REST Framework
* django-filter
* PostgreSQL 16
* Docker
* Docker Compose
* Django Templates
* Poetry

## Структура проекта

```text
HelpDesk/
├── categories/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── employees/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── tickets/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── web/
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   └── tickets/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .gitignore
├── manage.py
├── pyproject.toml
└── poetry.lock
```

## Модели

### Сотрудник

Содержит:

* ID
* ФИО
* Email
* Отдел
* Связь с пользователем Django
* Дата создания

### Категория

Содержит:

* ID
* Название
* Описание
* Активность
* Дата создания

### Заявка

Содержит:

* ID
* Сотрудник
* Категория
* Название
* Описание
* Статус
* Приоритет
* Дата создания
* Дата обновления

### Статусы заявки

* `NEW` — новая
* `IN_PROGRESS` — в работе
* `RESOLVED` — решена
* `CLOSED` — закрыта

### Приоритеты

* `LOW` — низкий
* `MEDIUM` — средний
* `HIGH` — высокий
* `CRITICAL` — критический

## Авторизация и права доступа

Страница входа:

```text
/login/
```

После авторизации сотрудник может:

* создавать заявки
* просматривать только свои заявки
* просматривать детали своих заявок

Администратор может:

* просматривать все заявки
* изменять статус и приоритет заявок
* управлять сотрудниками и категориями через Django Admin
* управлять заявками через Django Admin

## REST API

### Сотрудники

```text
GET    /api/employees/
POST   /api/employees/
GET    /api/employees/<id>/
PUT    /api/employees/<id>/
PATCH  /api/employees/<id>/
DELETE /api/employees/<id>/
```

### Категории

```text
GET    /api/categories/
POST   /api/categories/
GET    /api/categories/<id>/
PUT    /api/categories/<id>/
PATCH  /api/categories/<id>/
DELETE /api/categories/<id>/
```

### Заявки

```text
GET    /api/tickets/
POST   /api/tickets/
GET    /api/tickets/<id>/
PUT    /api/tickets/<id>/
PATCH  /api/tickets/<id>/
DELETE /api/tickets/<id>/
```

### Доступ к заявкам

API заявок требует авторизации.

Сотрудник получает доступ только к своим заявкам.

Администратор получает доступ ко всем заявкам.

При создании заявки через API сотрудник определяется автоматически по авторизованному пользователю.

## Фильтрация заявок

Фильтрация доступна по:

* статусу
* приоритету
* категории
* сотруднику

Примеры:

```text
/api/tickets/?status=NEW
/api/tickets/?priority=HIGH
/api/tickets/?category=2
/api/tickets/?employee=5
```

## Поиск

Поиск выполняется по названию и описанию заявки:

```text
/api/tickets/?search=printer
```

## Веб-интерфейс

Основные страницы:

```text
/login/                 — авторизация
/                       — Dashboard
/tickets/               — список заявок
/tickets/<id>/          — информация о заявке
/tickets/create/        — создание заявки
/admin/                 — административная панель
```

Dashboard отображает:

* общее количество заявок
* количество новых заявок
* количество решённых заявок
* последние заявки

## Django Admin

В административной панели зарегистрированы:

* Employees
* Categories
* Tickets

Для заявок доступны:

* отображение основных полей
* изменение статуса и приоритета
* фильтрация по статусу
* фильтрация по приоритету
* фильтрация по категории
* поиск по названию заявки
* поиск по имени сотрудника

## Запуск через Docker

Для запуска проекта необходимы:

* Docker
* Docker Compose

Клонировать репозиторий:

```bash
git clone https://github.com/SamSammich/HelpDesk.git
cd HelpDesk
```

Запустить проект:

```bash
docker compose up --build
```

После запуска приложение доступно по адресу:

```text
http://127.0.0.1:8000/
```

Django Admin:

```text
http://127.0.0.1:8000/admin/
```

## Создание администратора

Для создания суперпользователя:

```bash
docker compose exec web python manage.py createsuperuser
```

После этого можно войти в административную панель:

```text
http://127.0.0.1:8000/admin/
```

## Переменные окружения

Для настройки подключения к базе данных используется файл `.env`.

Пример конфигурации находится в:

```text
.env.example
```

Файл `.env` не добавляется в Git и должен использоваться для локальных секретных настроек.

## Полезные Docker-команды

Запуск:

```bash
docker compose up
```

Запуск с пересборкой:

```bash
docker compose up --build
```

Запуск в фоновом режиме:

```bash
docker compose up -d
```

Остановка:

```bash
docker compose down
```

Просмотр контейнеров:

```bash
docker compose ps
```

Просмотр логов:

```bash
docker compose logs
```

Открыть shell Django-контейнера:

```bash
docker compose exec web sh
```

## База данных

Проект использует PostgreSQL 16.

PostgreSQL запускается автоматически через Docker Compose и сохраняет данные в Docker volume.

При запуске приложения Django автоматически выполняет миграции:

```bash
python manage.py migrate
```

## Архитектура

Проект разделён на отдельные Django-приложения:

* `employees` — работа с сотрудниками и связь с пользователями Django
* `categories` — работа с категориями
* `tickets` — работа с заявками и их API
* `web` — веб-интерфейс и авторизация
* `config` — настройки и конфигурация проекта

REST API реализован с использованием Django REST Framework и ViewSet/Router.

Веб-интерфейс реализован с использованием стандартных Django Templates.

Права доступа к заявкам зависят от роли пользователя:

* сотрудники работают только со своими заявками
* администраторы имеют доступ ко всем заявкам

## Проверка проекта

Проект был проверен после настройки Docker и PostgreSQL:

* приложение запускается через Docker Compose
* PostgreSQL подключается корректно
* миграции выполняются автоматически
* REST API доступен
* Django Admin доступен
* веб-интерфейс работает
* авторизация пользователей работает
* сотрудник видит только свои заявки
* сотрудник может создавать заявки
* администратор имеет доступ ко всем заявкам
* администратор может изменять статус и приоритет заявок
* права доступа к заявкам проверяются
* создание заявок работает

## Автор

**Abdusamatov Somon**

GitHub:
https://github.com/SamSammich

# HelpDesk

A web-based IT HelpDesk system for managing technical support requests.

Employees can create support tickets, while administrators can manage employees, categories, tickets, priorities and statuses through Django Admin.

## Features

* Employee management
* Category management
* Ticket management
* Ticket priorities
* Ticket statuses
* User authentication
* Role-based access for employees and administrators
* Employees can view only their own tickets
* Employees cannot create tickets on behalf of other employees
* Administrators can view and manage all tickets
* REST API
* Ticket filtering
* Ticket search
* Django Admin interface
* Web dashboard
* Ticket list
* Ticket detail page
* Ticket creation form
* PostgreSQL database
* Docker / Docker Compose support

## Tech Stack

* Python 3.12
* Django 6.1
* Django REST Framework
* django-filter
* PostgreSQL
* Poetry
* Docker
* Docker Compose
* Django Templates

## Project Structure

```text
HelpDesk/
│
├── categories/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── employees/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── tickets/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── web/
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   └── tickets/
│       ├── ticket_list.html
│       ├── ticket_detail.html
│       └── ticket_create.html
│
├── config/
│   ├── settings.py
│   └── urls.py
│
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env.example
├── manage.py
├── pyproject.toml
└── README.md
```

## Authentication and Access Control

Login page:

```text
/login/
```

Employees can:

* create support tickets
* view only their own tickets
* view details of their own tickets

Administrators can:

* view all tickets
* change ticket status and priority
* manage employees and categories through Django Admin
* manage all tickets through Django Admin

## Running with Docker

Make sure Docker Desktop is installed and running.

Build and start the application:

```bash
docker compose up --build
```

The application will be available at:

```text
http://127.0.0.1:8000/
```

Django migrations are applied automatically when the container starts.

## Django Admin

Open:

```text
http://127.0.0.1:8000/admin/
```

Create an administrator with:

```bash
docker compose exec web python manage.py createsuperuser
```

Then use the created credentials to access Django Admin.

## REST API

### Employees

```text
GET    /api/employees/
POST   /api/employees/
GET    /api/employees/<id>/
PUT    /api/employees/<id>/
PATCH  /api/employees/<id>/
DELETE /api/employees/<id>/
```

### Categories

```text
GET    /api/categories/
POST   /api/categories/
GET    /api/categories/<id>/
PUT    /api/categories/<id>/
PATCH  /api/categories/<id>/
DELETE /api/categories/<id>/
```

### Tickets

```text
GET    /api/tickets/
POST   /api/tickets/
GET    /api/tickets/<id>/
PUT    /api/tickets/<id>/
PATCH  /api/tickets/<id>/
DELETE /api/tickets/<id>/
```

### Ticket API Access

Ticket API endpoints require authentication.

Employees can access only their own tickets.

Administrators can access all tickets.

When an employee creates a ticket through the API, the employee is assigned automatically from the authenticated user.

## Ticket Filtering

Filter by status:

```text
/api/tickets/?status=NEW
```

Filter by priority:

```text
/api/tickets/?priority=HIGH
```

Filter by category:

```text
/api/tickets/?category=2
```

Filter by employee:

```text
/api/tickets/?employee=1
```

## Ticket Search

Search by title or description:

```text
/api/tickets/?search=printer
```

## Web Interface

Dashboard:

```text
/
```

Login:

```text
/login/
```

Tickets:

```text
/tickets/
```

Ticket details:

```text
/tickets/<id>/
```

Create ticket:

```text
/tickets/create/
```

Admin:

```text
/admin/
```

## Ticket Statuses

* `NEW`
* `IN_PROGRESS`
* `RESOLVED`
* `CLOSED`

## Ticket Priorities

* `LOW`
* `MEDIUM`
* `HIGH`
* `CRITICAL`

## Local Development

Install dependencies:

```bash
poetry install
```

Run migrations:

```bash
poetry run python manage.py migrate
```

Run the development server:

```bash
poetry run python manage.py runserver
```

## Useful Docker Commands

Start:

```bash
docker compose up
```

Build and start:

```bash
docker compose up --build
```

Run in background:

```bash
docker compose up -d
```

Stop:

```bash
docker compose down
```

View logs:

```bash
docker compose logs -f
```

Open Django shell:

```bash
docker compose exec web python manage.py shell
```

Run migrations:

```bash
docker compose exec web python manage.py migrate
```

Create superuser:

```bash
docker compose exec web python manage.py createsuperuser
```

## Database

The Docker configuration uses PostgreSQL 16.

PostgreSQL data is stored in a Docker named volume:

```text
postgres_data
```

This allows the database data to persist when containers are restarted.

## Architecture

The project follows a Django application structure with separate applications for:

* Employees
* Categories
* Tickets
* Web interface

The REST API is implemented using Django REST Framework and ViewSets.

Filtering and searching are implemented using `django-filter` and DRF `SearchFilter`.

The web interface uses Django Templates.

Django Admin provides administrative management of all core entities.

Access control ensures that employees can work only with their own tickets, while administrators can access all tickets.

## Main Requirements Covered

| Requirement               | Status   |
| ------------------------- | -------- |
| Employee model            | Complete |
| Category model            | Complete |
| Ticket model              | Complete |
| User authentication       | Complete |
| Ticket access control     | Complete |
| Employee ticket ownership | Complete |
| Django Admin              | Complete |
| REST CRUD                 | Complete |
| Ticket filtering          | Complete |
| Ticket search             | Complete |
| Dashboard                 | Complete |
| Ticket list               | Complete |
| Ticket detail             | Complete |
| Ticket creation           | Complete |
| PostgreSQL                | Complete |
| Docker                    | Complete |
| Documentation             | Complete |

## Author

HelpDesk project developed as a backend/web development assessment project.
