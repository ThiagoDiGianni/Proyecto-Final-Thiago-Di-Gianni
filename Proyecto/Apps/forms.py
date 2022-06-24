
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#--------------------------------------------------------------------------------------------------    

class usuarios(forms.Form):   
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
#--------------------------------------------------------------------------------------------------    

class UserRegistrationForm(UserCreationForm):
    
    email = forms.EmailField(required=True)    
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña",widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        help_texts = {k:"" for k in fields}
#--------------------------------------------------------------------------------------------------   

class UserEditForm(UserCreationForm):
    
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label="Modificar Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña",widget=forms.PasswordInput)

    
    class Meta:
        model = User
        fields = ( 'password1','password2','email')
        help_texts = {k:"" for k in fields}

#--------------------------------------------------------------------------------------------------   

class Avatar_formulario(forms.Form):

    avatar = forms.ImageField(label="Avatar")        