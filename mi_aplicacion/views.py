from django.shortcuts import render, redirect
<<<<<<< HEAD
from mi_aplicacion.models import Autor, Libro, Editorial
from .forms import FormularioAutores
from django.http import HttpResponse
=======
from mi_aplicacion.forms import FormularioAutores
from mi_aplicacion.models import Autor
from .forms import FormularioAutores
>>>>>>> 64e651f631c5b4775243d0d1a87cf7512a31b10b
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


<<<<<<< HEAD
def agregar_editorial(request):
    if request.method == 'POST':
        editorial = Editorial(nombre=request.POST["nombre"], direccion=request.POST["direccion"], email=request.POST["email"])
        editorial.save()

        return render(request, "mi_aplicacion/inicio.html")
    return render(request, "mi_aplicacion/formulario_editorial.html")

def agregar_libro(request):
    if request.method == 'POST':
        titulo_1 = request.POST.get('titulo')
        autor_1 = request.POST.get('autor')
        editorial_1 = request.POST.get('editorial')

        nuevo_libro = Libro(titulo=titulo_1, autor=autor_1, editorial=editorial_1)
        nuevo_libro.save()
        return render(request, 'mi_aplicacion/formulario_libro.html')
    
    return render(request, 'mi_aplicacion/formulario_libro.html')

def buscar_autor(request):
    if request.GET['nombre']:
        autor = request.GET['nombre']
        autor = Autor.objects.filter(nombre__icontains=autor)

        return render(request, "mi_aplicacion/resultados_autor.html",{'autor':autor, 'query': autor })
    else:
        respuesta = 'No has escribido nada  '
    return HttpResponse(respuesta)

def buscar_libro(request):
    titulo = request.GET.get('titulo', '')
    autor = request.GET.get('autor', '')
    editorial = request.GET.get('editorial', '')


    libros = []

    if titulo or autor or editorial:

        libros = Libro.objects.filter(
            titulo__icontains=titulo,
            autor__icontains=autor,
            editorial__icontains=editorial
        )
    else:
        libros = []

    return render(request, 'mi_aplicacion/resultados_libro.html', {'libros': libros})

def buscar_editorial(request):
    nombre = request.GET.get('nombre', '')
    direccion = request.GET.get('direccion', '')
    email = request.GET.get('email', '')


    editorial = []

    if nombre or direccion or email:

        editorial = Editorial.objects.filter(
            nombre__icontains=nombre,
            direccion__icontains=direccion,
            email__icontains=email
        )
    else:
        editorial = []

    return render(request, 'mi_aplicacion/resultados_editorial.html', {'editorial': editorial})

def acerca(request):
    return render(request, "mi_aplicacion/template.html")
=======
>>>>>>> 64e651f631c5b4775243d0d1a87cf7512a31b10b

