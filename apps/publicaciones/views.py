# publicaciones/views.py
from django.shortcuts import render, get_object_or_404
from .models import Publicacion

# ------------------------------
# VISTA 1: LISTADO DE PUBLICACIONES (Página Principal)
# ------------------------------
def lista_publicaciones(request):
    """
    Muestra una lista de todas las publicaciones, ordenada por fecha.
    Aquí se implementará el filtro (Requerimiento 5) más adelante.
    """
    
    # Obtiene todas las publicaciones de la base de datos
    # El .order_by('-fecha_creacion') ya está definido en models.py
    publicaciones = Publicacion.objects.all() 

    context = {
        'publicaciones': publicaciones,
        'titulo': 'Portal de Noticias'
    }
    
    # Renderiza el template que aún no hemos creado (publicaciones/lista.html)
    return render(request, 'publicaciones/lista.html', context)

# ------------------------------
# VISTA 2: DETALLE DE PUBLICACIÓN
# ------------------------------
def detalle_publicacion(request, pk, slug):
    """
    Muestra el contenido completo de una publicación específica.
    Usa el ID (pk) y el slug para buscar.
    """
    
    # Busca la publicación por su ID y slug, si no la encuentra, devuelve un error 404
    publicacion = get_object_or_404(
        Publicacion, 
        pk=pk, 
        slug=slug
    )
    
    context = {
        'publicacion': publicacion,
        'titulo': publicacion.titulo
    }
    
    # Renderiza el template de detalle (publicaciones/detalle.html)
    return render(request, 'publicaciones/detalle.html', context)
