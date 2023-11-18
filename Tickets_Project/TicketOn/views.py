from typing import Self
from functools import wraps
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from .models import *
from django.contrib.auth.models import auth
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, login, logout
from allauth.account.decorators import login_required

#Sesión comprador
def register(request):
    auth.logout(request)
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            email = user.email
            Comprador.objects.create(usuario=user,correo=email)
            return redirect("TicketOn:my-login")

    context = {'registerform': form}
    return render(request, 'Inicio/comprador_register.html', context=context)
    
def my_login(request):
    auth.logout(request)
    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("TicketOn:eventos")


    context = {'loginform':form}

    return render(request, 'Inicio/comprador_login.html', context=context)






#Sesión Organizador
def registerOrganizador(request):
    auth.logout(request)
    user_form = CreateUserForm()
    organizador_form = OrganizadorForm()

    if request.method == "POST":
        user_form = CreateUserForm(request.POST)
        organizador_form = OrganizadorForm(request.POST)

        if user_form.is_valid() and organizador_form.is_valid():
            user = user_form.save()
            email = user.email
            empresa = organizador_form.cleaned_data['empresa']
            Organizador.objects.create(usuario=user, correo=email, empresa=empresa)
            return redirect("TicketOn:my_loginO")

    context = {'registerform': user_form, 'OrganizadorForm': organizador_form}
    return render(request, 'Inicio/organizador_register.html', context=context)
    
def my_loginOrganizador(request):
    auth.logout(request)
    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("TicketOn:eventos_en_curso")


    context = {'loginform':form}

    return render(request, 'Inicio/organizador_login.html', context=context)



def user_logout(request):

    auth.logout(request)

    return redirect("/home/")


def comprador_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Verifica si el usuario actual es un comprador
        if request.user.is_authenticated and Comprador.objects.filter(usuario=request.user).exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect("TicketOn:my-login")  # Redirige a la página de inicio de sesión si no es un comprador
    return _wrapped_view

def Organizador_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Verifica si el usuario actual es un comprador
        if request.user.is_authenticated and Organizador.objects.filter(usuario=request.user).exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect("TicketOn:my_loginO")  # Redirige a la página de inicio de sesión si no es un organizador
    return _wrapped_view


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
@comprador_required
def eventos(request):
    if request.method =="GET":
        eventos = Evento.objects.all()
        return render (request,'Comprador/Eventos.html',{
            'eventos':eventos
        })
    else:
        nombre_busq = request.POST["nombre"]
        eventos = Evento.objects.filter(nombre__contains = nombre_busq)
        return render (request,'Comprador/Eventos.html',{
            'eventos':eventos,
            'nombre_busq': nombre_busq
        })
    
    
    

@comprador_required
def ayuda(request):
    return render (request,'Comprador/Ayuda.html')

@comprador_required
def carrito(request):
    return render (request,'Comprador/Carrito.html')

@comprador_required
def detalles_evento(request,nombre_evento,evento_slug):
    evento= Evento.objects.get(slug=evento_slug)
    return render(request,'Comprador/Detalles_Evento.html',{
        "evento":evento
    })



#Organizador
@Organizador_required
def Eventos_en_curso(request):
    return render(request, 'Organizador/Eventos_en_curso.html')

@Organizador_required
def Creacion_de_eventos(request):
    evento_form = EventosForm()
    if request.method == "POST":
        evento_form= EventosForm(request.POST,request.FILES)

        if evento_form.is_valid():
            lugar=evento_form.cleaned_data['lugar']
            hora=evento_form.cleaned_data['hora']
            fecha=evento_form.cleaned_data['fecha']
            nombre=evento_form.cleaned_data['nombre']
            cupo=evento_form.cleaned_data['cupo']
            imagen = evento_form.cleaned_data['imagen']
            descripcion=evento_form.cleaned_data['descripcion']
            tipo=evento_form.cleaned_data['tipo']
            precio=evento_form.cleaned_data['precio']
            organizador = Organizador.objects.get(usuario=request.user)
            Evento.objects.create(lugar=lugar, hora=hora, fecha=fecha, nombre=nombre,cupo=cupo,imagen=imagen, descripcion=descripcion,tipo=tipo,organizador=organizador, precio=precio )
            return redirect("TicketOn:eventos_en_curso")

    context = {'Evento_form': evento_form}
    return render(request, 'Organizador/Creacion_de_eventos.html', context=context)

@Organizador_required
def editar_evento(request, evento_slug):
    evento = get_object_or_404(Evento, slug=evento_slug)

    # Verificar si el usuario actual es el organizador del evento
    if request.user != evento.organizador.usuario:
        return redirect("TicketOn:eventos_en_curso")

    if request.method == 'POST':
        evento_form = EventosForm(request.POST, request.FILES, instance=evento)
        if evento_form.is_valid():
            evento_form.save()
            return redirect("TicketOn:eventos_en_curso")
    else:
        evento_form = EventosForm(instance=evento)

    return render(request, 'Organizador/Editar_eventos.html', {'Evento_form': evento_form, 'evento': evento})

@Organizador_required
def Ventas(request):
    return render(request, 'Organizador/Ventas.html')
