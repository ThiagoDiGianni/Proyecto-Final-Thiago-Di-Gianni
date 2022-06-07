from django.urls import path
from .views import *
from Apps import views

urlpatterns = [
    
    path('', inicio ),
    path('blog',blog),
    path('formulario', views.usuario_formulario, name="Formulario"),
    path('ejemplo',padre),
    path('usuarios_info',views.mostrar_usuario),
    path('eliminar_usuario/<nombre>',views.eliminar_usuario, name="eliminar_usuario"),
    path('editar_usuario/<nombre>',views.editar_usuario, name="editar_usuario"),
    path('login',views.login_request,name="login")




 ]