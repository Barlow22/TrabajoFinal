from django.shortcuts import render
from .models import Servicios
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy




# Create your views here.

# def agregarServicios(request):

#     form = Servicios()
#     data = {'form':form}

#     if request.method == 'POST':
#         miFormulario = Servicios(request.POST)

#         if miFormulario.is_valid:
#             informacion = miFormulario.cleaned_data
#             miFormulario.save()
#             data['mensaje'] = "Datos Resgistrados"
#             return render(request, 'servicios/servicios.html')
#     else:
#         miFormulario= Servicios()
#     return render(request, '', data)

# @login_required
# def servicios(request):
#     servicios = Servicios.objects.all()
#     return render(request, "servicios/servicios.html", {'servicios':servicios})

# def leerServicios(request):
#     productos = Servicios.objects.all()
#     contexto = {"servicios" : servicios}
#     return render(request, 'servicios/leerServicios.html', contexto)

class ServiciosList(ListView):

    model = Servicios
    template_name = 'servicios_list.html'


class ServiciosDetalle(DetailView):

      model = Servicios
      template_name = "servicios/servicios_detalle.html"



class ServiciosCreacion(CreateView):

      model = Servicios
      success_url = reverse_lazy('List')
      fields = ['categoria', 'titulo', 'subtitulo', 'contenido']


class ServiciosUpdate(UpdateView):

      model = Servicios
      success_url = reverse_lazy('List')
      fields  = ['categoria', 'titulo', 'subtitulo', 'contenido']


class ServiciosDelete(DeleteView):

      model = Servicios
      success_url = reverse_lazy('List')