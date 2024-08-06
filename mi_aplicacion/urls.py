from django.urls import path
from mi_aplicacion import views
from mi_aplicacion.views  import *

urlpatterns = [
    path("", inicio),
    path("autores/", autores, name="autores"),
    path("libros/", libros , name="libros"),
    path("editoriales/", editorial, name="editorial"),
    path('formulario_autor/', agregar_autor, name="formulario_autor"),
    path('formulario_libro', agregar_libro, name='formulario_libro'),
    path('formulario_editorial', agregar_editorial, name='formulario_editorial'),
    path('buscar_autor', buscar_autor, name= 'buscar_autor'),
    path('buscar_libro', buscar_libro, name= 'buscar_libro'),
    path('buscar_editorial', buscar_editorial, name= 'buscar_editorial'),
    path("acerca", acerca, name= "acerca"),

]


