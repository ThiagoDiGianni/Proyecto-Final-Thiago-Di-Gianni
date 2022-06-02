from django.urls import path
from .views import *
from Apps import views

urlpatterns = [
    
    path('', inicio ),
    path('formulario', views.formulario, name="Formulario"),
    




 ]