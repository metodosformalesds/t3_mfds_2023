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
    eventos = Evento.objects.all()
    return render (request,'Comprador/Eventos.html',{'eventos':eventos})

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
def OrganizadorRegister(request):
    if request.method == 'POST':
        form = OrganizadorForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data['usuario']
            messages.success(request, f'usario{usuario} creado')
            return redirect('Home')
    else:
        form = OrganizadorForm()

    context = { 'form':form }
    return render (request,'Inicio/Login_Organizador.html',context)

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
