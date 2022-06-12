from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from .forms import *
from .models import *
from .services import logic


# Create your views here.


def index(request):
    # list_x, list_y = None, None
    data = None
    main_predict = 0
    brute_predict = []
    if request.method == "POST":
        form = CharacteristicForm(request.POST)
        if form.is_valid():
            data = logic.data_transform(form.cleaned_data)
            main_predict = logic.predict(data)
            brute_params = logic.gen_10to2()
            for params in brute_params:
                brute_data = data.copy()
                brute_data["flag_own_realty"] = params[0]
                brute_data["flag_own_car"] = params[1]
                brute_data["flag_employed"] = params[2]
                brute_data["flag_is_pensioner"] = params[3]
                brute_data["family_status"] = params[4]
                brute_predict.append(round(logic.predict(brute_data), 2))
            # print(data)
            # print(main_predict)
            # print("-----")
            # print(brute_predict)
            # print(predict)
            # list_x = logic.gen_redundant_data(data["salary"][0])
            # list_y = []
            # for i in range(len(list_x)):
            #     data["salary"][0] = list_x[i]
            #     list_y.append(logic.predict(data))
            # print(list_x, '\n', list_y)
    else:
        form = CharacteristicForm()

    return render(request, "index.html", {
        "title": "Dashboard",
        "form": form,
        "data": data,
        "predict": str(round(main_predict, 2)) + " ₽",
        "brute_predict": [str(item) + " ₽" for item in brute_predict]
    })


def get_cities_info(request):
    response = [item["name"].strip() for item in Cities.objects.values('name').distinct()]
    return JsonResponse(response, safe=False)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Error 404</h1>")
