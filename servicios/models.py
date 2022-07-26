from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

# class Servicios(models.Model):


#     #id = models.AutoField(primary_key=True)
#     categoria = models.CharField(max_length=200)
#     titulo = models.CharField(max_length=40)
#     subtitulo = models.CharField(max_length=40)
#     contenido = RichTextField()
#     fecha = models.DateField(default=datetime.now)
#     imagen = models.URLField(max_length = 255, blank = False, null= False)

#     class Meta:
#         verbose_name_plural = "servicios"
#         verbose_name = "servicio"

#     def __str__(self):
#         return f'{self.titulo} by {self.categoria}'

class Servicios(models.Model):


    categoria = models.CharField(max_length=200, verbose_name="Category")
    titulo = models.CharField(max_length=200, verbose_name="Título")
    subtitulo = models.CharField(max_length=200, verbose_name="Subtítulo")
    contenido = models.TextField(verbose_name="Contenido")
    #imagen = models.ImageField(verbose_name="Imagen", upload_to="Masajes")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['-creado']

    def __str__(self):
        return self.titulo