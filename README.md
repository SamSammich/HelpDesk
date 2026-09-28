# HelpDesk

A web-based IT HelpDesk system for managing technical support requests.

Employees can create support tickets, while administrators can manage employees, categories, tickets, priorities and statuses through Django Admin.

## Features

* Employee management
* Category management
* Ticket management
* Ticket priorities
* Ticket statuses
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

## Main Requirements Covered

| Requirement      | Status   |
| ---------------- | -------- |
| Employee model   | Complete |
| Category model   | Complete |
| Ticket model     | Complete |
| Django Admin     | Complete |
| REST CRUD        | Complete |
| Ticket filtering | Complete |
| Ticket search    | Complete |
| Dashboard        | Complete |
| Ticket list      | Complete |
| Ticket detail    | Complete |
| Ticket creation  | Complete |
| PostgreSQL       | Complete |
| Docker           | Complete |
| Documentation    | Complete |

## Author

HelpDesk project developed as a backend/web development assessment project.
