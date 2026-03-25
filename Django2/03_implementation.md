# Step:1 Go to views.py file
# Step:2 Take a http request from django 
    from django.http import HttpResponse
# Step:3 Now build some functions or methods (Routes) 
    
def home(request):
    return HttpResponse("Hello World. Your are at Chai and Django home page")

def about(request):
    return HttpResponse("Hello World. Your are at Chai and Django about page")

def contact(request):
    return HttpResponse("Hello World. Your are at Chai and Django contact page")


# Step:4  Go to urls.py file . To import views.py file  

from . import views 
  
# Step:5 Set the Home page routes , here name="home" is the name of the routes is an optional parameter
    path('',views.home,name="home"), 
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),

# Step: 6 Check to run the server 
python manage.py migrate
python manage.py runserver

# Step: 7 Create templates folder and static folder in django at root folder which will acts like layout and it is extensively used 

# static folder contains css and javascript files
# templates folder contains html file

# Step: 8  Used to load html pages add this command in views.py
from django.shortcuts import render 

def home(request):
    # return HttpResponse("Hello World. Your are at Chai and Django home page")
    return render(request,'website/index.html') 
    <!-- go inside one directory website/index.html inside templates -->
# Step: 9 But this will give you an error as u haven't mentioned where to use template for that come to settings.py

# Step:10 Inside settings.py you will find a section named as TEMPLATES array
At there mention the directory such as:
'DIRS': ['templates'],
# Step:11 Now the localhost will loads perfectly
# Step:12 Create a style.css in static folder
inject that syle.css in index.html
# Step:13 
{% load static %}

<link rel="stylesheet" href="{% static 'style.css' %}">

# Step:14 This will give an error that Did you forget to set the path /static/style.css
 Go to settings.py
# Step:15 
import os
add thisd line after 
STATIC_URL = 'static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]




