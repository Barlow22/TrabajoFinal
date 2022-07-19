from django.urls import path
from . import views

urlpatterns = [
    # path('', views.servicios, name="servicios"),

    path('list', views.ServiciosList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.ServiciosDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.ServiciosCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ServiciosUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ServiciosDelete.as_view(), name='Delete'),
]