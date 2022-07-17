from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.login_request, name="login"),
    path('registro', views.register, name="registro"),
    path('logout', LogoutView.as_view(template_name='login/logout.html'), name='logout'),
    path('editarPerfil', views.editarPerfil, name='editarPerfil'),
]