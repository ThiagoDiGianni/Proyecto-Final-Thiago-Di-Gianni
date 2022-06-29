from django.urls import path
from .views import *
from Apps import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('',views.inicio,name="inicio" ),
    path('sobre_mi',sobre_mi),
    path('prueba',views.registro_pruebas,name="prueba"),

    path('formulario', views.usuario_formulario, name="Formulario"),   
    path('usuarios_info',views.mostrar_usuario,name="usuarios_info"),
    path('eliminar_usuario/<nombre>',views.eliminar_usuario, name="eliminar_usuario"),
    path('editar_usuario/<nombre>',views.editar_usuario, name="editar_usuario"),
    
    path('login',views.login_request,name="login"),
    path('register',views.register,name="register"),
    path('logout',LogoutView.as_view(template_name="Apps/logout.html"),name='logout'),

    path('editar_superuser',views.editar_superuser,name="editar_superuser"),
    path('agregar_avatar',views.agregar_avatar ,name='agregar_avatar'),
    path('editar_avatar',views.editar_avatar ,name='editar_avatar'),
    path('mi_usuario',views.mi_usuario, name='mi_usuario'),

    path('crear_blog',views.blog_formulario, name='blog_formulario'),
    path('mostrar_blog',views.mostrar_blog, name='mostrar_blog'),
    path('eliminar_blog/<titulo>',views.eliminar_blog, name="eliminar_blog"),

    path('mostrar_mensaje',views.mostrar_mensaje, name='mostrar_mensaje'),
    path('formulario_mensaje',views.formulario_mensaje, name='formulario_mensaje'),



 ]