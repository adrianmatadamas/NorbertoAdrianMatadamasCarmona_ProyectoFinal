# clientes/forms.py
from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'email', 'telefono', 'direccion']
