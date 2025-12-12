from django.apps import AppConfig


class PublicacionesConfig(AppConfig):
    # Campo predeterminado para claves primarias
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Nombre de la aplicación (la ruta completa dentro de la estructura de carpetas)
    name = 'apps.publicaciones'

    # Etiqueta corta de la aplicación, usada internamente por Django (es lo que faltaba en INSTALLED_APPS)
    label = 'publicaciones'

    # Nombre legible por humanos para el Admin