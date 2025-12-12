# apps/usuarios/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm # Usamos el formulario estándar de Django temporalmente

# Nota: Si ya tienes tu archivo forms.py, cambia la importación a:
# from .forms import FormularioRegistroUsuario 


# Vista para manejar el registro de nuevos usuarios
def registro_usuario(request):
    # Usamos el formulario estándar de Django (UserCreationForm)
    # Si tienes tu propio forms.py, descomenta la línea de arriba y usa FormularioRegistroUsuario
    form_class_to_use = UserCreationForm # Cambiar a FormularioRegistroUsuario si existe y está definido
    
    if request.method == 'POST':
        # Procesar los datos enviados por el usuario
        form = form_class_to_use(request.POST)
        if form.is_valid():
            # Guardar el nuevo usuario en la base de datos
            user = form.save()
            
            # Iniciar sesión automáticamente al nuevo usuario
            login(request, user)
            
            # Redirigir a la página de inicio.
            # Asumo que la URL principal de la app 'publicaciones' se llama 'lista'.
            return redirect('publicaciones:lista') 
    else:
        # Mostrar el formulario vacío si es una petición GET
        form = form_class_to_use()
        
    return render(request, 'usuarios/registro.html', {'form': form})
