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
        #print
        serializer = ImgSerializer(Img , many=True)
        return Response(serializer.data)
class UploadImg(APIView):
    def post(self, request, format=None):
        
        serializer=ImgSerializer(data=request.data)
        if serializer.is_valid():
            Gallery=serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ImgDelete(APIView):
    def get_object(self, pk):
        try:
            return Gallery.objects.get(pk=pk)
        except Gallery.DoesNotExist:
            raise Http404
    def delete(self,request,pk,format=None):
        gallery = self.get_object(pk)
        gallery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
