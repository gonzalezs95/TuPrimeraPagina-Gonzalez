from django.shortcuts import render, redirect

from .models import Familiar, Curso, Estudiante, Ropa, Celular

from django.http import HttpResponse

from .forms import CursoForm, EstudianteForm, RopaForm, CelularForm

def inicio(request):
    return render(request, 'mi_primer_app/inicio.html')

def saludo(request):
    return HttpResponse("¡Hola, mundo!")

def saludo_con_template(request):
    return render(request, 'mi_primer_app/saludo.html')

def crear_familiar(request, nombre):
    if nombre is not None:
        #Creamos un nuevo objeto Familiar
        nuevo_familiar = Familiar(
            nombre=nombre,
            apellido="ApellidoEjemplo",
            edad=30,
            Fecha_nacimiento="1993-01-01",
            parentesco="Primo"
        )
        nuevo_familiar.save()
    return render(request, "mi_primer_app/crear_familiar.html", {"nombre": nombre})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            # Procesar el formulario
            nuevo_curso =  Curso(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                duracion_semanas=form.cleaned_data['duracion_semanas'],
                fecha_inicio=form.cleaned_data['fecha_inicio'],
                activo=form.cleaned_data['activo']
            )
            nuevo_curso.save()
            return redirect('cursos')

    else:
        form = CursoForm()
        return render(request, 'mi_primer_app/crear_curso.html', {'form': form})
    
def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            # Procesar el formulario
            nuevo_estudiante = Estudiante(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                edad=form.cleaned_data['edad'],
                fecha_inscripcion=form.cleaned_data['fecha_inscripcion']
            )
            nuevo_estudiante.save()
            return redirect('inicio')

    else:
        form = EstudianteForm()
        return render(request, 'mi_primer_app/crear_estudiante.html', {'form': form})

def buscar_estudiantes(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        estudiantes = Estudiante.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/estudiantes.html', {'estudiantes': estudiantes, 'nombre': nombre})
    else:
        return redirect('inicio')

def estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'mi_primer_app/estudiantes.html', {'estudiantes': estudiantes})
    
def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'mi_primer_app/cursos.html', {'cursos': cursos})
    
def buscar_cursos(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        cursos = Curso.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/cursos.html', {'cursos': cursos, 'nombre_curso': nombre})
    else:
        return redirect('inicio')

def ropa(request):
    ropas = Ropa.objects.all()
    return render(request, 'mi_primer_app/ropa.html', {'ropas': ropas})
    
def crear_ropa(request):
    if request.method == 'POST':
        form = RopaForm(request.POST)
        if form.is_valid():
            # Procesar el formulario
            nueva_ropa = Ropa(
                nombre=form.cleaned_data['nombre'],
                sexo=form.cleaned_data['sexo'],
                tipo=form.cleaned_data['tipo'],
                talla=form.cleaned_data['talla'],
                color=form.cleaned_data['color']
            )
            nueva_ropa.save()
            return redirect('inicio')

    else:
        form = RopaForm()
        return render(request, 'mi_primer_app/crear_ropa.html', {'form': form})

def buscar_ropa(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '')
        ropas = Ropa.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_primer_app/ropa.html', {'ropas': ropas, 'nombre': nombre})
    else:
        return redirect('inicio')
    
def celulares(request):
    celulares = Celular.objects.all()
    return render(request, 'mi_primer_app/celulares.html', {'celulares': celulares})

def crear_celular(request):
    if request.method == 'POST':
        form = CelularForm(request.POST)
        if form.is_valid():
            # Procesar el formulario
            nuevo_celular = Celular(
                marca=form.cleaned_data['marca'],
                modelo=form.cleaned_data['modelo'],
                precio=form.cleaned_data['precio'],
                fecha_lanzamiento=form.cleaned_data['fecha_lanzamiento'],
                estado=form.cleaned_data['estado']
            )
            nuevo_celular.save()
            return redirect('inicio')

    else:
        form = CelularForm()
        return render(request, 'mi_primer_app/crear_celular.html', {'form': form})  

def buscar_celulares(request):
    if request.method == 'GET':
        marca = request.GET.get('marca', '')
        celulares = Celular.objects.filter(marca__icontains=marca)
        return render(request, 'mi_primer_app/celulares.html', {'celulares': celulares, 'marca': marca})
    else:
        return redirect('celulares')
    