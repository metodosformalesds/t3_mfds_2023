from django.db import models
from django.contrib.auth.models import User

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
    imagen=models.ImageField(upload_to="eventos",blank=True)
    descripcion=models.TextField(max_length=1000)
    tipo= models.CharField(max_length=20)
    organizador=models.ForeignKey(Organizador,on_delete=models.CASCADE)
    slug=models.SlugField(blank=True)
    precio=models.FloatField(null=True)

    def __str__(self):
        return f"{self.nombre}"
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        self.slug = self.id
        super().save(*args,**kwargs)
    

class Ticket(models.Model):
    precio=models.FloatField()
    estado=models.BooleanField(default=False)
    codigo=models.CharField(max_length=30)
    fecha_compra=models.DateField()
    evento=models.ForeignKey(Evento,on_delete=models.CASCADE)
    comprador=models.ForeignKey(Comprador,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.codigo}"

class Transferencia(models.Model):
    fecha=models.DateField()
    monto_final=models.FloatField()
    estado=models.BooleanField(default=False)
    ticket=models.ForeignKey(Ticket,on_delete=models.CASCADE)
    organizador=models.ForeignKey(Organizador,on_delete=models.CASCADE)
    comprador=models.ForeignKey(Comprador,on_delete=models.CASCADE)

    

