from django import forms
from .models import Paleta, Comentario

class PaletaForm(forms.ModelForm):
    class Meta:
        model = Paleta
        fields = ['title', 'description', 'price', 'condition', 'image']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['content']
