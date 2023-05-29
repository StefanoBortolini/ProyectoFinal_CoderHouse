from django.contrib import admin
from django.urls import path

from AppPerfiles.views import registro, login_view, CustomLogoutView, MiPerfilUpdateView, agregar_avatar


urlpatterns = [
    # URLS Usuario y sesion
    path('signup/', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    # URLS de Perfil
    path('profile/', MiPerfilUpdateView.as_view(), name="editar_perfil"),
    path('change_avatar/', agregar_avatar, name="agregar_avatar"),
]