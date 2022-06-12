from django.http import HttpResponseNotFound
from django.shortcuts import render
from .forms import *
from .models import *


# Create your views here.


def index(request):
    if request.method == "POST":
        form = CharacteristicForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = CharacteristicForm()

    return render(request, "index.html", {
        "title": "Dashboard",
        "form": form,
        "list_cities": [item["name"] for item in Cities.objects.values('name').distinct()]
    })


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
