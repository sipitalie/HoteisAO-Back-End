from rest_framework import serializers
from seguir.models import Seguir

class SeguirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seguir
        fields =('User_id','hotel_id', 'data')
        
