from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio , name="home"),
    path("ver_cursos", views.ver_cursos , name="cursos"),
    #path("alta_curso/<nombre>", views.alta_curso),
    path("alumnos", views.alumnos , name="alumnos"),
    path("alta_alumnos/", views.alta_alumnos, name="alta_alumnos"),
    path("alumnos/<int:pk>/editar/", views.editar_alumno, name="editar_alumno"),
    path("alumnos/<int:pk>/eliminar/", views.eliminar_alumno, name="eliminar_alumno"),
    path("alta_curso", views.curso_formulario),
    path("buscar_curso", views.buscar_curso),
    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("editar_curso/<int:id>" , views.editar , name="editar_curso"),
    path("buscar", views.buscar, name='buscar'),
    path("alta_profesores/", views.alta_profesores, name="alta_profesores"),
    path("profesores/<int:pk>/editar/", views.editar_profesor, name="editar_profesor"),
    path('profesores/', views.profesores, name='profesores'),
    path("profesores/<int:pk>/eliminar/", views.eliminar_profesor, name="confirmar_eliminar_profesor"),
    path('resultado_busqueda/', views.resultado_busqueda, name='resultado_busqueda'),
    path("login", views.login_request , name="Login"),
    path("register", views.register , name="Register"),
    path("logout" , LogoutView.as_view (template_name="logout.html") , name="Logout"),
    path("editarPerfil" , views.editarPerfil , name="EditarPerfil")
]