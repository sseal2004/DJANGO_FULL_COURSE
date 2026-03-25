# Installation 
# Step:1 install uv for powershell

irm https://astral.sh/uv/install.ps1 | iex

# Step:2 Set path
$env:Path = "C:\Users\ADMIN\.local\bin;$env:Path"

# Step:3 Create that virtual environment
uv venv

# Step:4 You will see a venv folder will be created
From that venv folder we have to run the activation script

.venv\Scripts\activate

# Step:5 Django installation 
uv pip install Django

# Step:6 To start a new project in django
django-admin startproject ChaiAurCode

# Now you will see a folder named ./projectName/projectName created inside that and a manage.py file too
(Django2) PS D:\Django2> cd ChaiAurCode
(Django2) PS D:\Django2\ChaiAurCode> ls


    Directory: D:\Django2\ChaiAurCode


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        22-03-2026     19:54                ChaiAurCode
-a----        22-03-2026     19:54            689 manage.py

Here you can see one folder ChaiAurCode and manage.py is been created

# Step:7 Command to run the server 
python manage.py runserver

Default Python port:
Starting development server at http://127.0.0.1:8000/

You can choose your own port too:
python manage.py runserver 8001






