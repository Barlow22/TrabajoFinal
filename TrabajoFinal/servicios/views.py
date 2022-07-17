from django.shortcuts import render
from .models import Servicios
from django.contrib.auth.decorators import login_required

# Create your views here.

def agregarServicios(request):
    form = Servicios()
    data = {'form':form}
    if request.method == 'POST':
        miformulario = Servicios(request.POST)
        print(miformulario)
        if miformulario.is_valid:
            informacion = miformulario.cleaned_data
            miformulario.save()
            data['mensaje'] = "Datos Resgistrados"
            return render(request, 'servicios/servicios.html')
    else:
        miformulario= Servicios()
    return render(request, '', data)

@login_required
def servicios(request):
    servicios = Servicios.objects.all()
    return render(request, "servicios/servicios.html", {'servicios':servicios})