from django import forms
from .models import Transação, Mesas, Cadeiras

class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transação
        fields = '__all__'
        widgets = {
            'data_aluguel': forms.DateInput(attrs={'type': 'date'}),
            'data_devolução': forms.DateInput(attrs={'type': 'date'}),
        }

class MesasForm(forms.ModelForm):
    class Meta:
        model = Mesas
        fields = '__all__'


class CadeirasForm(forms.ModelForm):
    class Meta:
        model = Cadeiras
        fields = '__all__'

class CadastrarMesasCadeirasForm(forms.Form):
    quantidade_mesas = forms.IntegerField()
    quantidade_cadeiras = forms.IntegerField()
