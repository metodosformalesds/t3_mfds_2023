"""
URL configuration for Tickets_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from TicketOn import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("TicketOn.urls")),

    #Inicio
    path('', views.Home, name = 'home'),
    path('home/',views.Home,name='home'),
    path('comprador_login/',views.comprador_login, name='comprador_login'),
    path('organizador_login', views.organizador_login, name='organizador_login'),
    path('comprador_register/',views.comprador_register, name='comprador_register'),
    path('organizador_register', views.organizador_register, name='organizador_register'),


    #Comprador
    path('eventos/', views.eventos, name = 'eventos'),
    path('ayuda/',views.ayuda, name = 'ayuda'),
    path('carrito/',views.carrito, name='carrito'),

    #Organizador
    path('eventos_en_curso/',views.Eventos_en_curso,name='eventos_en_curso'),
    path('eventos/creacion/',views.Creacion_de_eventos, name='creacion_de_eventos'),
    path('editar_eventos/',views.Editar_eventos, name='editar_eventos'),
    path('ventas/',views.Ventas, name='ventas')

]
