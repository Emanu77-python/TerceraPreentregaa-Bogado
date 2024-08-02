from django.shortcuts import render, redirect
from mi_aplicacion.forms import FormularioAutores
from mi_aplicacion.models import Autor
from .forms import FormularioAutores
# Create your views here.

def inicio(request):
    return render(request, "mi_aplicacion/base.html")


def autores(request):
    return render(request, "mi_aplicacion/autores.html")

def libros(request):
    return render(request, "mi_aplicacion/libros.html")

def editorial(request):
    return render(request, "mi_aplicacion/editorial.html")

def agregar_autor(request):
    if request.method == 'POST':
        autor = Autor(nombre=request.POST["nombre"], apellido=request.POST["apellido"], nacionalidad=request.POST["nacionalidad"])
        autor.save()

        return render(request, "mi_aplicacion/inicio.html")
    return render(request, "mi_aplicacion/formulario_autor.html")



