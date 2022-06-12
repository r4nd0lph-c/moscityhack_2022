from django.contrib import admin
from .models import *


# Register your models here.


class CitiesAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)


admin.site.register(Cities, CitiesAdmin)
admin.site.site_title = 'Dashboard'
admin.site.site_header = 'Dashboard | База данных'
admin.site.index_title = 'Администрирование приложения'
