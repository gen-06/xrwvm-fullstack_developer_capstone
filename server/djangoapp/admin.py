from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.


# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'car_make', 'dealer_id', 'year')
    # Enable search on these fields
    search_fields = ('name', 'car_make__name')
    # Add filters for these fields
    list_filter = ('car_make', 'year')


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
