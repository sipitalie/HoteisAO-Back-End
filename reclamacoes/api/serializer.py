from rest_framework import serializers
from reclamacoes.models import Reclamacoes

class ReclamacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclamacoes
        fields ='__all__'
