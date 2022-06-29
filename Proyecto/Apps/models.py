#from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class usuario(models.Model):   
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
   
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}, Email: {self.email}"
#-------------------------------------------------------------------------------------------------- 
 
class Avatar(models.Model):

     user = models.ForeignKey(User, on_delete=models.CASCADE)
     avatar = models.ImageField(upload_to='avatar',null=True,blank=True)
    
#--------------------------------------------------------------------------------------------------  

class blog(models.Model):
 
     titulo = models.CharField(max_length=50)
     subtitulo = models.CharField(max_length=50)
     imagen = models.ImageField(upload_to='imagenes')
     fecha = models.DateField(auto_now=False, auto_now_add=True)
     descripcion = models.CharField(max_length=150)
     
#-------------------------------------------------------------------------------------------------- 

class mensajes(models.Model):

    
    mensaje = models.CharField(max_length=100)