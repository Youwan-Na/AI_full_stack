from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def home(reqeust):
    return HttpResponse("Hello")

def hompage(request):
    return HttpResponse("Welcome to Little Lemon!")

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)