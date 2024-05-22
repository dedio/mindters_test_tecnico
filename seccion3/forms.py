# Defina un formulario en Django para un modelo Usuario 
# que tenga campos para el nombre de usuario y el correo electrónico.
# Asegúrese de que el correo electrónico sea válido.

from django import forms
from .models import Usuario
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("Email inválido")
        return correo_electronico
