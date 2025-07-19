# 📚 Library API

A simple Django REST API for managing a book library, including endpoints for creating, reading, updating, and deleting book records using Django Rest Framework.

## 🚀 Features

- Add, update, delete, and view books
- REST API with JSON responses
- Django admin integration
- Built using ModelViewSet and Router
- SQLite for development

## 📸 Screenshot

![Book List API View](screenshots/
booklist.png)

## 📂 Project Structure

```bash
library_api/
├── books/                # Django app
├── library_api/          # Project settings
├── db.sqlite3            # SQLite database
├── manage.py
└── mod/                  # Virtual environment (excluded from Git)
```

## 🛠️ Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/impanaj07/library-api.git
cd library-api
```

2. Create and activate a virtual environment:
```bash
python -m venv mod
mod\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations and start server:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

5. Visit API:
- `http://127.0.0.1:8000/books/` – Book API
- `http://127.0.0.1:8000/admin/` – Admin Panel

## 📦 API Endpoints

| Method | Endpoint        | Description       |
|--------|-----------------|-------------------|
| GET    | /books/         | List all books    |
| POST   | /books/         | Create a book     |
| GET    | /books/{id}/    | Retrieve a book   |
| PUT    | /books/{id}/    | Update a book     |
| DELETE | /books/{id}/    | Delete a book     |

## 🧪 Technologies Used

- Python 3
- Django
- Django REST Framework
- SQLite
- Git & GitHub

## 🔐 License

This project is open source under the MIT License.
