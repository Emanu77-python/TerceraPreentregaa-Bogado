from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Autor, Libro, Editorial
from .forms import AutorForm, LibroForm, EditorialForm
# Create your views here.

def inicio(request):
    return render(request)


def autores(request):
    return render(request)


def libros(request):
    return render(request)
