from django.db import models
from django.contrib.auth.models import User

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
    
    