from django.shortcuts import render
from django.http import HttpResponse

from .models import *


from .views import *
from .forms import *

def inicio(request):
    
    return render(request, "Apps/template1.html")

def padre(request):
    
    return render(request, "Apps/template_padre.html")    

def usuario_formulario(request):
    
    if request.method == 'POST':

        mi_formulario = usuarios(request.POST)        

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            Usuario = usuario (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            
            Usuario.save()
            
            return render(request, 'Apps/template1.html')

    else:
        mi_formulario=usuarios()
    return render(request, 'Apps/herencia_formulario.html', {'formulario':mi_formulario})      
    

