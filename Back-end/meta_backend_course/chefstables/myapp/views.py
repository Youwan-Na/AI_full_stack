from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def home(request):
    path = request.path
    response = HttpResponse("This work!")
    return response

def hompage(request):
    return HttpResponse("Welcome to Little Lemon!")

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menuitems(request, dish):
    items = {
        'pasta':'pasta is a type of a noodle',
        'falafel' : 'falafel are deep fried patties',
        'cheese cake' : 'Cheese cake for you!',
        "fish_cake" : "This is not recommend..."
    }

    description = items[dish]
    return HttpResponse(f"<h2> {dish} <h2>" + description)