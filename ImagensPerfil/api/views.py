from ImagensPerfil.models import Gallery
from .serializer import ImgSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404

class GetImgGallery(APIView):
    def get(self, request, quarto_id): 
        Img = Gallery.objects.filter(quarto=quarto_id)
        #Img = Gallery.objects.all()#.select_related('quarto')
        serializer = ImgSerializer(Img , many=True)
        return Response(serializer.data)
class UploadImg(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=ImgSerializer(data=request.data)
        if serializer.is_valid():
            Gallery=serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ImgDelete(APIView):
    def delete(self, request, format=None):
        print(request.data)
        serializer=ImgSerializer(data=request.data)
        if serializer.is_valid():
            Gallery=serializer.delete()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
