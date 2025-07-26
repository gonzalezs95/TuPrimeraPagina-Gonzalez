from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_paletas, name='lista_paletas'),
    path('crear/', views.crear_paleta, name='crear_paleta'),
    path('paleta/<int:pk>/', views.detalle_paleta, name='detalle_paleta'),
    path('register/', views.register, name='register'),
    path('eliminar/<int:pk>/', views.eliminar_paleta, name='eliminar_paleta'),
]
