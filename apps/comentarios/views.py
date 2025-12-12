# apps/comentarios/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# 🚨 CORRECCIÓN CLAVE: Se usa la ruta completa 'apps.publicaciones' 
# para resolver el RuntimeError debido a la estructura de carpetas anidadas.
from apps.publicaciones.models import Publicacion 

from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView

from .models import Comentario
from .forms import ComentarioForm


@login_required # <--- RESTRICCIÓN: Solo usuarios autenticados (Nivel 2 y 3) pueden acceder
def agregar_comentario(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, pk=publicacion_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            
            # no guarda directamente, solamente crea el objeto
            comentario = form.save(commit=False)

            # Asigna claves externas de autor y publicacion
            comentario.autor = request.user
            comentario.publicacion = publicacion

            # Guardar comentario en BDD
            comentario.save()

            # redirigir al detalle de la publicacion
            # Usamos el método get_absolute_url() para una redirección robusta
            return redirect(publicacion.get_absolute_url()) 
        
    # Si hay un error en el formulario (o si es GET)
    return redirect(publicacion.get_absolute_url())


# Mixin de Seguridad: Define quién puede ejecutar la acción
class AutorComentarioOAdminMixin(UserPassesTestMixin):
    def test_func(self):
        comentario = self.get_object()
        
        # El usuario es el autor del comentario O el rol es 'Admin'
        # NOTA: Si no tienes el campo 'rol' en el modelo User, 'self.request.user.is_superuser' es la alternativa.
        # Ajusta esta línea según tu modelo de usuario personalizado.
        es_autor = self.request.user == comentario.autor
        es_admin = self.request.user.is_superuser # Usamos is_superuser como fallback/alternativa a 'rol == Admin'
        
        # Asumiendo que tu usuario tiene el campo 'rol':
        # return es_autor or self.request.user.rol == 'Admin'
        
        # Usando la superposición de Django:
        return es_autor or es_admin


class ComentarioDeleteView(LoginRequiredMixin, AutorComentarioOAdminMixin, DeleteView):
    model = Comentario
    template_name = 'comentarios/comentario_confirm_delete.html' # Debe crear este template
    
    def get_success_url(self):
        # Redirige al URL de la publicación después de eliminar
        return self.object.publicacion.get_absolute_url()


class ComentarioUpdateView(LoginRequiredMixin, AutorComentarioOAdminMixin, UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = 'comentarios/comentario_form.html'

    def get_success_url(self):
        # redirige al detalle de la publicacion despues de editar
        return self.object.publicacion.get_absolute_url()