from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# Create your views here.

def index(request):
    return HttpResponse("<h1>Страница приложения analysis</h1>")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
