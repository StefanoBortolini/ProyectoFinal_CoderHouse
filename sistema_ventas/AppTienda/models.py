from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Posteo(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fcha_posteo         = models.DateField(auto_now_add=True)
    fcha_modificacion   = models.DateField(auto_now=True)
    marca               = models.CharField(max_length=32)
    modelo              = models.CharField(max_length=32)
    year                = models.IntegerField()
    kilometros          = models.IntegerField
    descripcion         = models.CharField(max_length=1500)
    email               = models.EmailField(null=True)
    telefono            = models.IntegerField()
    patente             = models.CharField(max_length=7, blank=True)
    precio              = models.IntegerField()
    fotos               = models.ImageField(upload_to='fotos_vehiculos', null=True, blank=True)