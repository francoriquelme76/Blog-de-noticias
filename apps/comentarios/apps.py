from django.apps import AppConfig

class ComentariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Ruta completa a la aplicación
    name = 'apps.comentarios'
    
    # Etiqueta corta de la aplicación, útil para la referencia interna
    label = 'comentarios' 
    
    # Nombre legible para el Admin
    verbose_name = 'Módulo de Comentarios'