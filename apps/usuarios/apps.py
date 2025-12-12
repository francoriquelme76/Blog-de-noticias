from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Ruta completa
    name = 'apps.usuarios'

    # Etiqueta corta (la que usará Django internamente)
    label = 'usuarios'

    # Nombre legible
    verbose_name = 'Modulo de Usuarios'