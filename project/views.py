from django.shortcuts import render, HttpResponse

from .models import *

def person(request):
    return HttpResponse(f'<h1>done person</h1>')

def tache(request):
    return HttpResponse("<h1>done tache</h1>")

def login(request):
    person = Person.objects.all()
    return HttpResponse(person)

