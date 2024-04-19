from django.shortcuts import render, redirect, get_object_or_404
from AppCoder.models import Curso, Profesor, Alumno, Avatar
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from AppCoder.forms import Curso_formulario, Profesor_formulario, Alumno_formulario, UserEditForm
from django.db.models import Q

def inicio(request):
    return render(request, "padre.html")

def alta_curso(request, nombre):
    curso = Curso(nombre=nombre, camada=234512)
    curso.save()
    texto = f"Se guardó en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)

@login_required
def ver_cursos(request):
    cursos = Curso.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    avatar_url = avatares[0].imagen.url if avatares.exists() else None
    return render(request, "cursos.html", {"url": avatar_url, "cursos": cursos})

def elimina_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    cursos = Curso.objects.all()
    return render(request, "cursos.html", {"cursos": cursos})

def editar(request, id):
    curso = Curso.objects.get(id=id)

    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST, instance=curso)
        if mi_formulario.is_valid():
            mi_formulario.save()
            cursos = Curso.objects.all()
            return render(request, "cursos.html", {"cursos": cursos})
    else:
        mi_formulario = Curso_formulario(instance=curso)
    
    return render(request, "editar_curso.html", {"mi_formulario": mi_formulario, "curso": curso})

def buscar_curso(request):
    return render(request, "buscar_curso.html")

def alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumnos.html', {'alumnos': alumnos})

def alta_alumnos(request):
    if request.method == 'POST':
        form = Alumno_formulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumnos')
    else:
        form = Alumno_formulario()
    return render(request, 'alta_alumnos.html', {'form': form})

def editar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        form = Alumno_formulario(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('alumnos')
    else:
        form = Alumno_formulario(instance=alumno)
    return render(request, 'editar_alumno.html', {'form': form})

def eliminar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    if request.method == 'POST':
        alumno.delete()
        return redirect('alumnos')
    return render(request, 'confirmar_eliminar_alumno.html', {'alumno': alumno})

def alta_profesores(request):
    if request.method == 'POST':
        form = Profesor_formulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Profesor_formulario()
    return render(request, 'alta_profesores.html', {'form': form})

def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesores.html', {'profesores': profesores})

def editar_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        form = Profesor_formulario(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('profesores')
    else:
        form = Profesor_formulario(instance=profesor)
    return render(request, 'editar_profesor.html', {'form': form})

def eliminar_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    if request.method == 'POST':
        profesor.delete()
        return redirect('profesores')
    return render(request, 'confirmar_eliminar_profesor.html', {'profesor': profesor})

def curso_formulario(request):
    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            mi_formulario.save()
            return render(request, "formulario.html")
    return render(request, "formulario.html")

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

            filtro_alumnos = Q()

            if nombre_alumno:
                filtro_alumnos &= Q(nombre__icontains=nombre_alumno)

            if edad:
                filtro_alumnos &= Q(edad=edad)

            alumnos = Alumno.objects.filter(filtro_alumnos)

            return render(request, "resultado_busqueda.html", {"alumnos": alumnos})

        elif tipo == "profesor":
            nombre_profesor = request.GET.get("nombre_profesor", "")
            especialidad = request.GET.get("especialidad", "")

            filtro_profesores = Q()

            if nombre_profesor:
                filtro_profesores &= Q(nombre__icontains=nombre_profesor)

            if especialidad:
                filtro_profesores &= Q(especialidad__icontains=especialidad)

            profesores = Profesor.objects.filter(filtro_profesores)

            return render(request, "resultado_busqueda.html", {"profesores": profesores})

    return HttpResponse("Error en la búsqueda")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario , password=contra)
            if user is not None:
                login(request , user )
                avatares = Avatar.objects.filter(user=request.user.id)
                if avatares.exists():
                    return render(request, "inicio.html", {"url": avatares[0].imagen.url})
                else:
                    return render(request, "inicio.html")
            else:
                return HttpResponse(f"Usuario no encontrado")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")
    else:
        form = UserCreationForm()
    return render(request , "registro.html" , {"form":form})

def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request , "inicio.html")
    else:
        miFormulario = UserEditForm(initial={"email":usuario.email})
    return render( request , "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})
