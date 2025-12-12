# apps/usuarios/urls.py
from django.urls import path
from . import views

# Define el namespace (nombre de la aplicación) para usarlo en las plantillas: {% url 'usuarios:registro' %}
app_name = 'usuarios' 

urlpatterns = [
    # Esta URL debe coincidir con el nombre de la vista que maneja el registro
    # Asumo que la vista se llama 'registro' en views.py de esta app
    path('registro/', views.registro_usuario, name='registro'), 
]