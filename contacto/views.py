
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm


def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name= request.POST.get('nombre', '')
            email = request.POST.get('email', '')
            content = request.POST.get('contenido', '')

            # Creamos el correo
            email = EmailMessage(
                "Via Massage: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["django@hektorprofe.net"],
                reply_to=[email]
            )

            # Lo enviamos y redireccionamos
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contacto')+"?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contacto')+"?fail")
    
    return render(request, "contact/contact.html",{'form':contact_form})

    