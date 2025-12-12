# apps/comentarios/views.py

from django.urls import reverse_lazy
# 🚨 CORRECCIÓN 1: Agregar importaciones necesarias para la función agregar_comentario
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required 
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Comentario
from .forms import ComentarioForm
# 🚨 CORRECCIÓN 1: Importar el modelo Publicacion de la aplicación correspondiente
from apps.publicaciones.models import Publicacion 


# <--- VISTA BASADA EN FUNCIÓN (FBV) PARA AGREGAR COMENTARIOS --->

@login_required # RESTRICCIÓN: Solo usuarios autenticados (Nivel 2 y 3) pueden acceder
def agregar_comentario(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, pk=publicacion_id)

    if request.method == 'POST':
        # Instancia el formulario con los datos POST
        form = ComentarioForm(request.POST)
        
        if form.is_valid():
            
            # Crear el objeto, pero sin guardar en la BD aún
            comentario = form.save(commit=False)

            # Asigna claves externas de autor (usuario logueado) y publicacion
            comentario.autor = request.user
            comentario.publicacion = publicacion

            # Guardar comentario en BDD
            comentario.save()

            # Redirigir al detalle de la publicacion
            # Usamos el método get_absolute_url() para una redirección robusta
            return redirect(publicacion.get_absolute_url()) 
        else:
            # Si el formulario no es válido, redirigir y mostrar la publicación
            # El usuario verá la publicación con el formulario vacío (GET) y deberá intentarlo de nuevo.
            # En un entorno real, pasarías el formulario inválido al render, pero con redirect es más simple.
            return redirect(publicacion.get_absolute_url())
    
    # 🚨 MEJORA: Si es GET a esta URL sin querer, simplemente redirige a la publicación.
    return redirect(publicacion.get_absolute_url())


# <--- VISTAS BASADAS EN CLASES (CBV) PARA EDICIÓN Y ELIMINACIÓN --->

# Mixin de Seguridad: Define quién puede ejecutar la acción (Autor o Superusuario)
class AutorComentarioOAdminMixin(UserPassesTestMixin):
    """
    Permite el acceso a la vista solo si:
    1. El usuario logueado es el autor del comentario.
    2. El usuario logueado es un superusuario (Admin).
    """
    def test_func(self):
        comentario = self.get_object()
        
        es_autor = self.request.user == comentario.autor
        es_admin = self.request.user.is_superuser 
        
        return es_autor or es_admin


class ComentarioDeleteView(LoginRequiredMixin, AutorComentarioOAdminMixin, DeleteView):
    model = Comentario
    template_name = 'comentarios/comentario_confirm_delete.html' # Debe crear este template
    
    def get_success_url(self):
        # Redirige al URL de la publicación después de eliminar
        # Usamos self.object para acceder al comentario que se acaba de eliminar
        return self.object.publicacion.get_absolute_url()


class ComentarioUpdateView(LoginRequiredMixin, AutorComentarioOAdminMixin, UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentarios/comentario_form.html'

    def get_success_url(self):
        # Redirige al detalle de la publicacion después de editar
        # Usamos self.object para acceder al comentario que se acaba de editar
        return self.object.publicacion.get_absolute_url()