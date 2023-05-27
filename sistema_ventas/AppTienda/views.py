from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

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
        form = CrearPosteo(request.POST, request.FILES)
        if form.is_valid():
            posteo = form.save(commit=False)
            posteo.user = request.user
            posteo.save()
            return redirect('all_posteos')
        else:
            print(form.errors)
    else:
        form = CrearPosteo()
    return render(request, 'AppTienda/formulario_posteo.html', {'form': form})
    

class VehiculoDetailView(DetailView):
    model = Posteo
    success_url = reverse_lazy('inicio')
    
@login_required
def Reserva(request):
    if request.method == "POST":
        data = request.POST
        id_posteo = data["id_posteo"]
        reservado = data["reservado"]
        user_reserva = data["user_reserva"]
        posteo = Posteo.objects.get(id__contains=id_posteo)
        posteo.reserva = reservado
        posteo.user_reserva = user_reserva
        posteo.save()
        return redirect('all_posteos')
 
@login_required
def eliminar_posteo(request):
    if request.method == "POST":
        data = request.POST
        id_posteo = data["id_posteo"]
        posteo = Posteo.objects.get(id=id_posteo)
        posteo.delete()
        return redirect('all_posteos')
    else:
        return HttpResponse("No se pudo ELIMINAR el registro")