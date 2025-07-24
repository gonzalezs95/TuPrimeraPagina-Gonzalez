from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import RegisterForm, AvatarForm
from django.views import View
from .models import Avatar

class UserRegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'usuarios/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'])
        if user:
            login(self.request, user)
        return response

class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'
    
    def get_success_url(self):
        return reverse_lazy('inicio')  # Redirect to home after login
    
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirect to login after logout

class ProfileView(DetailView):
    model = User
    template_name = 'usuarios/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user  # Return the current logged-in user
    
class ProfileUpdateView(View):
    template_name = "user/edit_profile.html"
    success_url = reverse_lazy('profile')

    def get(self, request, *args, **kwargs):
        user_form = ProfileUpdateView(instance=request.user)
        avatar, _ = Avatar.objects.get_or_create(user=request.user)
        avatar_form = AvatarForm(instance=avatar)
        password_form = PasswordChangeForm(request.user)
        context = {
            'user_form': user_form,
            'avatar_form': avatar_form,
            'password_form': password_form
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        user_form = ProfileUpdateView(request.POST, instance=request.user)
        avatar, _ = Avatar.objects.get_or_create(user=request.user)
        avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        password_form = PasswordChangeForm(request.user, request.POST)

        if "update_profile" in request.POST:
            if user_form.is_valid() and avatar_form.is_valid():
                user_form.save()
                avatar_form.save()
                return redirect(self.success_url)
        elif "change_password" in request.POST:
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                return redirect(self.success_url)
        context = {
            'user_form': user_form,
            'avatar_form': avatar_form,
            'password_form': password_form
        }
        return render(request, self.template_name, context)

class AvatarUpdateView(UpdateView):
    model = Avatar
    form_class = AvatarForm
    template_name = 'usuarios/avatar_form.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        avatar, created = Avatar.objects.get_or_create(user=self.request.user)
        return avatar



class ProfileUpdateView(UpdateView):
    model = User
    