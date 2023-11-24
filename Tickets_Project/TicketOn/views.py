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
import random
import string
from copy import deepcopy
from datetime import date
from django.contrib import messages

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
        tipo_busq = request.POST["tipo"]
        lugar_busq = request.POST["lugar"]
        fecha_busq = request.POST["fecha"]
        
        if not fecha_busq:
            eventos = Evento.objects.filter(nombre__contains = nombre_busq,tipo__contains = tipo_busq, lugar__contains = lugar_busq)
            
        else:
            eventos = Evento.objects.filter(nombre__contains = nombre_busq,tipo__contains = tipo_busq, lugar__contains = lugar_busq,fecha = fecha_busq)
        
        return render (request,'Comprador/Eventos.html',{
            'eventos':eventos,
            'nombre_busq': nombre_busq,
            'tipo_busq': tipo_busq,
            'fecha_busq': fecha_busq,
            'lugar_busq':lugar_busq
        })
    
    
    

@comprador_required
def ayuda(request):
    return render (request,'Comprador/Ayuda.html')

@comprador_required
def carrito(request):
    # Obtener el carrito del comprador actual
    comprador_actual = Comprador.objects.get(usuario=request.user)
    carrito, creado = Carrito.objects.get_or_create(comprador=comprador_actual)

    # Obtener todos los tickets en el carrito
    tickets_en_carrito = carrito.tickets.all()
    montofinal = sum(ticket.precio for ticket in tickets_en_carrito)
    

    return render(request, 'Comprador/Carrito.html', {'tickets_en_carrito': tickets_en_carrito, 'montofinal': montofinal})

@comprador_required
def detalles_evento(request,nombre_evento,evento_slug):
    evento= Evento.objects.get(slug=evento_slug)
    return render(request,'Comprador/Detalles_Evento.html',{
        "evento":evento
    })



#Organizador
@Organizador_required
def Eventos_en_curso(request):
    organizador = get_object_or_404(Organizador, usuario=request.user)
    eventos_en_curso = Evento.objects.filter(organizador=organizador,en_curso=True)
    return render(request, 'Organizador/Eventos_en_curso.html', {'eventos_en_curso': eventos_en_curso})

@Organizador_required
def Creacion_de_eventos(request):
    evento_form = EventosForm()

    if request.method == "POST":
        evento_form = EventosForm(request.POST, request.FILES)

        if evento_form.is_valid():
            organizador = Organizador.objects.get(usuario=request.user)
            
            nuevo_evento = evento_form.save(commit=False)
            
            nuevo_evento.organizador = organizador

            nuevo_evento.save()

            return redirect("TicketOn:eventos_en_curso")

    context = {'Evento_form': evento_form}
    return render(request, 'Organizador/Creacion_de_eventos.html', context=context)

@Organizador_required
def Ventas(request):
    return render(request, 'Organizador/Ventas.html')


@Organizador_required
def editar_evento(request, evento_slug):
    evento = get_object_or_404(Evento, slug=evento_slug)

    if request.user != evento.organizador.usuario:
        return redirect("TicketOn:eventos_en_curso")

    if request.method == 'POST':
        if 'eliminar_evento' in request.POST:
            evento.delete()
            return redirect("TicketOn:eventos_en_curso")

        evento_form = EventosForm(request.POST, request.FILES, instance=evento)
        if evento_form.is_valid():
            evento_form.save()
            return redirect("TicketOn:eventos_en_curso")
    else:
        evento_form = EventosForm(instance=evento)

    return render(request, 'Organizador/Editar_eventos.html', {'Evento_form': evento_form, 'evento': evento})

def eliminar_evento(request, evento_slug):
    evento = get_object_or_404(Evento, slug=evento_slug)

    if request.method == 'POST' and 'eliminar_evento' in request.POST:
        evento.delete()
        return redirect("TicketOn:eventos_en_curso")

    return render(request, 'ruta_a_tu_plantilla_eliminar_evento.html', {'evento': evento})

#Sistema logico de tickets
def generar_codigo():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


#Sistema de pagos
def agregar_al_carrito(request, evento_slug):
    evento = get_object_or_404(Evento, slug=evento_slug)

    if request.method == 'POST':
        cantidad = request.POST.get('cant_tickets', 1)

        try:
            cantidad = int(cantidad)
            comprador_actual = Comprador.objects.get(usuario=request.user)

            carrito, creado = Carrito.objects.get_or_create(comprador=comprador_actual)

            for _ in range(cantidad):
                codigo_ticket = generar_codigo()

                while Ticket.objects.filter(codigo=codigo_ticket).exists():
                    codigo_ticket = generar_codigo()

                nuevo_ticket = Ticket.objects.create(
                    precio=evento.precio,
                    estado=False,
                    codigo=codigo_ticket,
                    fecha_compra=None,
                    evento=evento,
                    comprador=comprador_actual
                )

                carrito.tickets.add(nuevo_ticket)

            messages.success(request, f'Boleto(s) agregado(s) al carrito exitosamente.')
        except ValueError as e:
            messages.error(request, str(e))

    return redirect('TicketOn:carrito') 

def quitar_del_carrito(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == 'POST':
        comprador_actual = get_object_or_404(Comprador, usuario=request.user)
        carrito = get_object_or_404(Carrito, comprador=comprador_actual)

        carrito.tickets.remove(ticket)

        ticket.delete()

        messages.success(request, 'Boleto quitado del carrito exitosamente.')

    return redirect('TicketOn:carrito')

def limpiar_carrito(request):
    comprador_actual = Comprador.objects.get(usuario=request.user)
    carrito, creado = Carrito.objects.get_or_create(comprador=comprador_actual)

    # Eliminar los tickets del carrito de la base de datos
    for ticket in carrito.tickets.all():
        ticket.delete()

    messages.success(request, 'Carrito limpiado exitosamente.')

    return redirect('TicketOn:carrito')

def pago_contarjeta(request):
    # Obtener el carrito del comprador actual
    comprador_actual = Comprador.objects.get(usuario=request.user)
    carrito, creado = Carrito.objects.get_or_create(comprador=comprador_actual)

    # Obtener todos los tickets en el carrito
    tickets_en_carrito = carrito.tickets.all()
    montofinal = sum(ticket.precio for ticket in tickets_en_carrito)

    return render(request, 'Comprador/Pago_tarjeta.html', {'tickets_en_carrito': tickets_en_carrito, 'montofinal': montofinal})