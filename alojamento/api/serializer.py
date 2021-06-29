from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from alojamento.models import Alojamento, AlojamentoViewsCount, ContactsSchedule



class AlojamentoSerializer(serializers.ModelSerializer):
    #imgs=ImgPerfilSerializer()
    class Meta:
        model = Alojamento
        fields='__all__'
        #fields =['owner','nome', 'Type_Alojamento',
        #        'Estrela', 'pais', 'Provincia', 
        #         'latitude', 'longitude']

    #def create(self, validated_data):
        #imgs=validated_data['imgs']
       # del validated_data['imgs']
        # alojamento= Alojamento.objects.create(**validated_data)
        #end=Imagens.objects.create(**imgs)
        #alojamento.imgs=end
        #return alojamento
class AlojamentoContactsScheduleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =ContactsSchedule
        fields='__all__'