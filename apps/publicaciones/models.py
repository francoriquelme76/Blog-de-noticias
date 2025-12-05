# publicaciones/models.py
from django.db import models
from django.conf import settings # Necesario para referenciar AUTH_USER_MODEL
from django.utils import timezone

class Categoria(models.Model):
    """Modelo para clasificar las publicaciones (Deportes, Economía, etc.)."""
    nombre = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = "Categorias" # Nombre que aparece en el Admin de Django
    
    def __str__(self):
        return self.nombre

class Publicacion(models.Model):
    """Modelo principal para el artículo de noticias o blog."""
    
    titulo = models.CharField(max_length=250)
    contenido = models.TextField()
    
    # Fecha de creación, establecida automáticamente al crear el objeto
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    # Relación de Clave Foránea (ForeignKey) con Categoria
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL, # Si se borra la categoría, la publicación mantiene el campo vacío
        null=True, 
        blank=True,
        related_name='publicaciones' 
    )
    
    # Relación de Clave Foránea (ForeignKey) con el Autor (usa el modelo Perfil)
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL, # Referencia a usuarios.Perfil, gracias al settings.py
        on_delete=models.CASCADE, # Si se borra el Perfil, se borran sus publicaciones
        related_name='publicaciones_autor'
    )
    
    # URL amigable, útil para SEO y URLs limpias // wao
    slug = models.SlugField(max_length=250, unique_for_date='fecha_creacion')

    class Meta:
        # Ordena la lista de publicaciones de más reciente a más antigua
        ordering = ['-fecha_creacion']
        
    def __str__(self):
        return self.titulo