from django import forms

# Create your models here.



class FormularioAutores(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    nacionalidad = forms.CharField()

class Libro(forms.Form):
    titulo = forms.CharField()
    autor = forms.CharField()

class Editorial(forms.Form):
    nombre = forms.CharField()
    direccion = forms.CharField()
    email = forms.EmailField()
