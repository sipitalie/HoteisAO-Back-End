from rest_framework import serializers
from promocoes.models import Promocao

class PromocaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocao
        fields ='__all__'
