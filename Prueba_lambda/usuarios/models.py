from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    genero = models.CharField(max_length=10)
    cc = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre
