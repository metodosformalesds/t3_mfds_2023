from django.contrib import admin
from django.urls import include, path
from . import views
from django.urls import path,include
from . import views

app_name = "TicketOn"
urlpatterns = [

    path('comprador/register/', views.register, name="register"),
    path('comprador/login/',views.comprador_login, name='comprador_login'),

    #Inicio
    path('', views.Home, name = 'home'),
    path('home/',views.Home,name='home'),
    path('organizador/login/', views.organizador_login, name='organizador_login'),
    path('organizador/register/', views.organizador_register, name='organizador_register'),


    #Comprador
    path('comprador/eventos/', views.eventos, name = 'eventos'),
    path('comprador/ayuda/',views.ayuda, name = 'ayuda'),
    path('comprador/carrito/',views.carrito, name='carrito'),
    path('comprador/eventos/<nombre_evento>/<evento_slug>',views.detalles_evento, name="detalles_evento"), #probar ejemplo /comprador/eventos/Evento%20Prueba/1

    #Organizador
    path('organizador/eventos/curso/',views.Eventos_en_curso,name='eventos_en_curso'),
    path('organizador/eventos/creacion/',views.Creacion_de_eventos, name='creacion_de_eventos'),
    path('organizador/editar/eventos/',views.Editar_eventos, name='editar_eventos'),
    path('organizador/ventas/',views.Ventas, name='ventas'),

]
