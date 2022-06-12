from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("get_cities_info/", get_cities_info, name="get_cities_info"),
]
