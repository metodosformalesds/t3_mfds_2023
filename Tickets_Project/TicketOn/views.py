from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .forms import UserRegisterForm
from .models import Evento

# Inicio
def Home(request):
    return render(request, 'Inicio/Home.html')

def comprador_login(request):
    return render(request, 'Inicio/comprador_login.html')

def organizador_login(request):
    return render(request, 'Inicio/organizador_login.html')

def comprador_register(request):
    return render(request, 'Inicio/comprador_register.html')

def organizador_register(request):
    return render(request, 'Inicio/organizador_register.html')

#Comprador
def eventos(request):
    return render (request,'Comprador/Eventos.html')

def ayuda(request):
    return render (request,'Comprador/Ayuda.html')

def carrito(request):
    return render (request,'Comprador/Carrito.html')



def detalles_evento(request,nombre_evento,evento_slug):
    evento= Evento.objects.get(slug=evento_slug)
    return render(request,'Detalles_Evento.html',{
        "evento":evento
    })



#Organizador
def Eventos_en_curso(request):
    return render(request, 'Organizador/Eventos_en_curso.html')

def Creacion_de_eventos(request):
    return render(request, 'Organizador/Creacion_de_eventos.html')

def Editar_eventos(request):
    return render(request, 'Organizador/Editar_eventos.html')

def Ventas(request):
    return render(request, 'Organizador/Ventas.html')





