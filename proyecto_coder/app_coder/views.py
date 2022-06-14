from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso, Alumno, Profesor
from django.template import loader
# Create your views here.

def cursos(request):
    cursos= Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("plantilla.html")
    documento= plantilla.render(dicc)
    return HttpResponse( documento)


def alumnos(request):
    alumnos= Alumno.objects.all()
    dicc = {"alumnos": alumnos}
    plantilla = loader.get_template("alumno.html")
    documento= plantilla.render(dicc)
    return HttpResponse( documento)


def profesores(request):
    profesores= Profesor.objects.all()
    dicc = {"profesores": profesores}
    plantilla= loader.get_template("profesor.html")
    documento= plantilla.render(dicc)
    return HttpResponse ( documento)


def alta_curso(request, nombre):
    curso= Curso(nombre= nombre, camada=23454)
    curso.save()
    texto=f"Se guardo en la BD el Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse ( texto )


def alta_alumno(request, nombre, apellido):
    alumno= Alumno(nombre= nombre, apellido= apellido)
    alumno.save()
    texto= f"Se guardo en la BD el Alumno: {alumno.nombre} Apellido {alumno.apellido}"
    return HttpResponse ( texto )


def alta_profesor(request, nombre, apellido, profesion):
    profesor= Profesor(nombre= nombre, apellido= apellido, profesion= profesion)
    profesor.save()
    texto= f"Se guardo en la BD el Profesor: {profesor.nombre} Apellido: {profesor.apellido} Profesion: {profesor.profesion}"
    return HttpResponse (texto)