# Step: 1 Virtual Environment

python -m venv .venv

# Step: 2 Requirement.txt file

pip install -r requirements.txt

# Step: 3 To Start django Project

django-admin startproject backend

# Step: 4 To create api folder

python manage.py startapp api

# Step: 5 Include this in settings.py

import Path
from datetime import timedelta
from dotenv import load_dotenv
import os

load_dotenv()

# Step: 6 It will allow any localhost to host our django application update this at settings.py :

ALLOWED_HOSTS = ["*"]

# Step: 7 Including some configuration such as JWT tokens below this allowed host:

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

# Step: 7  inside installed apps add this

INSTALLED_APPS = [
    "api",
    "rest_framework",
    "corsheaders"

]
# Step: 8 add Middlewares inside Middlewares
    Middlewares=[
    "corsheaders.middleware.CorsMiddleware",
    ]

# Step: 9 Cors Allowed Origin at the bottom of settings.py
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWS_CREDENTIALS = True    

#Step: 7 to create JWT access token create a file in api/serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

# Step : 8 Remove this from url.py

"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Step : 9 Now setup all the urls here

# Step: 10 Create models.py to store database table

# Create your models here.
# You created a Django model called Note → it represents a database table.
# Imports
from django.db import models
from django.contrib.auth.models import User

# Model Declaration
class Note(models.Model): # Create a table named Note in the database
    #Fields (Columns in DB)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title
# Step : 11 It is creating and updating your database tables automatically based on Django models.
(.venv) D:\DJANGO_REACT_TUTORIAL\Backend>python manage.py migrate


What tables were created
🔹 auth (User system)

User table

Groups

Permissions


🔹 admin

Stores admin panel logs

🔹 contenttypes

Tracks models dynamically

🔹 sessions

Stores user login sessions

# Step:12 To run our application 
python manage.py runserver

# Step:13 By using that html form create a newUser 
![alt text](image.png)
# Step:14 User Created in the html form
![alt text](image-1.png)

# Step:15 Inside api folder create a file name urls.py to set the urls
# Run this command python manage.py makemigrations


# Step:16 Database Connectivity
Check this file:

backend/settings.py

You’ll see:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

👉 This means:
✔ Database already exists
✔ No setup needed

Step 2: Create tables (you already did partially)

Run:

python manage.py makemigrations
python manage.py migrate

👉 This creates tables like:

users

notes (your model)

Step 3: View database

Install:

pip install dbsqlite3

OR use GUI:
👉 DB Browser for SQLite

# Step:17 Database Connectivity
Step 1: Install MySQL

👉 Download from:

MySQL

✅ Step 2: Create database
CREATE DATABASE myproject;

# Step:18  Installation Command
Step 3: Install connector
pip install mysqlclient
✅ Step 4: Update Django settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
✅ Step 5: Migrate again
python manage.py migrate
❗ About your current screen

That WSO2 dashboard:

Shows API usage

Tracks requests

NOT for database creation

👉 That’s why it shows:

No requests received during the selected time period
🎯 Recommendation for YOU

Since you're learning:
👉 Start with SQLite (default Django DB)

Then later:
👉 Move to MySQL/PostgreSQL

🚀 Next step (important)

Tell me:
👉 Do you want to:

Connect your Django DB to React

See your Notes in database

Use MySQL instead

I’ll guide you step-by-step 🔥

in choreo where is database connectivity option

Good question — and here’s the truth (very important) 👇

👉 In Choreo, there is NO direct “database connectivity” option like a button/menu.

🧠 How database works in Choreo

Choreo is:

❌ NOT a database platform
✅ It is an app + API deployment platform

👉 So database connection is done inside your backend code, not from UI.

🔍 Where you SHOULD look in your screen

From your screenshot:

👉 Left sidebar:

Resources

Connections ✅ (important)

✅ Option 1: Use “Connections” (Recommended)

👉 Go to:

Connections → Create Connection

There you can:

Add external services like:

MySQL

PostgreSQL

MongoDB

👉 This stores:

DB URL

Username

Password

Then Choreo gives you:
👉 Environment variables

✅ Option 2: Use Environment Variables (Most common)

👉 Go to:

Settings → Configurations / Environment Variables

Add:

DB_NAME=mydb
DB_USER=root
DB_PASSWORD=1234
DB_HOST=localhost
DB_PORT=3306
🔥 Then connect in Django (IMPORTANT)

In your Django settings.py:

import os

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
❗ Why you don’t see “Database” button

Because Choreo works like:

Your Code (Django/Node) → connects to DB
Choreo → just runs your app
📌 What your current screen shows

👉 You are in:

Insights → Usage

👉 That is:

API analytics

NOT configuration

🎯 What you should do now
👉 Step-by-step:

Go to Connections

Add DB connection OR

Use Environment Variables

Update Django config

Deploy again

💡 Simple analogy

Choreo = Hosting platform (like Vercel)

Database = separate service (like MySQL)

🚀 If you want next

Tell me:
👉 “I want MySQL setup in Choreo”

I’ll give you:

exact DB service

full Django config

deployment steps

