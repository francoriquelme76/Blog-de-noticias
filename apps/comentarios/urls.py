# apps/comentarios/urls.py

from django.urls import path
from . import views

# Definimos el namespace para ser usado en reverse y en la plantilla
app_name = 'comentarios'

urlpatterns = [
    
    # URL para agregar un comentario (Ej: /comentarios/agregar/5/)
    # El name es 'agregar' y coincide con la plantilla.
    path('agregar/<int:publicacion_id>/', views.agregar_comentario, name='agregar'), 
    
    # 🚨 CORRECCIÓN 1: Cambiado name='eliminar_comentario' a name='eliminar' 🚨
    # URL para eliminar un comentario (Ej: /comentarios/eliminar/12/)
    path('eliminar/<int:pk>/', views.ComentarioDeleteView.as_view(), name='eliminar'),

    # 🚨 CORRECCIÓN 2: Cambiado name='editar_comentario' a name='editar' 🚨
    # Nueva ruta para la edicion de un comentario
    path('editar/<int:pk>/', views.ComentarioUpdateView.as_view(), name='editar'),

]