from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import *
from .views import *
from .forms import *

#--------------------------------------------------------------------------------------------------
@login_required
def inicio(request):
    
    avatar = Avatar.objects.filter(user=request.user)
    return render(request, "Apps/template1.html",{'url':avatar[0].avatar.url})

#--------------------------------------------------------------------------------------------------
@login_required
def mi_usuario(request):
    
    avatar = Avatar.objects.filter(user=request.user)
    return render(request, "Apps/mi_usuario.html",{'url':avatar[0].avatar.url})    

#--------------------------------------------------------------------------------------------------

def padre(request):
    
    return render(request, "Apps/template_padre.html")    
#--------------------------------------------------------------------------------------------------
@login_required
def blog(request):
    
    return render(request, "Apps/Template_blog.html")    
#--------------------------------------------------------------------------------------------------
@login_required
def mostrar_usuario(request):

      user = usuario.objects.all() 

      contexto = {"user":user} 

      return render(request, "Apps/mostrar_usuario.html",contexto) 
#--------------------------------------------------------------------------------------------------
@login_required
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
#--------------------------------------------------------------------------------------------------   
@login_required
def eliminar_usuario(request,nombre):

      usuarios = usuario.objects.get(nombre = nombre)
      usuarios.delete()

      user = usuario.objects.all() 
      contexto= {"user":user} 

      return render(request, "Apps/mostrar_usuario.html",contexto)
#--------------------------------------------------------------------------------------------------
@login_required
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

            return render(request,'Apps/mostrar_usuario.html',contexto)

    else:

        formulario = usuarios(initial={'nombre': usuario.nombre, 'apellido':usuario.apellido , 
        'email':usuario.email}) 

        return render(request, 'Apps/editar_usuario.html', {'formulario':formulario,'nombre':nombre})
#--------------------------------------------------------------------------------------------------

    
def login_request(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request=request,data=request.POST)
        
        if formulario.is_valid():
            usuario1 = formulario.cleaned_data.get('username')
            clave = formulario.cleaned_data.get('password')
            user = authenticate(username=usuario1,password=clave)
            
            if user is not None:
                login(request,user)
                return render(request, 'Apps/login_exitoso.html')
            
            else:
                return render(request,'Apps/login_error.html')
        
        else:           
            return render(request,'Apps/login_error.html')
    
    else:
       formulario = AuthenticationForm()
       return render(request, 'Apps/Template_login.html',{'formulario':formulario})
#--------------------------------------------------------------------------------------------------

def register(request):
    
    if request.method == 'POST':
        formulario = UserRegistrationForm(request.POST)

        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            formulario.save()
            return render(request,'Apps/registro_exitoso.html')
        
        else:
            return render(request,'Apps/registro_error.html') 
    
    else:
         formulario = UserRegistrationForm()
         return render(request,'Apps/Template_register.html',{'formulario':formulario})   
#--------------------------------------------------------------------------------------------------

@login_required
def editar_superuser(request):

      superuser = request.user
     
      if request.method == 'POST':
            mi_formulario = UserEditForm(request.POST, instance=superuser) 
            
            if mi_formulario.is_valid():   

                  informacion = mi_formulario.cleaned_data
                              
                  superuser.email = informacion['email']
                  superuser.password1 = informacion['password1']
                  superuser.password2 = informacion['password2']
                  superuser.save()

                  return render(request, "Apps/edicion_exitoso.html")    
      
      else:             
            mi_formulario = UserEditForm(instance=superuser) 
      
      return render(request, "Apps/editar_superuser.html", {"formulario":mi_formulario,'superuser':superuser.username})         

#--------------------------------------------------------------------------------------------------
@login_required
def agregar_avatar(request):
    
    user = User.objects.get(username=request.user)

    if request.method == 'POST':

        formulario = Avatar_formulario(request.POST, request.FILES)

        if formulario.is_valid():
            

            avatar = Avatar(user=user,avatar=formulario.cleaned_data['avatar'])
            avatar.save()
            
            return render(request,'Apps/avatar_exitoso.html')

    else:

        formulario = Avatar_formulario()
    return render(request,'Apps/agregar_avatar.html', {'formulario':formulario, 'usuario':user})            

#--------------------------------------------------------------------------------------------------
@login_required
def editar_avatar(request):
    
    user = User.objects.get(username=request.user)

    if request.method == 'POST':

        formulario = Avatar_formulario(request.POST, request.FILES)

        if formulario.is_valid():
            
            avatar_viejo = Avatar.objects.get(user=request.user)
            
            if(avatar_viejo.avatar):
                avatar_viejo.delete()

            avatar = Avatar(user=user,avatar=formulario.cleaned_data['avatar'])
            avatar.save()
            
            return render(request,'Apps/avatar_exitoso.html')

    else:

        formulario = Avatar_formulario()
    return render(request,'Apps/agregar_avatar.html', {'formulario':formulario, 'usuario':user})         