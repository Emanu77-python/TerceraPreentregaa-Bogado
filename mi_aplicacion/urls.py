from django.urls import path

from mi_aplicacion.views  import inicio, autores, libros

urlpatterns = [
    path("", inicio),
    path('autores/', autores),
    path('libros/', libros),
]

