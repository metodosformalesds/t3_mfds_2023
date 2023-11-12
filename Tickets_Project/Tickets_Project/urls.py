from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth.views import LoginView, LogoutView
from TicketOn import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("TicketOn.urls")),
    path('accounts/', include('allauth.urls')),
    path('login/', views.login, name = 'login'),
    path('accounts/login/', LoginView.as_view(template_name='accounts/login.html'), name='account_login'),

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
    path('creacion_de_eventos/',views.Creacion_de_eventos, name='creacion_de_eventos'),
    path('editar_eventos/',views.Editar_eventos, name='editar_eventos'),
    path('ventas/',views.Ventas, name='ventas'),

]
