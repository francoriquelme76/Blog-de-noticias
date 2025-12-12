# apps/publicaciones/context_processors.py

from .models import Categoria # 🌟 ¡IMPORTACIÓN CORREGIDA AQUÍ! 🌟

def categories_processor(request):
    """
    Inyecta la lista de todas las categorías en el contexto de todas las plantillas.
    """
    try:
        # Obtiene todas las categorías ordenadas por nombre
        all_categories = Categoria.objects.all().order_by('nombre')
    except Exception:
        all_categories = []
        
    return {'categories': all_categories}