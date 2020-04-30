from django import forms
from .models import Usuarios

class UsuariosForm(forms.ModelForm):

    class Meta:
        model = Usuarios
        fields = ('nombre_usuario','passwd_usuario','id_tipo_usuario','id_estado_usuario',)