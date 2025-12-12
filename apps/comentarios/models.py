# apps/comentarios/models.py

from django.db import models
from django.utils import timezone 
from django.conf import settings 
from apps.publicaciones.models import Publicacion 

class Comentario(models.Model):
    """Modelo para los comentarios de los usuarios."""
    
    # 1. Relación con el usuario (Autor del comentario)
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comentarios_autor' # Nombre de la relación inversa desde el modelo de Usuario
    )
    
    # 2. Relación con la publicación
    publicacion = models.ForeignKey(
        Publicacion,
        on_delete=models.CASCADE,
        related_name='comentarios' # <--- NOMBRE CLAVE: Así se accede desde una Publicacion
    ) 
    
    # 3. Contenido del Comentario
    contenido = models.TextField(verbose_name='Comentario') 
    
    # 4. Fecha de Creación
    fecha_creacion = models.DateTimeField(default=timezone.now) 
    
    # 5. Campo de Moderación
    aprobado = models.BooleanField(default=False) 

    class Meta:
        # Ordena del más antiguo al más reciente
        ordering = ['fecha_creacion']

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.publicacion.titulo}"