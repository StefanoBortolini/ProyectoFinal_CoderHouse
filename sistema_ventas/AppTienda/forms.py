from django import forms
from AppTienda.models import *


class CrearPosteo(forms.ModelForm):
    class Meta:
        model = Posteo
        fields = ['marca', 'modelo', 'year', 'kilometros', 'descripcion', 'email', 'telefono', 'patente', 'precio', 'fotos']
