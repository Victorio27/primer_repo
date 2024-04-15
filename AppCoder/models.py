from django.db import models

# Create your models here.


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()