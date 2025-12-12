# blog_noticias/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# 🚨 Importación CRÍTICA para las URLs de autenticación de Django 🚨
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. URLs de la aplicación USUARIOS (REGISTRO)
    # Patrón: /cuentas/registro/
    path('cuentas/', include('apps.usuarios.urls', namespace='usuarios')), 
    
    # 2. LOGIN, LOGOUT, PASSWORD RESET, etc. (Usamos el set completo de Django)
    # 🚨 CORRECCIÓN CLAVE: Eliminamos 'name='auth' para evitar el KeyError/NoReverseMatch 🚨
    # Ahora las URLS se buscarán como 'login' y 'logout' (sin namespace)
    path('cuentas/', include('django.contrib.auth.urls')),
    
    # 3. URLs de la aplicación COMENTARIOS
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