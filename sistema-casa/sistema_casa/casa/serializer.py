from casa.models import Casa
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

class SerializadorCasa(serializers.ModelSerializer):
    foto = Base64ImageField(required=False, represent_in_base64=True)

    class Meta:
        model = Casa
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['num_quartos'] = instance.get_num_quartos_display()
        representation['num_banheiros'] = instance.get_num_banheiros_display()
        representation['status'] = instance.get_status_display()
        representation['tipo'] = instance.get_tipo_display()
        return representation
    
    #Antes de passar os dados validados para o método update original, ele remove o campo usuario de validated_data. Isso garante que, caso o campo usuario seja enviado na requisição, ele não seja usado para atualizar o modelo Casa.
    def update(self, instance, validated_data):
        validated_data.pop('usuario', None) 
        return super().update(instance, validated_data)