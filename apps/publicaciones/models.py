# apps/publicaciones/models.py (Versión Corregida y Completa)

from django.db import models
from django.conf import settings # Necesario para referenciar AUTH_USER_MODEL
from django.utils import timezone
from django.utils.text import slugify 
from django.urls import reverse # 🚨 CORRECCIÓN 1: Importar reverse 🚨

class Categoria(models.Model):
    """Modelo para clasificar las publicaciones (Deportes, Economía, etc.)."""
    nombre = models.CharField(max_length=100, unique=True)
    
    # Añadir el campo slug aquí y permitirlo en blanco
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Categorias" # Nombre que aparece en el Admin de Django
    
    # Sobreescribir save() para autogenerar el slug si está vacío
    def save(self, *args, **kwargs):
        # Genera el slug automáticamente a partir del nombre si el campo slug está vacío
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class Publicacion(models.Model):
    """Modelo principal para el artículo de noticias o blog."""
    
    titulo = models.CharField(max_length=250)
    contenido = models.TextField()
    
    fecha_creacion = models.DateTimeField(default=timezone.now)
    
    # Relación de Clave Foránea (ForeignKey) con Categoria
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='publicaciones' 
    )
    
    # Relación de Clave Foránea (ForeignKey) con el Autor
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='publicaciones_autor'
    )
    
    slug = models.SlugField(max_length=250, unique_for_date='fecha_creacion', blank=True, null=True)

    class Meta:
        ordering = ['-fecha_creacion']
        
    # 🚨 CORRECCIÓN 2: Añadir get_absolute_url() para la redirección 🚨
    def get_absolute_url(self):
        """Devuelve la URL para acceder a la publicación en detalle."""
        # Asumo que tu URL de detalle en apps/publicaciones/urls.py se llama 'detalle'
        # y espera la clave primaria (pk) y el slug.
        return reverse('publicaciones:detalle', kwargs={'pk': self.pk, 'slug': self.slug})
        
    def __str__(self):
        return self.titulo