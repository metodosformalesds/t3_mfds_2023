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
from django.contrib.auth.views import LoginView, LogoutView
from TicketOn import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("TicketOn.urls")),
    path('', views.Home, name = 'home'),
    path('home/',views.Home,name='home'),
    path('signup/', views.signup, name = 'signup'),
    path('eventos/', views.eventos, name = 'eventos'),
    path('logout/', views.CS, name = 'logout'),
    path('signin/', views.IS, name = 'signin'),
    path('ayuda/',views.ayuda, name = 'ayuda'),
    path('carrito/',views.carrito, name='carrito'),
    path('eventos_en_curso/',views.Eventos_en_curso,name='eventos_en_curso'),
    path('creacion_de_eventos/',views.Creacion_de_eventos, name='creacion_de_eventos'),
    path('editar_eventos/',views.Editar_eventos, name='editar_eventos'),
    path('ventas/',views.Ventas, name='ventas'),
    path('Login_Organizador/', views.OrganizadorRegister, name = 'Login_Organizador')

]
