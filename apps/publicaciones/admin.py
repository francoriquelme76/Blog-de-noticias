from django.contrib import admin
from .models import Categoria, Publicacion # 1. Importar los modelos

# 2. Personalizar la visualización del modelo Publicacion en el Admin
@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    # Campos que se muestran en la lista de publicaciones
    list_display = ('titulo', 'autor', 'categoria', 'fecha_creacion')
    
    # Campos por los que se puede filtrar la lista
    list_filter = ('categoria', 'autor', 'fecha_creacion')
    
    # Campos que permiten buscar
    search_fields = ('titulo', 'contenido')
    
    # Pre-poblar automáticamente el campo 'slug' a partir del 'titulo'
    prepopulated_fields = {'slug': ('titulo',)} 
    
    # Muestra el autor logueado como valor por defecto (útil para el proceso de creación)
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.autor = request.user # Asigna el usuario actual como autor
        super().save_model(request, obj, form, change)

# 3. Registrar el modelo Categoria
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)