from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from publicaciones.models import Publicacion #-- Enlazar bien la ruta de este import!!

from django.urls import reverse_lazy

from django.views.generic.edit import DeleteView, UpdateView

from .models import Comentario
from .forms import ComentarioForm




@login_required
def agregar_comentario(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, pk=publicacion_id)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            
            #no guarda directamente, solamente crea el objeto
            comentario = form.save(commit=False)

            #Asigna claves externas de autor y publicacion
            comentario.autor = request.user
            comentario.publicacion = publicacion

            #Guardar comentario en BDD
            comentario.save()

        #redirigir al detalle de la publicacion
        return redirect(f'{publicacion.get_absolute_url()}')
    
    #Si hay error, redirecciona a la publicacion
    return redirect(publicacion.get_absolute_url())



# Mixin de Seguridad: Define quién puede ejecutar la acción
class AutorComentarioOAdminMixin(UserPassesTestMixin):
    def test_func(self):
        comentario = self.get_object()
        # El usuario es el autor del comentario O el rol es 'Admin'
        return self.request.user == comentario.autor or self.request.user.rol == 'Admin'

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
        #redirige al detalle de la publicacion despues de editar
        return self.object.publicacion.get_absolute_url()
