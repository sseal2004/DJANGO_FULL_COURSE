# Django + React Full Stack Project

A full-stack web application built with **Django REST Framework** (backend) and **React** (frontend), using JWT authentication and SQLite/MySQL database support.

---

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Project Setup](#project-setup)
- [Backend Configuration](#backend-configuration)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [Deployment on Choreo](#deployment-on-choreo)

---

## Prerequisites

- Python 3.8+
- Node.js & npm
- pip

---

## Project Setup

### 1. Create Virtual Environment

```bash
python -m venv .venv
```

Activate it:

- **Windows:** `.venv\Scripts\activate`
- **Mac/Linux:** `source .venv/bin/activate`

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create Django Project

```bash
django-admin startproject backend
cd backend
```

### 4. Create API App

```bash
python manage.py startapp api
```

---

## Backend Configuration

### 5. Update `backend/settings.py`

Add the following imports at the top:

```python
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()
```

### 6. Allow All Hosts (Development)

```python
ALLOWED_HOSTS = ["*"]
```

### 7. Add Installed Apps

```python
INSTALLED_APPS = [
    # Default apps...
    "api",
    "rest_framework",
    "corsheaders",
]
```

### 8. Configure REST Framework & JWT

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}
```

### 9. Add CORS Middleware

In the `MIDDLEWARE` list, add this **at the top**:

```python
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    # ... other middleware
]
```

### 10. Configure CORS

```python
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWS_CREDENTIALS = True
```

---

## Models

### 11. Create the Note Model (`api/models.py`)

```python
from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title
```

### 12. Create Serializers (`api/serializers.py`)

```python
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}
```

---

## URL Configuration

### 13. Update `backend/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]
```

### 14. Create `api/urls.py`

```python
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path("user/register/", views.CreateUserView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="get_token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
]
```

---

## Database Setup

### Option A — SQLite (Default, Recommended for Development)

No setup needed. Django uses SQLite automatically via `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

To view the database, install [DB Browser for SQLite](https://sqlitebrowser.org/).

### Option B — MySQL (Production)

**Step 1:** [Download and install MySQL](https://dev.mysql.com/downloads/)

**Step 2:** Create the database:

```sql
CREATE DATABASE myproject;
```

**Step 3:** Install the connector:

```bash
pip install mysqlclient
```

**Step 4:** Update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
```

**Step 5:** Add a `.env` file in your project root:

```env
DB_NAME=myproject
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=3306
```

---

## Running the Application

### 15. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

This creates the following tables:

| Table | Purpose |
|---|---|
| `auth_user` | User accounts |
| `auth_group` | User groups |
| `auth_permission` | Permissions |
| `django_admin_log` | Admin panel logs |
| `django_content_type` | Dynamic model tracking |
| `django_session` | User login sessions |
| `api_note` | Your Note model |

### 16. Start the Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

---

## Deployment on Choreo

Choreo is an app deployment platform — the database runs separately and connects via environment variables.

### Step 1: Set Environment Variables

In Choreo, go to **Settings → Configurations / Environment Variables** and add:

```
DB_NAME=myproject
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=your-db-host
DB_PORT=3306
```

### Step 2: Add a Database Connection (Optional)

Go to **Connections → Create Connection** to link an external database service (MySQL, PostgreSQL, etc.). Choreo will provide the connection details as environment variables.

### Step 3: Deploy

Push your code to the connected repository. Choreo will automatically build and deploy your Django app using the environment variables you configured.

> **Note:** Choreo is a hosting platform (similar to Vercel). It runs your app but does not host your database — use a managed DB service like PlanetScale, Railway, or AWS RDS.

---

## Project Structure

```
project-root/
├── backend/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── api/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── .env
├── requirements.txt
└── manage.py
```

---

## requirements.txt (Reference)

```
django
djangorestframework
djangorestframework-simplejwt
django-cors-headers
python-dotenv
mysqlclient       # only if using MySQL
```