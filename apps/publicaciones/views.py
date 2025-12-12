# apps/publicaciones/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required 
from django.urls import reverse_lazy, reverse 
from django.utils.text import slugify 

from .models import Publicacion, Categoria 
from .forms import PublicacionForm 

# Importaciones para comentarios:
from apps.comentarios.forms import ComentarioForm
from apps.comentarios.models import Comentario 

# Importaciones de Vistas Basadas en Clases (CBV) y Mixins de Seguridad
from django.views.generic import CreateView, UpdateView, DeleteView 
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin 


# 1. Vista para la lista de publicaciones (Función, mejorada para categorías)
def lista_publicaciones(request):
    """
    Obtiene todas las publicaciones y todas las categorías para la navegación.
    (Visitante Anónimo y Registrado - Nivel 1 y 2)
    """
    publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')
    categorias = Categoria.objects.all()
    
    # 🚨 INICIO DE LA CORRECCIÓN 🚨
    # Verificamos si el usuario tiene el permiso de crear publicaciones (Colaborador)
    puede_crear = request.user.is_authenticated and request.user.has_perm('publicaciones.add_publicacion')
    # 🚨 FIN DE LA CORRECCIÓN 🚨
    
    contexto = {
        'object_list': publicaciones,
        'titulo': 'Últimas Publicaciones',
        'categorias': categorias, # Pasamos las categorías a la plantilla
        # 🚨 PASAMOS LA VARIABLE BOLEANA AL CONTEXTO 🚨
        'puede_crear': puede_crear,
    }
    
    return render(request, 'publicaciones/lista_publicaciones.html', contexto) 


# 2. Vista para el detalle de un artículo (Función con lógica de Comentarios)
def detalle_publicacion(request, pk, slug):
    """
    Muestra el detalle de una publicación, incluyendo comentarios.
    (Visitante Anónimo y Registrado - Nivel 1 y 2)
    """
    publicacion = get_object_or_404(
        Publicacion, 
        pk=pk, 
        slug=slug
    )
    
    # Obtener solo los comentarios aprobados de esta publicación
    comentarios = publicacion.comentarios.filter(aprobado=True) 
    
    # 🚨 CORRECCIÓN CLAVE: Inicializar el formulario aquí para pasarlo al contexto
    comentario_form = ComentarioForm() 
    
    contexto = {
        'publicacion': publicacion,
        'comentarios': comentarios,      
        'form': comentario_form,
    }
    
    return render(request, 'publicaciones/detalle_publicacion.html', contexto)


# 3. Vista para crear una publicación (Clase)
class PublicacionCrearView(PermissionRequiredMixin, CreateView):
    """
    Permite a los Colaboradores crear una publicación.
    """
    # 🚨 RESTRICCIÓN Nivel 3: Solo si tiene el permiso asignado al grupo COLABORADORES 🚨
    permission_required = 'publicaciones.add_publicacion'
    
    model = Publicacion
    form_class = PublicacionForm 
    template_name = 'publicaciones/publicacion_form.html'
    success_url = reverse_lazy('publicaciones:lista') 
    
    def form_valid(self, form):
        form.instance.autor = self.request.user

        # Asegura que el slug se genera solo si no fue enviado o no existe
        if not form.instance.slug:
            form.instance.slug = slugify(form.instance.titulo)
            
        return super().form_valid(form)


# 4. Vista para editar una publicación (Clase)
class PublicacionEditarView(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Permite al autor (Colaborador) editar su propia publicación. 
    """
    # 🚨 RESTRICCIÓN Nivel 3: El usuario debe tener permiso para editar cualquier publicación 🚨
    permission_required = 'publicaciones.change_publicacion' 

    model = Publicacion
    form_class = PublicacionForm 
    template_name = 'publicaciones/publicacion_form.html'
    
    # Redirige al detalle del artículo después de la edición
    def get_success_url(self):
        return reverse('publicaciones:detalle', kwargs={'pk': self.object.pk, 'slug': self.object.slug})
    
    # Método CRÍTICO: Comprueba si el usuario logueado es el autor
    def test_func(self):
        publicacion = self.get_object()
        # Permitir la edición si es el autor O si el usuario tiene el permiso de cambio global
        return publicacion.autor == self.request.user or self.request.user.has_perm('publicaciones.change_publicacion')

    # Sobreescribir form_valid para regenerar el slug si el título cambia
    def form_valid(self, form):
        if not form.instance.slug:
            form.instance.slug = slugify(form.instance.titulo)
        return super().form_valid(form)


# 5. Vista para la lista de publicaciones filtrada por categoría (Función)
def publicaciones_por_categoria(request, slug_categoria):
    """
    Muestra la lista de publicaciones filtrada por una categoría específica.
    (Visitante Anónimo y Registrado - Nivel 1 y 2)
    """
    categoria = get_object_or_404(Categoria, slug=slug_categoria)
    publicaciones = Publicacion.objects.filter(categoria=categoria).order_by('-fecha_creacion')
    
    # Pasamos todas las categorías para que el menú de categorías siga funcionando
    categorias = Categoria.objects.all()
    
    # 🚨 INICIO DE LA CORRECCIÓN 🚨
    # Verificamos si el usuario tiene el permiso de crear publicaciones (Colaborador)
    puede_crear = request.user.is_authenticated and request.user.has_perm('publicaciones.add_publicacion')
    # 🚨 FIN DE LA CORRECCIÓN 🚨
    
    contexto = {
        'object_list': publicaciones,
        'titulo': f'Noticias de {categoria.nombre}', 
        'categorias': categorias, 
        'categoria_actual': categoria,
        # 🚨 PASAMOS LA VARIABLE BOLEANA AL CONTEXTO 🚨
        'puede_crear': puede_crear,
    }
    
    return render(request, 'publicaciones/lista_publicaciones.html', contexto)

# 6. Vista para eliminar una publicación (AÑADIDO PARA COMPLETAR EL CRUD)
class PublicacionEliminarView(PermissionRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Permite al autor (Colaborador) eliminar su propia publicación.
    """
    # 🚨 RESTRICCIÓN Nivel 3
    permission_required = 'publicaciones.delete_publicacion'
    model = Publicacion
    template_name = 'publicaciones/publicacion_confirm_delete.html' # Debes crear esta plantilla
    success_url = reverse_lazy('publicaciones:lista') 

    # Solo permite eliminar si es el autor o tiene el permiso global de eliminar
    def test_func(self):
        publicacion = self.get_object()
        return publicacion.autor == self.request.user or self.request.user.has_perm('publicaciones.delete_publicacion')