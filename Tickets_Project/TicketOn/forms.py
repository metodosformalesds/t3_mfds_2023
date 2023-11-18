from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *
from django.forms.widgets import PasswordInput, TextInput


class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class OrganizadorForm(ModelForm):
    class Meta:

        model = Organizador
        fields = ['empresa']

class EventosForm(ModelForm):
    imagen_actual = forms.ImageField(required=False, label='Imagen Actual', disabled=True)
    class Meta:

        model = Evento
        fields = ['nombre', 'descripcion', 'lugar', 'fecha', 'hora', 'tipo', 'cupo', 'precio', 'imagen'] 
        widgets = {
            'imagen': forms.ClearableFileInput(),
        }     
        

