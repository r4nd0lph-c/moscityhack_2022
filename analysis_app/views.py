from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html', {'title': "index"})


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
