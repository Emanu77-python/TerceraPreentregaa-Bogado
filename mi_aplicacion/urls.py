from django.urls import path
from mi_aplicacion import views
from mi_aplicacion.views  import *

urlpatterns = [
    path("", inicio),
    path("autores/", autores, name="autores"),
    path("libros/", libros , name="libros"),
    path("editoriales/", editorial, name="editorial"),
<<<<<<< HEAD
    path('formulario_autor/', agregar_autor, name="formulario_autor"),
    path('formulario_libro', agregar_libro, name='formulario_libro'),
    path('formulario_editorial', agregar_editorial, name='formulario_editorial'),
    path('buscar_autor', buscar_autor, name= 'buscar_autor'),
    path('buscar_libro', buscar_libro, name= 'buscar_libro'),
    path('buscar_editorial', buscar_editorial, name= 'buscar_editorial'),
    path("acerca", acerca, name= "acerca"),
=======
    path('formulario_autor/', views.agregar_autor, name="formulario_autor"),
>>>>>>> 64e651f631c5b4775243d0d1a87cf7512a31b10b

]


