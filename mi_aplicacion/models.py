from django.db import models

# Create your models here.



class Autor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40, null = True)
    nacionalidad = models.CharField(max_length=20)

class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=20)

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    email = models.EmailField(null=True)
