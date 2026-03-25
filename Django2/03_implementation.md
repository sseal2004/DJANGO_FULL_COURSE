# 🍵 Chai and Django — Setup Guide

A step-by-step guide to setting up views, URLs, templates, and static files in Django.

---

## 📁 Project Structure

```
myproject/
├── manage.py
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── views.py
├── static/
│   └── style.css
└── templates/
    └── website/
        ├── index.html
        ├── about.html
        └── contact.html
```

---

## Step 1 — Create View Functions

Go to `views.py` and define your route handler functions.

### Basic version (using `HttpResponse`)

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World. You are at Chai and Django home page")

def about(request):
    return HttpResponse("Hello World. You are at Chai and Django about page")

def contact(request):
    return HttpResponse("Hello World. You are at Chai and Django contact page")
```

### Updated version (using HTML templates)

Once templates are set up (see Step 4), switch to `render()`:

```python
from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')
```

> `render()` loads an HTML file from the `templates/` folder instead of returning a plain string.

---

## Step 2 — Register URL Routes

Go to `urls.py` and map URL paths to your view functions.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('',         views.home,    name='home'),
    path('about/',   views.about,   name='about'),
    path('contact/', views.contact, name='contact'),
]
```

> The `name=` parameter is optional but useful for reverse URL lookups using `{% url 'home' %}` inside templates.

---

## Step 3 — Run Migrations & Start the Server

```bash
# Apply any pending database migrations
python manage.py migrate

# Start the development server at http://127.0.0.1:8000/
python manage.py runserver
```

---

## Step 4 — Create Templates & Static Folders

At the **root of your project**, create two folders:

| Folder | Purpose |
|--------|---------|
| `templates/` | Contains HTML files |
| `static/` | Contains CSS, JavaScript, and image files |

Inside `templates/`, create a subfolder for your app (e.g., `website/`) to avoid name collisions across multiple Django apps.

```
templates/
└── website/
    └── index.html

static/
└── style.css
```

---

## Step 5 — Register Templates & Static Paths in Settings

Go to `settings.py` and make the following two changes:

```python
import os

# ── Templates ────────────────────────────────────────────────────────────────
# Tell Django where to look for HTML template files
TEMPLATES = [
    {
        ...
        'DIRS': ['templates'],
        ...
    }
]

# ── Static Files (CSS, JS, Images) ───────────────────────────────────────────
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

> `BASE_DIR` is already defined at the top of `settings.py` — do not change it.

---

## Step 6 — Create an HTML Template

Create `templates/website/index.html`:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chai and Django</title>
    <link rel="stylesheet" href="{% static 'style.css' %}">
</head>
<body>
    <h1>Hello World — Chai and Django</h1>
</body>
</html>
```

> ⚠️ `{% load static %}` **must** appear at the very top of the file before any HTML tags.

---

## Step 7 — Create a CSS File

Create `static/style.css`:

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    color: #333;
    padding: 2rem;
}

h1 {
    color: #c0392b;
}
```

---

## ✅ Quick Reference

| File | What to Change |
|------|---------------|
| `views.py` | Add view functions using `render()` |
| `urls.py` | Map URL paths to view functions |
| `settings.py` | Set `DIRS: ['templates']` and `STATICFILES_DIRS` |
| `templates/website/index.html` | Add `{% load static %}` at top, link CSS |
| `static/style.css` | Write your styles |

---

## ⚠️ Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `TemplateDoesNotExist` | `DIRS` not set in `settings.py` | Add `'DIRS': ['templates']` to `TEMPLATES` |
| `/static/style.css` not found | `STATICFILES_DIRS` not set | Add `STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]` |
| `{% static %}` tag not working | Forgot `{% load static %}` | Add it to the very top of the HTML file |
