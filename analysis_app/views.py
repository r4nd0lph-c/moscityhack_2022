from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .forms import *


# Create your views here.

def index(request):
    if request.method == "POST":
        form = CheckForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = CheckForm()
    return render(request, "index.html", {"title": "index", "form": form})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
