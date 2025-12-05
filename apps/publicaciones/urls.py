# publicaciones/urls.py
from django.urls import path
from . import views

# Define el "namespace" de la aplicación para evitar conflictos de nombres
app_name = 'publicaciones'

urlpatterns = [
    # Ruta: / (Raíz del sitio) -> Muestra todas las publicaciones
    path('', views.lista_publicaciones, name='lista'),
    
    # Ruta: /articulo/slug-del-articulo/ -> Muestra el artículo completo
    # <slug:slug> captura la parte amigable de la URL //que locura ajsdj , <int:pk> captura el ID
    path('articulo/<slug:slug>/<int:pk>/', views.detalle_publicacion, name='detalle'),
]