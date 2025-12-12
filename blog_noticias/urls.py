# blog_noticias/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Necesario para media/static en DEBUG
from django.conf.urls.static import static # Necesario para media/static en DEBUG


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. URLs de la aplicación USUARIOS (REGISTRO)
    # Patrón: /cuentas/registro/
    path('cuentas/', include('apps.usuarios.urls', namespace='usuarios')), 
    
    # 2. LOGIN, LOGOUT, PASSWORD RESET, etc. (Usamos el set completo de Django)
    # Patrón: /cuentas/login/, /cuentas/logout/, etc.
    path('cuentas/', include('django.contrib.auth.urls')),
    
    # 3. URLs de la aplicación COMENTARIOS
    # ¡CRÍTICO! Esto registra el namespace 'comentarios' que tu plantilla necesita.
    # Patrón: /comentarios/
    path('comentarios/', include('apps.comentarios.urls', namespace='comentarios')),
    
    # 4. URLs de publicaciones (Home)
    # Patrón: /
    path('', include('apps.publicaciones.urls')),
]

# Configuración para servir archivos MEDIA y STATIC durante el desarrollo (DEBUG=True)
if settings.DEBUG:
    # Si usas archivos subidos por el usuario (imágenes de publicaciones, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    # Nota: Los archivos STATIC ya suelen ser servidos por runserver, 
    # pero esta línea es útil si tienes configuraciones específicas.
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)