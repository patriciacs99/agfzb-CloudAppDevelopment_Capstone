from django.contrib import admin
from .models import *

# Register your models here.

# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display=("name","type","year","dealerId")

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [
        CarModelInline,
    ]
    list_display=("name","description")

# Register models here
admin.site.register(CarModel,CarModelAdmin)
admin.site.register(CarMake,CarMakeAdmin)
