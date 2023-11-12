from django.contrib import messages
from multiprocessing import context
from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm, EventoForm, OrganizadorForm
from .models import Evento

# Inicio
def login(request):
    return render(request, 'account/login.html')

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
    eventos = Evento.objects.all()
    return render (request,'Comprador/Eventos.html',{'eventos':eventos})

def ayuda(request):
    return render (request,'Comprador/Ayuda.html')

def carrito(request):
    return render (request,'Comprador/Carrito.html')



def detalles_evento(request,nombre_evento,evento_slug):
    evento= Evento.objects.get(slug=evento_slug)
    return render(request,'Comprador/Detalles_Evento.html',{
        "evento":evento
    })



#Organizador
def Eventos_en_curso(request):
    return render(request, 'Organizador/Eventos_en_curso.html')

def Creacion_de_eventos(request):
    if request.method == 'GET':
        return render(request, 'Organizador/Creacion_de_eventos.html',{
            'form': EventoForm()
        })
    elif request.method == 'POST':
        try:
            form = EventoForm(request.POST)
            if form.is_valid():
                new_evento = form.save(commit = False)
                new_evento.Organizador = request.user
                new_evento.save()
                return redirect ('eventos')
        except ValueError:
            return render(request, 'Organizador/Creacion_de_eventos.html',{
                'form': EventoForm(),
                'error': 'Ingrese los datos necesarios'
                })
        return HttpResponse("Algo salió mal")

def Editar_eventos(request):
    return render(request, 'Organizador/Editar_eventos.html')

def Ventas(request):
    return render(request, 'Organizador/Ventas.html')
