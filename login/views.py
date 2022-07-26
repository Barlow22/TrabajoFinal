from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import UserEditForm, UserRegisterForm

# Create your views here.

#login

def login_request(request):
    
      if request.method == "POST":

            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username = usuario , password = contra)
                  
                  if user is not None:
                        login(request, user)

                        return render (request, "core/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
                  else:
                        
                        return render (request, "login/login.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "login/login.html", {"mensaje":"Formulario erroneo"})
      

      form = AuthenticationForm()
      return render(request, "login/login.html", {'form': form})

def register(request):
      
      if request.method == "POST":

            form = UserRegisterForm(request.POST)

            if form.is_valid():
                  username = form.cleaned_data['username']
                 
                  form.save()

                  return render(request, "core/inicio.html", {"mensaje": "usuario creado"})

      else: 
            form = UserRegisterForm()

      return render(request, "login/registro.html", {"form": form})

@login_required
def editarPerfil(request):
      #se instancia el Login; 
      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid(): #si pasa la validación Django
                  informacion = miFormulario.cleaned_data
                  
                  #datos que modificaríamos
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.last_name = informacion['last_name']
                  usuario.first_name = informacion['first_name']

                  usuario.save()
            
                  return render(request, "login/editarPerfil.html", {"mensaje": "Informacion actualizada correctamente"}) #vuelvo a inicio

      else:
            #creo el formulario con los datos que voy a modificar
            miFormulario = UserEditForm(initial={'email':usuario.email})
      
      #voy al HTML que me permite editar
      return render(request, "login/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
