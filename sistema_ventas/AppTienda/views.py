from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from AppTienda.forms import CrearPosteo
from AppTienda.models import Posteo

# Create your views here.

def galeria_vechiculos(request):
    contexto = {
        'vehiculos': Posteo.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='AppTienda/all_posteos.html',
        context=contexto,
    )
    return http_response

@login_required
def crear_vehiculos(request):
    if request.method == 'POST':
        # formulario = CrearPosteo(request.POST)

        # if formulario.is_valid():
            # data        = formulario.cleaned_data
        data        = request.POST
        user        = request.user
        marca       = data['marca']
        modelo      = data['modelo']
        year        = data['year']
        kilometros  = data['kilometros']
        descripcion = data['descripcion']
        email       = data['email']
        telefono    = data['telefono']
        patente     = data['patente']
        precio      = data['precio']
        fotos       = data['fotos']
        crear_posteo= Posteo(user=user, marca=marca, modelo=modelo, year=year, kilometros=kilometros, descripcion=descripcion, email=email, telefono=telefono, patente=patente, precio=precio, fotos=fotos)
        crear_posteo.save()

        url_exitosa = reverse('inicio')
        return redirect(url_exitosa)
    else:
        # formulario = CrearPosteo()
        http_response = render(
            request=request,
            template_name='AppTienda/formulario_posteo.html',
            # context={'formulario': formulario}
        )
        return http_response