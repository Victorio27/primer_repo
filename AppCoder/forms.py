from django import forms
from .models import Curso, Profesor, Alumno

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