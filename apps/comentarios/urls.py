# apps/comentarios/urls.py

from django.urls import path
from . import views

# Definimos el namespace para ser usado en reverse y en la plantilla
app_name = 'comentarios'

urlpatterns = [
    
    # URL para agregar un comentario (Ej: /comentarios/agregar/5/)
    # Usamos 'agregar' como name para que coincida con el uso en la plantilla.
    path('agregar/<int:publicacion_id>/', views.agregar_comentario, name='agregar'), 
    
    # URL para eliminar un comentario (Ej: /comentarios/eliminar/12/)
    path('eliminar/<int:pk>/', views.ComentarioDeleteView.as_view(), name='eliminar_comentario'),

    # Nueva ruta para la edicion de un comentario
    path('editar/<int:pk>/', views.ComentarioUpdateView.as_view(), name='editar_comentario'),

]
