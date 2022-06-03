from django.urls import path
from .views import *
from Apps import views

urlpatterns = [
    
    path('', inicio ),
    path('formulario', views.usuario_formulario, name="Formulario"),
    path('ejemplo',padre)
    




 ]