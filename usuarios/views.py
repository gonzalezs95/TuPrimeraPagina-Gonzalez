from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class UserRegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'usuarios/register.html'
    success_url = reverse_lazy('login')