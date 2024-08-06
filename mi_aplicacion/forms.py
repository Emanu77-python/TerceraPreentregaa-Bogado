from django import forms

# Create your models here.



class FormularioAutores(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    nacionalidad = forms.CharField()

class FormularioLibro(forms.Form):
    titulo = forms.CharField()
    autor = forms.CharField()
    editorial= forms.CharField()


class FormularioEditorial(forms.Form):
    nombre = forms.CharField()
    autor = forms.CharField()
    email= forms.EmailField()