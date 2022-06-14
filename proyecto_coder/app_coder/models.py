from operator import length_hint
from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre= models.CharField(max_length=40)
    camada= models.IntegerField()

class Alumno(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=30)

class Profesor(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=30)
    profesion= models.CharField(max_length=30)
    