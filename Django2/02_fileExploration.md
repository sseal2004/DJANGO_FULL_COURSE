# 🍵 Chai and Django — File Exploration Guide

A breakdown of every important file and folder in a Django project — what it does and why it matters.

---

## 📁 Project Structure Overview

```
ChaiAurCode/
├── manage.py               ← Entry point — run all Django commands from here
├── db.sqlite3              ← Default database file (auto-created after migrations)
├── ChaiAurCode/            ← Project-level config folder (same name as project)
│   ├── __init__.py         ← Marks this folder as a Python package
│   ├── settings.py         ← ⭐ Most important file — all project configuration lives here
│   ├── urls.py             ← Root routing file — maps URLs to views
│   ├── asgi.py             ← Entry point for async servers (e.g., Daphne)
│   └── wsgi.py             ← Entry point for production servers (e.g., Gunicorn)
└── __pycache__/            ← Auto-generated cache folder — speeds up code execution
```

---

## 📄 File-by-File Breakdown

---

### `manage.py` — The Starting Point

The **entry-level** command-line utility for your project. You interact with Django almost entirely through this file.

```bash
python manage.py runserver      # Start the dev server
python manage.py migrate        # Apply database migrations
python manage.py createsuperuser  # Create an admin user
python manage.py startapp myapp   # Create a new Django app
```

> ⚠️ Never delete or edit `manage.py`. It is auto-generated and should remain untouched.

---

### `db.sqlite3` — The Default Database

Django uses **SQLite** as the default database. This file is auto-created the first time you run:

```bash
python manage.py migrate
```

| Feature | Detail |
|---------|--------|
| Type | File-based relational database |
| Location | Root of the project |
| Good for | Development and small projects |
| Production use | Switch to PostgreSQL or MySQL |

---

### `__pycache__/` — The Cache Folder

Python automatically creates this folder to store **compiled bytecode** (`.pyc` files).

- It **speeds up** your application by avoiding re-compilation on every run
- You can safely **delete** it — Python will recreate it automatically
- It should be added to `.gitignore` so it's not committed to version control

```gitignore
# .gitignore
__pycache__/
*.pyc
```

---

### ⭐ `settings.py` — The Most Important File

This is the **central configuration file** for your entire Django project. Everything from installed apps to database settings lives here.

---

#### `INSTALLED_APPS` — Registered Applications

```python
INSTALLED_APPS = [
    'django.contrib.admin',        # Admin dashboard at /admin/
    'django.contrib.auth',         # User authentication system
    'django.contrib.contenttypes', # Framework for content types
    'django.contrib.sessions',     # Session management
    'django.contrib.messages',     # Flash messaging system
    'django.contrib.staticfiles',  # Serves CSS, JS, and images
]
```

> Each entry is a **separate Django app** — this allows multiple developers to work on isolated features independently. When you create your own app (e.g., `startapp blog`), you register it here too.

---

#### `MIDDLEWARE` — Request/Response Pipeline

Middleware sits **between the browser and your views** — every request passes through this list top to bottom, and every response passes back through it bottom to top.

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',         # HTTPS, HSTS headers
    'django.contrib.sessions.middleware.SessionMiddleware',  # Enables session support
    'django.middleware.common.CommonMiddleware',             # URL normalization
    'django.middleware.csrf.CsrfViewMiddleware',             # CSRF attack protection
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Attaches user to request
    'django.contrib.messages.middleware.MessageMiddleware',  # Flash message support
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Clickjacking protection
]
```

> Think of middleware as a **security checkpoint** — requests are inspected, validated, and enriched before reaching your view.

---

#### `TEMPLATES` — HTML Template Configuration

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],          # ← Add ['templates'] here to use a root templates/ folder
        'APP_DIRS': True,    # Looks for templates inside each app's templates/ subfolder
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request', # Adds request to templates
                'django.contrib.auth.context_processors.auth', # Adds user & perms
                'django.contrib.messages.context_processors.messages', # Adds messages
            ],
        },
    },
]
```

> To use a global `templates/` folder at the project root, change `'DIRS': []` to `'DIRS': ['templates']`.

---

#### `DATABASES` — Database Configuration

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Database type
        'NAME': BASE_DIR / 'db.sqlite3',         # Path to the database file
    }
}
```

To switch to **PostgreSQL** in production:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

#### `AUTH_PASSWORD_VALIDATORS` — Password Rules

```python
AUTH_PASSWORD_VALIDATORS = [
    {
        # Password must not be too similar to the username or email
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        # Password must be at least 8 characters (default)
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        # Password must not be a commonly used password (e.g., "password123")
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        # Password must not be entirely numeric (e.g., "12345678")
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
```

> These validators run automatically when a user sets or changes their password.

---

### `urls.py` — The Routing File

This is the **root URL configuration** — it maps incoming URL paths to the correct view functions.

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel — built-in but needs setup
]
```

> The `/admin/` route is **pre-registered** by Django but the admin panel won't work until you run migrations and create a superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

Then visit `http://127.0.0.1:8000/admin/` and log in.

---

## ✅ Quick Reference

| File / Folder | Role | Edit? |
|---------------|------|-------|
| `manage.py` | CLI entry point | ❌ Never |
| `db.sqlite3` | Default database | ❌ Auto-managed |
| `__pycache__/` | Bytecode cache | ❌ Auto-generated |
| `settings.py` | Project configuration | ✅ Frequently |
| `urls.py` | URL routing | ✅ Frequently |
| `wsgi.py` / `asgi.py` | Server entry points | ⚠️ Only for deployment |

---

## 🔑 Key Concepts Summary

| Concept | What It Does |
|---------|-------------|
| `INSTALLED_APPS` | Registers apps so Django knows about them |
| `MIDDLEWARE` | Processes every request/response globally |
| `TEMPLATES` | Configures where Django looks for HTML files |
| `DATABASES` | Sets the database engine and connection |
| `AUTH_PASSWORD_VALIDATORS` | Enforces password strength rules |
| `urlpatterns` | Maps URL paths to view functions |
