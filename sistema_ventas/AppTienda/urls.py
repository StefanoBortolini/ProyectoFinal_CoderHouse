from django.contrib import admin
from django.urls import path

from AppTienda.views import galeria_vechiculos, crear_vehiculos


urlpatterns = [
    # URLS Usuario y sesion
    path('vehiculos/', galeria_vechiculos, name="all_posteos"),
    path('crear_vehiculo', crear_vehiculos, name='crear_vehiculo')
]