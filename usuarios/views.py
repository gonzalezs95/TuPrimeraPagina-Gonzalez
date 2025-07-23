from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .forms import RegistreForm

class UserRegisterView(CreateView):
    model = User
    form_class = RegistreForm
    template_name = 'usuarios/register.html'
    success_url = reverse_lazy('login')