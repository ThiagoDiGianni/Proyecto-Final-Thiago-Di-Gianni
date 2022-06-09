from django.urls import path
from .views import *
from Apps import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('', inicio ),
    path('blog',blog),
    path('ejemplo',padre),

    path('formulario', views.usuario_formulario, name="Formulario"),   
    path('usuarios_info',views.mostrar_usuario,name="usuarios_info"),
    path('eliminar_usuario/<nombre>',views.eliminar_usuario, name="eliminar_usuario"),
    path('editar_usuario/<nombre>',views.editar_usuario, name="editar_usuario"),
    
    path('login',views.login_request,name="login"),
    path('register',views.register,name="register"),
    path('logout',LogoutView.as_view(template_name="Apps/logout.html"),name='logout'),

    path('editar_superuser',views.editar_superuser,name="editar_superuser")



 ]