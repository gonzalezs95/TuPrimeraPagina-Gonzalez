from django.contrib import admin

# Register your models here.
from .models import Familiar

register_models = [Familiar]

admin.site.register(register_models)