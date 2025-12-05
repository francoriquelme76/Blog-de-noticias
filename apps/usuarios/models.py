# usuarios/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Perfil(AbstractUser):
    """
    Modelo de Usuario Personalizado que extiende AbstractUser de Django.
    Define los roles (Admin, Autor, Registrado) para la gestión de permisos.
    """
    
    # Definición de las constantes de Roles
    ADMIN = 1
    AUTOR = 2
    REGISTRADO = 3
    
    ROLES_CHOICES = (
        (ADMIN, 'Administrador'),
        (AUTOR, 'Autor'),
        (REGISTRADO, 'Usuario Registrado'),
    )

    rol = models.CharField(max_length=10, choices=ROLES_CHOICES, default='Usuario')

    #Intento de solucion para evitar el CLASH con el modelo User predeterminado

    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'El grupo al que el usuario pertenece. Un usuario tendra todos los permisos'
            'Garantizado a cada uno de sus grupos.'
        ),
        related_name="perfil_set", #related_name UNICO 1
        related_query_name="perfil",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Permiso especifico para este usuario'),
        related_name="perfil_permissions_set", #related_name UNICO 2
        related_query_name="perfil_permission",
    )




    # Campo que almacena el rol del usuario (ESTE CAMPO FALTABA)
    #rol = models.PositiveSmallIntegerField(
    #    choices=ROLES_CHOICES,
    #    default=REGISTRADO)
    
    def __str__(self):
        # Muestra el nombre de usuario en el panel de administración (ESTE METODO FALTABA)
        return self.username
    
    # Métodos de ayuda para verificar roles en las vistas
    def es_admin(self):
        return self.rol == self.ADMIN

    def es_autor(self):
        return self.rol == self.AUTOR