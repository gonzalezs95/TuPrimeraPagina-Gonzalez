from django.shortcuts import render, get_object_or_404, redirect
from .models import Paleta, Comentario
from .forms import PaletaForm, ComentarioForm
from django.contrib.auth.decorators import login_required
from usuarios.forms import RegisterForm
from django.contrib.auth import login, authenticate

def lista_paletas(request):
    paletas = Paleta.objects.all().order_by('-created_at')
    return render(request, 'blog/lista_paletas.html', {'paletas': paletas})

@login_required
def crear_paleta(request):
    if request.method == 'POST':
        form = PaletaForm(request.POST, request.FILES)
        if form.is_valid():
            paleta = form.save(commit=False)
            paleta.author = request.user
            paleta.save()
            return redirect('lista_paletas')
    else:
        form = PaletaForm()
    return render(request, 'blog/crear_paleta.html', {'form': form})

def detalle_paleta(request, pk):
    paleta = get_object_or_404(Paleta, pk=pk)
    comentarios = paleta.comentarios.all()
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = paleta
            comentario.author = request.user
            comentario.save()
            return redirect('detalle_paleta', pk=paleta.pk)
    else:
        form = ComentarioForm()
    return render(request, 'blog/detalle_paleta.html', {'paleta': paleta, 'comentarios': comentarios, 'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Guardar el nuevo usuario
            user = form.save()
            # Autenticar al usuario después del registro
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # Tienes que usar password1 para autenticarse
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)  # Iniciar sesión al registrar
            return redirect('tienda_padel:lista_paletas')  # Redirigir al listado de paletas
    else:
        form = RegisterForm()

    return render(request, 'tienda_padel/register.html', {'form': form})

def eliminar_paleta(request, pk):
    paleta = get_object_or_404(Paleta, pk=pk)
    paleta.delete()
    return redirect('tienda_padel:lista_paletas') 
