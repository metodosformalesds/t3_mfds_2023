from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Evento, Organizador , Comprador

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'descripcion', 'tipo','hora','lugar','fecha','precio']

class OrganizadorForm(ModelForm):
    class Meta:
        model = Organizador
        fields = ['usuario', 'correo', 'empresa', 'cuenta_clabe']
