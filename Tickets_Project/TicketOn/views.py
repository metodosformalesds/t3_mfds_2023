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

def signup(request):

    if request.method == 'GET':
        return render(request, 'Inicio/login.html', {
            'form': UserRegisterForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registro de usuario
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('eventos')
            except IntegrityError:
                return render(request, 'Inicio/login.html', {
                    'form': UserRegisterForm,
                    "error": 'Usuario ya existe'
                })

        return render(request, 'Inicio/login.html', {
            'form': UserRegisterForm,
            "error": 'Contraseñas no coinciden'
        })
 
def CS(request):
    logout(request)
    return redirect('home')

def IS(request):
    if request.method == 'GET':
        return render (request, 'Inicio/signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'Inicio/signin.html',{
                'form': AuthenticationForm,
                'error': 'Usario o contraseña incorrecto'
            })
        else:
            login(request, user)
            return redirect ('eventos')
         


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





