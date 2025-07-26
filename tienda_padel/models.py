from django.db import models
from django.contrib.auth.models import User

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
