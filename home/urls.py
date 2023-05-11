from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
     path('api/get_hotel/', get_hotel, name='get_hotel')
]

