from django import forms

class CrearPosteo(forms.Form):
    marca       = forms.CharField(required=True, max_length=32)
    modelo      = forms.CharField(required=True, max_length=32)
    year        = forms.DateField(required=True)
    kilometros  = forms.IntegerField(required=True)
    descripcion = forms.CharField(required=True, max_length=1500)
    email       = forms.EmailField()
    telefono    = forms.IntegerField(required=True)
    patente     = forms.IntegerField(max_value=7)
    precio      = forms.IntegerField(required=True)
    fotos       = forms.ImageField()