from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    parentesco = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}{self.apellido} ({self.parentesco}) - Edad: {self.edad}, Nacido el: {self.fecha_nacimiento}"
class Curso(models.Model):
  nombre = models.CharField(max_length=50)
  descripcion = models.TextField(blank=True, null=True)
  duracion_semanas = models.IntegerField(default=4)
  fecha_inicio = models.DateField()
  activo = models.BooleanField(default=True)

  def __str__(self):
    return self.nombre
     
class Estudiante(models.Model):
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  email = models.EmailField(unique=True)
  edad = models.IntegerField()
  fecha_inscripcion = models.DateField(auto_now_add=True)

  def __str__(self):
    return f"{self.nombre} {self.apellido} ({self.email}) - Edad: {self.edad}, Inscrito el: {self.fecha_inscripcion}"

class Ropa(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)
    tipo = models.CharField(max_length=50)
    talla = models.CharField(max_length=10)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - Talla: {self.talla}, Color: {self.color}"
     
class Celular(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_lanzamiento = models.DateField()
    estado = models.CharField(choices=[('Nuevo', 'Nuevo'), ('Usado', 'Usado')], max_length=10)

    def __str__(self):
        return f"{self.marca} {self.modelo} - Precio: {self.precio}, Lanzado el: {self.fecha_lanzamiento}"

class Auto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.marca} {self.modelo}"

class Paleta(models.Model):
    PALETA_TIPOS = (
        ('nueva', 'Nueva'),
        ('usada', 'Usada'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    condition = models.CharField(max_length=6, choices=PALETA_TIPOS)
    image = models.ImageField(upload_to='paletas/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comentario(models.Model):
    post = models.ForeignKey(Paleta, related_name='comentarios', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.author} en {self.post.title}"