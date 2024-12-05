from rest_framework import serializers
from .models import Anuncio
from casa.serializer import SerializadorCasa


class SerializadorAnuncio(serializers.ModelSerializer):
    casa = SerializadorCasa()
    class Meta:
        model = Anuncio
        fields = '__all__'  # Ou especifique campos, como: ['id', 'titulo', 'descricao', 'preco', 'veiculo']
