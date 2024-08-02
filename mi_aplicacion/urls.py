from django.urls import path
from mi_aplicacion import views
from mi_aplicacion.views  import *

urlpatterns = [
    path("", inicio),
    path("autores/", autores, name="autores"),
    path("libros/", libros , name="libros"),
    path("editoriales/", editorial, name="editorial"),
    path('formulario_autor/', views.agregar_autor, name="formulario_autor"),

]


