from django.contrib import admin
from .models import *
# Register your models here.


class HotelAdmin(admin.ModelAdmin):
    list_display = ['hotel_name','hotel_price','hotel_desc']

admin.site.register(Amenities)
admin.site.register(Hotel)
admin.site.register(HotelImage)
