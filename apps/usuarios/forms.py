# apps/usuarios/forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model # Usamos get_user_model() para mayor robustez

# Obtenemos el modelo de usuario activo (generalmente django.contrib.auth.models.User)
User = get_user_model()

# Heredamos del formulario estándar de creación de usuarios de Django
class FormularioRegistroUsuario(UserCreationForm):
    
    class Meta:
        model = User
        # Al heredar de UserCreationForm, NO ES NECESARIO LISTAR 'password' 
        # (ya que UserCreationForm agrega los campos de contraseña).
        # Para evitar problemas, listamos los campos que queremos mostrar, 
        # que suelen ser solo el 'username' y el email (si lo usas), 
        # pero para el User base, 'username' es suficiente.
        
        # Una forma común de listar solo los campos del User base que queremos (sin password)
        fields = ('username', 'email') # Incluir 'email' es una buena práctica, aunque no obligatorio.
        
        # Si SOLO quieres el nombre de usuario, la forma correcta de hacerlo es:
        # fields = ('username',) 
        # Pero si tienes un formulario basado en tu modelo de usuario, es mejor incluir:
        
        # Usaremos la forma que incluye 'username' y 'email' para una mejor experiencia de registro:
        fields = ('username', 'email')
        