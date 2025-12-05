from django.apps import AppConfig


class PublicacionesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.publicaciones'

    label = 'publicaciones'

    verbose_name = 'Modulo de Publicaciones'
