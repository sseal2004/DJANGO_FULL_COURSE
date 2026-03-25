# 🍵 Chai and Django — Installation Guide

A step-by-step guide to installing Django using `uv` on Windows (PowerShell).

---

## 📋 Prerequisites

- Windows with PowerShell
- Internet connection

---

## Step 1 — Install `uv` Package Manager

Run the following command in **PowerShell** to install `uv`:

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

> `uv` is a fast Python package and project manager — a modern alternative to `pip` and `venv`.

---

## Step 2 — Set the PATH

Add `uv` to your current session's PATH so it can be used immediately:

```powershell
$env:Path = "C:\Users\ADMIN\.local\bin;$env:Path"
```

> ⚠️ This sets the PATH only for the **current session**. To make it permanent, add it to your System Environment Variables.

---

## Step 3 — Create a Virtual Environment

```powershell
uv venv
```

This creates a `.venv` folder in your current directory.

```
your-project/
└── .venv/        ← virtual environment created here
```

---

## Step 4 — Activate the Virtual Environment

Navigate into the `.venv` folder and run the activation script:

```powershell
.venv\Scripts\activate
```

Once activated, your terminal prompt will show the environment name:

```
(.venv) PS D:\Django2>
```

---

## Step 5 — Install Django

With the virtual environment active, install Django using `uv`:

```powershell
uv pip install Django
```

---

## Step 6 — Create a New Django Project

Use `django-admin` to scaffold a new project:

```powershell
django-admin startproject ChaiAurCode
```

This generates the following structure:

```
Django2/
├── ChaiAurCode/          ← project root
│   ├── ChaiAurCode/      ← inner config folder
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── manage.py         ← project management CLI
```

Navigate into the project folder:

```powershell
cd ChaiAurCode
```

---

## Step 7 — Run the Development Server

Start the server on the **default port (8000)**:

```powershell
python manage.py runserver
```

Output:

```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Or run on a **custom port**:

```powershell
python manage.py runserver 8001
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

You should see the Django welcome page. 🎉

---

## ✅ Quick Reference

| Step | Command | Purpose |
|------|---------|---------|
| 1 | `irm https://astral.sh/uv/install.ps1 \| iex` | Install `uv` |
| 2 | `$env:Path = "C:\Users\ADMIN\.local\bin;$env:Path"` | Set PATH |
| 3 | `uv venv` | Create virtual environment |
| 4 | `.venv\Scripts\activate` | Activate virtual environment |
| 5 | `uv pip install Django` | Install Django |
| 6 | `django-admin startproject ChaiAurCode` | Create new project |
| 7 | `python manage.py runserver` | Start dev server |

---

## ⚠️ Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `uv` not recognized | PATH not set | Run Step 2 again or restart terminal |
| `.venv\Scripts\activate` fails | Execution policy restricted | Run `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| `django-admin` not found | Virtual env not activated | Run `.venv\Scripts\activate` first |
| Port already in use | Another process on port 8000 | Use `python manage.py runserver 8001` |
