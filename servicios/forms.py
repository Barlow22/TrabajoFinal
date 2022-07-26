from dataclasses import fields
from django import forms 
from .models import Servicios

# class ServiciosFormulario(forms.Form):

#     categoria = forms.CharField(max_length=200)
#     titulo = forms.CharField(max_length=40)
#     subtitulo = forms.CharField(max_length=40)
#     contenido = forms.CharField(max_length=1000)
#     fecha = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
#     imagen = forms.ImageField()

#     class Meta: #Esto es para que el formulario sepa que campos tiene que mostrar
#       model = Servicios
#       fields = ['categoria', 'titulo', 'subtitulo', 'contenido', 'fecha', 'imagen']


class ServiciosFormulario(forms.Form):   


    categoria = forms.CharField(max_length=200, verbose_name="Category")
    titulo = forms.CharField(max_length=200, verbose_name="Título")
    subtitulo = forms.CharField(max_length=200, verbose_name="Subtítulo")
    contenido = forms.CharField(label="Contenido", required=False, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 3, 'placeholder':'Escribe tu mensaje'}
    ), min_length=10, max_length=1000)
    #imagen = forms.ImageField(verbose_name="Imagen", upload_to="Servicios", required=False)