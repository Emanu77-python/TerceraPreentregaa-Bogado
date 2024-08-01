from django.shortcuts import render, redirect
from .models import Autor, Libro, Editorial
from .forms import AutorForm, LibroForm, EditorialForm
# Create your views here.

def inicio(request):
    return render(request)

def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'mi_aplicacion/agregar_autor.html', {'form': form})

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'mi_aplicacion/agregar_libro.html', {'form': form})

def agregar_editorial(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio') 
    else:
        form = EditorialForm()
    return render(request, 'mi_aplicacion/agregar_editorial.html', {'form': form})


def buscar_libro(request):
    query = request.GET.get('q')
    resultados = Libro.objects.filter(titulo__icontains=query) if query else None
    return render(request, 'mi_aplicacion/buscar_libro.html', {'resultados': resultados})
