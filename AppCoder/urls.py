from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio , name="home"),
    path("ver_cursos", views.ver_cursos , name="cursos"),
    #path("alta_curso/<nombre>", views.alta_curso),
    path("alumnos", views.alumnos , name="alumnos"),
    path("alta_curso", views.curso_formulario),
    path("buscar_curso", views.buscar_curso),
    path("buscar", views.buscar, name='buscar'),
    path("alta_profesores/", views.alta_profesores, name="alta_profesores"),
    path("alta_alumnos/", views.alta_alumnos, name="alta_alumnos"),
    path('profesores/', views.profesores, name='profesores'),
    path('resultado_busqueda/', views.resultado_busqueda, name='resultado_busqueda'),
    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("editar_curso/<int:id>" , views.editar , name="editar_curso"),
    path("login", views.login_request , name="Login"),
    path("register", views.register , name="Register")

]