from django import forms
from apps.entradas.models import Entrada



class FormEntrada (forms.ModelForm):

    class Meta:
        model = Entrada

        fields = (
            'fecha',
            'cantidad',
            'valor',
            'producto',
        )

        labels = {
            'fecha' : 'Ingrese la fecha',
            'cantidad' : 'Ingrese la cantidad',
            'valor' : 'Ingrese un valor',
            'producto' : 'Seleccione su producto'
        }

        widgets = {
            'fecha' : forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad' : forms.TextInput(attrs={'class': 'form-control'}),
            'valor' : forms.TextInput(attrs={'class': 'form-control'}),
            'producto' : forms.Select(attrs={'class': 'form-control'}),
        }