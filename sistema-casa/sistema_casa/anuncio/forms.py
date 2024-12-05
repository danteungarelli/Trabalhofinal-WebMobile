from django import forms
from anuncio.models import Anuncio
from casa.models import Casa

class FormularioAnuncio(forms.ModelForm):
    casa = forms.ModelChoiceField(
        queryset=Casa.objects.all(), 
        label="Selecione a casa",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Anuncio
        fields = ['casa', 'descricao', 'preco','titulo']      
    
    def __init__(self, *args, **kwargs):
        usuario = kwargs.pop('usuario', None)  # Recebe o usuário logado
        super().__init__(*args, **kwargs)
        if usuario:
            self.fields['casa'].queryset = Casa.objects.filter(usuario=usuario)