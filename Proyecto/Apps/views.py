from django.shortcuts import render
from django.http import HttpResponse
from .views import *

def inicio(request):
    
    return render(request, "Apps/template1.html")

def formulario(request):
    
    return render(request, "Apps/herencia_formulario.html")    