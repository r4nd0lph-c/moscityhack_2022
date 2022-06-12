from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from .forms import *
from .models import *
from .services import logic


# Create your views here.


def index(request):
    if request.method == "POST":
        form = CharacteristicForm(request.POST)
        if form.is_valid():
            data = logic.data_transform(form.cleaned_data)
            print(data)
    else:
        form = CharacteristicForm()

    return render(request, "index.html", {
        "title": "Dashboard",
        "form": form,
    })


def get_cities_info(request):
    response = [item["name"].strip() for item in Cities.objects.values('name').distinct()]
    return JsonResponse(response, safe=False)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Error 404</h1>")
