from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify




class Comprador(models.Model):
    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    correo=models.CharField(max_length=30,blank=True)
    
    cvv=models.CharField(max_length=4,null=True)
    num_tarjeta=models.CharField(max_length=16,null=True)
    fecha_venc=models.DateField(null=True)
    nombre_titular=models.CharField(max_length=100,null=True)
    

    def __str__(self):
        return f"{self.usuario}"

class Organizador(models.Model):
    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    correo=models.CharField(max_length=30,blank=True)
    empresa=models.CharField(max_length=30,blank=True)

    cuenta_clabe=models.CharField(max_length=18,null=True)
    def __str__(self):
        return f"{self.usuario}"

class Evento(models.Model):
    lugar=models.CharField(max_length=100,blank=True)
    hora=models.TimeField(blank=True)
    fecha=models.DateField()
    nombre=models.CharField(max_length=100)
    cupo=models.IntegerField()
    imagen=models.ImageField(upload_to="eventos",blank=True,null=True)
    descripcion=models.TextField(max_length=1000)
    tipo= models.CharField(max_length=20)
    organizador=models.ForeignKey(Organizador,on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='nombre', unique=True, always_update=True)
    precio=models.FloatField(null=True)
    en_curso = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
    

class Ticket(models.Model):
    precio = models.FloatField()
    estado = models.BooleanField(default=False)
    codigo = models.CharField(max_length=30, unique=True)
    fecha_compra = models.DateField(null=True, blank=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    comprador = models.ForeignKey(Comprador, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.codigo}"

class Transferencia(models.Model):
    fecha=models.DateField()
    monto_final=models.FloatField()
    estado=models.BooleanField(default=False)
    ticket=models.ForeignKey(Ticket,on_delete=models.CASCADE)
    organizador=models.ForeignKey(Organizador,on_delete=models.CASCADE)
    comprador=models.ForeignKey(Comprador,on_delete=models.CASCADE)

    
class Carrito(models.Model):
    comprador=models.ForeignKey(Comprador,on_delete=models.CASCADE)
    tickets = models.ManyToManyField(Ticket, related_name='tickets_en_carrito')

    def __str__(self):
        return f"Carrito de {self.comprador}"
