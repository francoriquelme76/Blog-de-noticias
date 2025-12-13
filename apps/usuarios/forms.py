# apps/usuarios/forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model # Usamos get_user_model() para mayor robustez

# Importamos el modelo Perfil directamente desde la carpeta .models
from .models import Perfil

# Heredamos del formulario estándar de creación de usuarios de Django
class FormularioRegistroUsuario(UserCreationForm):
    
    class Meta:
        # FIXEADO// Usamos el nombre del modelo personalizado Perfil 
        model = Perfil
        
        # Definimos los campos
        fields = ('username', 'email')

