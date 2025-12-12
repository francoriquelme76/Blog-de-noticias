# apps/publicaciones/urls.py
<<<<<<< HEAD
from django.urls import path
from . import views
from apps.usuarios.views import registro_usuario 

# Define el "namespace"
app_name = 'publicaciones'

urlpatterns = [
    # Ruta: / (Raíz del sitio) -> Muestra las primeras 8 publicaciones
    path('', views.lista_publicaciones, name='lista'),
    
    # ELIMINAMOS: path('cargar-mas/', views.cargar_mas_publicaciones, name='cargar_mas'),
    
    # Ruta: /articulo/slug-del-articulo/pk/ -> Muestra el artículo completo
    path('articulo/<slug:slug>/<int:pk>/', views.detalle_publicacion, name='detalle'),
    
    # Ruta: /registro/ -> Muestra el formulario de registro
    path('registro/', registro_usuario, name='registro'),
    
    # Ruta: /AcercaDe
    path('acerca/', views.acerca_de, name='acerca'),

    path('categoria/<slug:category_slug>/', views.category_posts, name='category_posts'),
]
=======

from django.urls import path
from . import views # Importamos todas las vistas

app_name = 'publicaciones'

urlpatterns = [
    # 1. HOME / LISTADO GENERAL (Nivel 1 y 2)
    # Patrón: /
    path('', views.lista_publicaciones, name='lista'),
    
    # 2. LISTADO POR CATEGORÍA (Nivel 1 y 2)
    # Patrón: /categoria/deportes/
    path('categoria/<slug:slug_categoria>/', 
         views.publicaciones_por_categoria, 
         name='por_categoria'),
    
    # 3. CREACIÓN DE PUBLICACIÓN (Nivel 3 - Colaborador)
    # Patrón: /crear/
    path('crear/', 
         views.PublicacionCrearView.as_view(), 
         name='crear'),
    
    # 4. EDICIÓN DE PUBLICACIÓN (Nivel 3 - Colaborador)
    # Patrón: /editar/1/
    path('editar/<int:pk>/', 
         views.PublicacionEditarView.as_view(), 
         name='editar'),

    # 5. ELIMINACIÓN DE PUBLICACIÓN (Nivel 3 - Colaborador)
    # Patrón: /eliminar/1/
    path('eliminar/<int:pk>/', 
         views.PublicacionEliminarView.as_view(), 
         name='eliminar'),
    
    # 6. DETALLE DE PUBLICACIÓN (Nivel 1 y 2)
    # Patrón: /articulo/1/mi-titulo-de-articulo/
    # Es CRÍTICO que esta URL de detalle vaya al final, 
    # ya que su patrón es más genérico que los anteriores.
    path('articulo/<int:pk>/<slug:slug>/', 
         views.detalle_publicacion, 
         name='detalle'),
]
>>>>>>> 4f114730af45f235e4354b8ed00145427861897c
