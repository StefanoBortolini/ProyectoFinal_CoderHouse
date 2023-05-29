from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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
def mis_vechiculos(request):
    contexto = {
        'vehiculos': Posteo.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='AppTienda/mis_posteos.html',
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
def eliminar_posteo(request, id):
    posteo = Posteo.objects.get(id=id)
    if request.method == 'POST':
        posteo.delete()
        return redirect('all_posteos')
    else:
        return HttpResponse("No se pudo ELIMINAR el registro")


class ModificarPosteo(LoginRequiredMixin, UpdateView):
    model = Posteo
    form_class = CrearPosteo
    template_name = 'AppTienda/modificar_posteo.html'
    success_url = reverse_lazy('all_posteos')

    def get_object(self):
        # Obtener el registro que tiene el mismo id que el pk de la URL
        return get_object_or_404(Posteo, id=self.kwargs['pk'])


# def eliminar_posteo(request):
#     if request.method == "POST":
#         data = request.POST
#         id_posteo = data["id_posteo"]
#         posteo = Posteo.objects.get(id=id_posteo)
#         posteo.delete()
#         return redirect('all_posteos')
#     else:
#         return HttpResponse("No se pudo ELIMINAR el registro")