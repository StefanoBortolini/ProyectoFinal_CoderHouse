# Importamos la clase TestCase, el modelo Posteo y el cliente de prueba
from django.test import TestCase
from AppTienda.models import Posteo
from django.contrib.auth.models import User

class PosteoModelTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(username="usuario1", email="usuario1@gmail.com", password="123456")
        Posteo.objects.create(user=user, marca="Ford", modelo="Fiesta", year=2010, kilometros=50000, descripcion="Buen estado", email="usuario1@gmail.com", telefono=123456789, precio=100000)

    def test_posteo_year(self):
        posteo = Posteo.objects.get(id=1)
        self.assertEqual(posteo.year, 2010)

    def test_posteo_precio(self):
        posteo = Posteo.objects.get(id=1)
        self.assertEqual(posteo.precio, 100000)