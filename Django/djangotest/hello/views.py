from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def krish(request):
    return HttpResponse("Hello, Krish!")

def beachoo(request):
    return HttpResponse("Hello, beachoo!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")