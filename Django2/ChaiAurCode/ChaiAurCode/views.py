from django.http import HttpResponse
from django.shortcuts import render # Used to load html pages

def home(request):
    # return HttpResponse("Hello World. Your are at Chai and Django home page")
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("Hello World. Your are at Chai and Django about page")

def contact(request):
    return HttpResponse("Hello World. Your are at Chai and Django contact page")
