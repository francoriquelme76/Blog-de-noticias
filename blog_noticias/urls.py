"""
URL configuration for blog_noticias project.
"""
from django.contrib import admin
from django.urls import path, include # 1. ¡IMPORTAR 'include'!

urlpatterns = [
    # URL para el panel de administración
    path('admin/', admin.site.urls),
    
    # 2. Conecta la raíz ('') del sitio a las URLs de la aplicación publicaciones
    # Esto le dice a Django que busque las rutas en apps/publicaciones/urls.py
    path('', include('apps.publicaciones.urls')),
]