from django.db import models

# Create your models here.



class Autor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40, null = True)
    nacionalidad = models.CharField(max_length=20)

class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    autor = models.CharField(max_length=20)
<<<<<<< HEAD
    editorial = models.CharField(max_length=20, null = True)
=======
>>>>>>> 64e651f631c5b4775243d0d1a87cf7512a31b10b

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    email = models.EmailField(null=True)
