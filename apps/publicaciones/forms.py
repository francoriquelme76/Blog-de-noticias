# apps/publicaciones/forms.py

from django import forms
from .models import Publicacion

class PublicacionForm(forms.ModelForm):
    # Sobreescribimos el campo 'slug' para hacerlo NO requerido
    slug = forms.CharField(
        required=False,
        label="Slug (URL amigable, se genera automáticamente si está vacío)",
        help_text="Opcional. Si lo deja vacío, se generará a partir del título."
    )

    class Meta:
        model = Publicacion
        # Definimos los campos que SÍ queremos que se muestren en el formulario
        fields = ('titulo', 'contenido', 'categoria', 'slug')
        