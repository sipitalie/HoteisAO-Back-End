from ImagensPerfil.models import Gallery
from rest_framework.serializers import ModelSerializer 
from rest_framework import serializers
 
class ImgSerializer(ModelSerializer):
    file = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Gallery
        fields = '__all__'




        

