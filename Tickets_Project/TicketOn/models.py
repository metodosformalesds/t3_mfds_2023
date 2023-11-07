from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comprador(models.Model):
    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    correo=models.CharField(max_length=30)
    
    cvv=models.CharField(max_length=4)
    num_tarjeta=models.CharField(max_length=16)
    fecha_venc=models.DateField()
    nombre_titular=models.CharField(max_length=100)

class Organizador(models.Model):
    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    correo=models.CharField(max_length=30)
    empresa=models.CharField(max_length=30)

    cuenta_clabe=models.CharField(max_length=18)

class Evento(models.Model):
    lugar=models.CharField(max_length=100)
    hora=models.TimeField()
    fecha=models.DateField()
    nombre=models.CharField(max_length=100)
    cupo=models.IntegerField()
    imagen=models.ImageField(upload_to="eventos")
    descripcion=models.TextField(max_length=1000)
    TIPOS=[("1","Deportivo")]
    tipo= models.CharField(max_length=2)
    organizador=models.ForeignKey(Organizador,on_delete=models.CASCADE)

class Ticket(models.Model):
    precio=models.FloatField()
    estado=models.BooleanField(default=False)
    codigo=models.CharField(max_length=30)
    fecha_compra=models.DateField()
    evento=models.ForeignKey(Evento,on_delete=models.CASCADE)
    comprador=models.ForeignKey(Comprador,on_delete=models.CASCADE)

class Transferencia(models.Model):
    fecha=models.DateField()
    monto_final=models.FloatField()
    estado=models.BooleanField(default=False)
    ticket=models.ForeignKey(Ticket,on_delete=models.CASCADE)
    organizador=models.ForeignKey(Organizador,on_delete=models.CASCADE)
    comprador=models.ForeignKey(Comprador,on_delete=models.CASCADE)

