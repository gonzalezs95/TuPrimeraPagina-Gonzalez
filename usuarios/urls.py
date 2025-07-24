from django.urls import path

from .views import CustomLogoutView, UserRegisterView, CustomLoginView, ProfileView, AvatarUpdateView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('update-avatar/', AvatarUpdateView.as_view(), name='avatar_update'),
]