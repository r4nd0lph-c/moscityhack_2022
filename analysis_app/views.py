from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from .forms import *
from .models import *
from .services import logic


# Create your views here.


def index(request):
    list_x, list_y = None, None
    if request.method == "POST":
        form = CharacteristicForm(request.POST)
        if form.is_valid():
            data = logic.data_transform(form.cleaned_data)
            predict = logic.predict(data)
            # print(data)
            # print(predict)
            list_x = logic.gen_redundant_data(data["salary"][0])
            list_y = []
            for i in range(len(list_x)):
                data["salary"][0] = list_x[i]
                list_y.append(logic.predict(data))
            # print(list_x, '\n', list_y)
    else:
        form = CharacteristicForm()

    return render(request, "index.html", {
        "title": "Dashboard",
        "form": form,
        "list_x": list_x,
        "list_y": list_y
    })


def get_cities_info(request):
    response = [item["name"].strip() for item in Cities.objects.values('name').distinct()]
    return JsonResponse(response, safe=False)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Error 404</h1>")
