from django.urls import path

from .views import saludo, saludo_con_template, crear_familiar, inicio, crear_curso, crear_estudiante, cursos, buscar_cursos, crear_ropa, buscar_ropa, crear_celular, buscar_celulares, celulares, estudiantes, buscar_estudiantes

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('hola-mundo/', saludo),
    path('hola-mundo-template/', saludo_con_template),
    path('crear-familiar/<str:nombre>/', crear_familiar),
    path('crear-curso/', crear_curso , name = 'crear-curso'),
    path('crear-estudiante/', crear_estudiante , name = 'crear-estudiante'),
    path('estudiantes/buscar', buscar_estudiantes, name='buscar-estudiantes'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('cursos/', cursos , name='cursos'),
    path('cursos/buscar', buscar_cursos, name='buscar-cursos'),
    path('ropa/', buscar_ropa, name='buscar-ropa'),
    path('crear-ropa/', crear_ropa, name='crear-ropa'),
    path('ropa/buscar', buscar_ropa, name='buscar-ropa'),
    path('celulares/', celulares, name='celulares'),
    path('crear-celular/', crear_celular, name='crear-celular'),
    path('celulares/buscar', buscar_celulares, name='buscar-celulares'),
]