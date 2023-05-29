from django.contrib import admin
from django.urls import path

from AppTienda.views import galeria_vechiculos, mis_vechiculos, crear_vehiculos, VehiculoDetailView, Reserva, eliminar_posteo, ModificarPosteo


urlpatterns = [
    # URLS Usuario y sesion
    path('vehiculos/', galeria_vechiculos, name="all_posteos"),
    path('mis_vehiculos/', mis_vechiculos, name="mis_posteos"),
    path('crear_vehiculo/', crear_vehiculos, name='crear_vehiculo'),
    path('ver_vehiculo/<int:pk>/', VehiculoDetailView.as_view(), name='ver_vehiculo'),
    path('reservar/', Reserva, name='Reserva'),
    path('eliminar_posteo/<int:id>/', eliminar_posteo, name='eliminar'),
    path('modificar_posteo/<int:pk>/', ModificarPosteo.as_view(), name='modificar'),
]