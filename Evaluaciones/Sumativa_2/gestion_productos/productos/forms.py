       # productos/forms.py
from django import forms
from .models import Producto, Caracteristica
 
class ProductoForm(forms.ModelForm):
    caracteristicas = forms.ModelMultipleChoiceField(
        queryset=Caracteristica.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
 
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'precio', 'marca', 'categoria', 'caracteristicas']