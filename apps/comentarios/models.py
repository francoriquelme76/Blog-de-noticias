# comentarios/models.py
from django.db import models
from django.conf import settings 
# ---------NOTA: RELOCALIZAR ESTA IMPORTACION PARA QUE COINCIDA CON LA APP DE PUBLICACIONES
from apps.publicaciones.models import Publicacion 

class Comentario(models.Model):
    # 1. Relación con el usuario del Colega A
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    
    # 2. Relación con la publicación del Colega B
    publicacion = models.ForeignKey(
        Publicacion, 
        on_delete=models.CASCADE,
        related_name='comentarios'
    ) 
    
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['fecha_creacion']

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.publicacion.titulo}"