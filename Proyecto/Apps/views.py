from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .views import *
from .forms import *

def inicio(request):
    
    return render(request, "Apps/template1.html")


def padre(request):
    
    return render(request, "Apps/template_padre.html")    


def mostrar_usuario(request):

      user = usuario.objects.all() 

      contexto = {"user":user} 

      return render(request, "Apps/mostrar_usuario.html",contexto) 


def usuario_formulario(request):
    
    if request.method == 'POST':

        mi_formulario = usuarios(request.POST)        

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            Usuario = usuario (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            
            Usuario.save()
            
            return render(request, 'Apps/template1.html')

    else:
        mi_formulario = usuarios()
    return render(request, 'Apps/herencia_formulario.html', {'formulario':mi_formulario})      
    

def eliminar_usuario(request,nombre):

      usuarios = usuario.objects.get(nombre = nombre)
      usuarios.delete()

      user = usuario.objects.all() 
      contexto= {"user":user} 

      return render(request, "Apps/mostrar_usuario.html",contexto)


def editar_usuario(request,nombre):

    Usuario = usuario.objects.get( nombre = nombre )

    if request.method == 'POST':

        formulario = usuarios(request.POST)
        
        if formulario.is_valid():

            informacion = formulario.cleaned_data
            Usuario.nombre = informacion['nombre']
            Usuario.apellido = informacion['apellido']
            Usuario.email = informacion['email']
            Usuario.save()
            #---------------
            user = usuario.objects.all()
            contexto = {'user':user}

            return render(request,"Apps/mostrar_usuario.html",contexto)

    else:

         formulario = usuarios(initial={'nombre': usuario.nombre, 'apellido':usuario.apellido , 
        'email':usuario.email}) 

         return render(request, 'Apps/editar_usuario.html', {'formulario':formulario,'nombre':nombre})


    
