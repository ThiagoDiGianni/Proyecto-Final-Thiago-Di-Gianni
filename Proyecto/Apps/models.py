from django.db import models

class usuario(models.Model):   
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
   
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}, Email: {self.email}"
   
    
    