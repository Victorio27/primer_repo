from django import forms
from .models import Curso, Profesor, Alumno
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Curso_formulario(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'camada']

class Profesor_formulario(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'especialidad']

class Alumno_formulario(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'edad']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña" , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','password1','password2']
        help_text = {k:"" for k in fields}