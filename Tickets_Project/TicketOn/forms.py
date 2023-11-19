from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *
from django.forms.widgets import PasswordInput, TextInput


TIPOS_DE_EVENTO = [
    ('concierto', 'Concierto'),
    ('conferencia', 'Conferencia'),
    ('exposicion', 'Exposición'),
    ('festival', 'Festival'),
    ('deportivo', 'Deportivo'),
    ('teatro', 'Teatro'),
    ('social', 'Social'),
    ('networking', 'Networking'),
    ('educativo', 'Educativo'),
    ('recreativo', 'Recreativo'),
    # Agrega más tipos según sea necesario
]

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
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'precio': forms.NumberInput(attrs={'min': '0.00', 'step': '0.01'}),
            'cupo': forms.NumberInput(attrs={'min': '0', 'step': '0'}),
            'tipo': forms.Select(choices=TIPOS_DE_EVENTO),
            'descripcion': forms.Textarea(attrs={'cols': 51, 'rows': 10}), 
        }     
        
