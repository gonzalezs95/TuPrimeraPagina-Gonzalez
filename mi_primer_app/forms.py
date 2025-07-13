from django import forms

class CursoForm(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField(widget=forms.Textarea, required=False)
    duracion_semanas = forms.IntegerField(min_value=1, initial=4)
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    activo = forms.BooleanField(required=False, initial=True)

class EstudianteForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    edad = forms.IntegerField(min_value=1)
    fecha_inscripcion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)  # Auto-filled by the model

class RopaForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    sexo = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Femenino')])
    tipo = forms.CharField(max_length=50)
    talla = forms.CharField(max_length=10)
    color = forms.CharField(max_length=20)

class CelularForm(forms.Form):
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    fecha_lanzamiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    estado = forms.ChoiceField(choices=[('Nuevo', 'Nuevo'), ('Usado', 'Usado')])
    