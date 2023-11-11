from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .forms import UserRegisterForm

# Create your views here.


def Home(request):
    return render(request, 'Home.html')


def index(request):
    return HttpResponse("Welcome to my website")


def signup(request):

    if request.method == 'GET':
        return render(request, 'login.html', {
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
                return render(request, 'login.html', {
                    'form': UserRegisterForm,
                    "error": 'Usuario ya existe'
                })

        return render(request, 'login.html', {
            'form': UserRegisterForm,
            "error": 'Contraseñas no coinciden'
        })

def eventos(request):
    return render (request,'Eventos.html')

def CS(request):
    logout(request)
    return redirect('home')

def IS(request):
    if request.method == 'GET':
        return render (request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'signin.html',{
                'form': AuthenticationForm,
                'error': 'Usario o contraseña incorrecto'
            })
        else:
            login(request, user)
            return redirect ('eventos')
        
def detalles_evento(request,nombre_evento,evento_slug):
    return render(request,'Detalles_Evento.html')