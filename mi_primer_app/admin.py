from django.contrib import admin

# Register your models here.
from .models import Familiar, Curso, Estudiante, Ropa, Celular

register_models = [Familiar, Curso, Estudiante, Ropa, Celular]

admin.site.register(register_models)