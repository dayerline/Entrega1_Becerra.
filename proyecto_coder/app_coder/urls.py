from django.urls import path
from . import views

urlpatterns = [
    path('cursos', views.cursos),
    path('alta_curso/<nombre>', views.alta_curso),
    path('Alumnos', views.alumnos),
    path('alta_alumno/<nombre>/<apellido>', views.alta_alumno),
    path('Profesores', views.profesores),
    path('alta_profesor/<nombre>/<apellido>/<profesion>', views.alta_profesor),
]