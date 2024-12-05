from django import forms
from casa.models import Casa

class FormularioCasa (forms.ModelForm):
    
    class Meta:
        model = Casa
        exclude = []