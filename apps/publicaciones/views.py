from django.shortcuts import render, get_object_or_404
from .models import Publicacion, Categoria # Importamos los modelos

# 1. Vista para la lista de publicaciones (Función)
def lista_publicaciones(request):
    """
    Obtiene todas las publicaciones y las muestra en la página de inicio.
    """
    # Consulta la base de datos para obtener todas las publicaciones
    publicaciones = Publicacion.objects.all()
    
    # Prepara el contexto (los datos que se enviarán al template)
    contexto = {
        'publicaciones': publicaciones,
        'titulo': 'Blog de Noticias',
    }
    
    # Renderiza (muestra) el template HTML con los datos
    return render(request, 'publicaciones/lista_publicaciones.html', contexto)

# 2. Vista para el detalle de un artículo (Función)
def detalle_publicacion(request, pk, slug):
    """
    Obtiene una publicación específica usando su ID (pk) y slug.
    """
    # Usa get_object_or_404 para buscar la Publicacion por su ID (pk) y slug
    # Si no la encuentra, Django automáticamente retorna un error 404 (página no encontrada)
    publicacion = get_object_or_404(
        Publicacion, 
        pk=pk, 
        slug=slug
    )
    
    contexto = {
        'publicacion': publicacion,
        'titulo': publicacion.titulo,
    }
    
    return render(request, 'publicaciones/detalle_publicacion.html', contexto)