from django.contrib import admin
from django.urls import path
from AppShop import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('alimentos', views.alimentos, name='Alimentos'),
    path('accesorios', views.accesorios, name='Accesorios'),
    path('juguetes', views.juguetes, name='Juguetes'),
    path('agregar-alimento', views.alimento_formulario, name='AgregarAlimentos'),
    path('agregar-accesorio', views.accesorios_formulario, name='AgregarAccesorios'),
    path('agregar-juguete', views.juguetes_formulario, name='AgregarJuguetes'),    
    path('busq-mascota', views.busqueda_mascota, name="BusquedaMascota"),
    path('buscar', views.buscar, name="Buscar"),
]