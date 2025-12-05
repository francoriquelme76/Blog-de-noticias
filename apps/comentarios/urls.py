from django.urls import path
from . import views



urlpatterns = [
    
    # URL para agregar un comentario (Ej: /comentarios/agregar/5/)
    path('agregar/<int:publicacion_id>/', views.agregar_comentario, name='agregar_comentario'),
    
    # URL para eliminar un comentario (Ej: /comentarios/eliminar/12/)
    path('eliminar/<int:pk>/', views.ComentarioDeleteView.as_view(), name='eliminar_comentario'),

    #Nueva ruta para la edicion de un comentario
    path('editar/<int:pk>/', views.ComentarioUpdateView.as_view(), name='editar_comentario'),

]