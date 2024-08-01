from django.urls import path

from mi_aplicacion.views  import inicio ,agregar_autor, agregar_libro, agregar_editorial, buscar_libro

urlpatterns = [
    path("", inicio),
    path('agregarautor/', agregar_autor),
    path('agregarlibro/', agregar_libro),
    path('agregareditorial/', agregar_editorial),
    path("buscarlibro", buscar_libro)
]

