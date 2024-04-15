from django.shortcuts import render, redirect
from AppCoder.models import Curso, Profesor, Alumno
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from AppCoder.forms import Curso_formulario, Profesor_formulario, Alumno_formulario

# Create your views here.

def inicio(request):
    return render(request, "padre.html")

def alta_curso(request, nombre):
    curso = Curso(nombre=nombre, camada=234512)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)

def alta_profesores(request):
    if request.method == 'POST':
        form = Profesor_formulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            especialidad = form.cleaned_data['especialidad']
            Profesor.objects.create(nombre=nombre, especialidad=especialidad)
            return redirect('home')
    else:
        form = Profesor_formulario()
    return render(request, 'alta_profesores.html', {'form': form})

def alta_alumnos(request):
    if request.method == 'POST':
        form = Alumno_formulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            edad = form.cleaned_data['edad']
            Alumno.objects.create(nombre=nombre, edad=edad)
            return redirect('alumnos')
    else:
        form = Alumno_formulario()
    return render(request, 'alta_alumnos.html', {'form': form})

def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos.html', {'alumnos': alumnos})

def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesores.html', {'profesores': profesores})

def curso_formulario(request):
    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso(nombre=datos["nombre"], camada=datos["camada"])
            curso.save()
            return render(request, "formulario.html")
    return render(request, "formulario.html")

def buscar_curso(request):
    return render(request, "buscar_curso.html")


def buscar(request):
    return render(request, 'buscar.html')


def buscar(request):
    if request.method == "GET":
        nombre = request.GET.get("nombre", "")
        tipo = request.GET.get("tipo", "")

        elementos = []
        if tipo == "curso":
            elementos = Curso.objects.filter(nombre__icontains=nombre)
        elif tipo == "alumno":
            elementos = Alumno.objects.filter(nombre__icontains=nombre)
        elif tipo == "profesor":
            elementos = Profesor.objects.filter(nombre__icontains=nombre)

        return render(request, "buscar.html", {"elementos": elementos, "tipo": tipo, "nombre": nombre})
    return HttpResponse("Ingrese el nombre y tipo de búsqueda")

def resultado_busqueda(request):
    if request.method == "GET":
        tipo = request.GET.get("tipo", "")

        if tipo == "curso":
            nombre_curso = request.GET.get("nombre_curso", "")
            camada = request.GET.get("camada", "")

            cursos = Curso.objects.filter(Q(nombre__icontains=nombre_curso) | Q(camada__icontains=camada))

            return render(request, "resultado_busqueda.html", {"cursos": cursos})

        elif tipo == "alumno":
            nombre_alumno = request.GET.get("nombre_alumno", "")
            edad = request.GET.get("edad", "")

            # Crear un filtro vacío para alumnos
            filtro_alumnos = Q()

            # Si se proporciona un nombre de alumno, agregar al filtro
            if nombre_alumno:
                filtro_alumnos &= Q(nombre__icontains=nombre_alumno)

            # Si se proporciona una edad, agregar al filtro
            if edad:
                filtro_alumnos &= Q(edad=edad)

            alumnos = Alumno.objects.filter(filtro_alumnos)

            return render(request, "resultado_busqueda.html", {"alumnos": alumnos})

        elif tipo == "profesor":
            nombre_profesor = request.GET.get("nombre_profesor", "")
            especialidad = request.GET.get("especialidad", "")

            # Crear un filtro vacío para profesores
            filtro_profesores = Q()

            # Si se proporciona un nombre de profesor, agregar al filtro
            if nombre_profesor:
                filtro_profesores &= Q(nombre__icontains=nombre_profesor)

            # Si se proporciona una especialidad, agregar al filtro
            if especialidad:
                filtro_profesores &= Q(especialidad__icontains=especialidad)

            profesores = Profesor.objects.filter(filtro_profesores)

            return render(request, "resultado_busqueda.html", {"profesores": profesores})

    return HttpResponse("Error en la búsqueda")