from django import forms

# Create your models here.



class FormularioAutores(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    nacionalidad = forms.CharField()

<<<<<<< HEAD
class FormularioLibro(forms.Form):
    titulo = forms.CharField()
    autor = forms.CharField()
    editorial= forms.CharField()


class FormularioEditorial(forms.Form):
=======
class Libro(forms.Form):
    titulo = forms.CharField()
    autor = forms.CharField()

class Editorial(forms.Form):
>>>>>>> 64e651f631c5b4775243d0d1a87cf7512a31b10b
    nombre = forms.CharField()
    direccion = forms.CharField()
    email = forms.EmailField()
