from django.contrib import admin
from django.urls import include, path
from . import views
from django.urls import path,include
from . import views
from .views import eliminar_evento
from .views import agregar_al_carrito
from .views import quitar_del_carrito
from .views import limpiar_carrito

app_name = "TicketOn"
urlpatterns = [

    path('comprador/register/', views.register, name="register"),
    path('comprador/login/',views.my_login, name='my-login'),
    path('comprador/logout', views.user_logout, name="user-logout"),


    #Inicio
    path('', views.Home, name = 'home'),
    path('home/',views.Home,name='home'),
    path('organizador/login/', views.my_loginOrganizador, name='my_loginO'),
    path('organizador/register/', views.registerOrganizador, name='register'),


    #Comprador
    path('comprador/eventos/', views.eventos, name = 'eventos'),
    path('comprador/ayuda/',views.ayuda, name = 'ayuda'),
    path('comprador/carrito/',views.carrito, name='carrito'),
    path('comprador/eventos/<nombre_evento>/<evento_slug>',views.detalles_evento, name="detalles_evento"), #probar ejemplo /comprador/eventos/Evento%20Prueba/1

    #sistema de pagos
    path('evento/agregar_al_carrito/<slug:evento_slug>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('quitar_del_carrito/<int:ticket_id>/', quitar_del_carrito, name='quitar_del_carrito'),
    path('limpiar_carrito/', limpiar_carrito, name='limpiar_carrito'),


    #Organizador
    path('organizador/eventos/',views.Eventos_en_curso,name='eventos_en_curso'),
    path('organizador/eventos/creacion/',views.Creacion_de_eventos, name='creacion_de_eventos'),
    path('organizador/eventos/editar/<slug:evento_slug>/', views.editar_evento, name='editar_evento'),
    path('organizador/ventas/',views.Ventas, name='ventas'),
    path('evento/eliminar/<slug:evento_slug>/', eliminar_evento, name='evento_eliminar'),

]
