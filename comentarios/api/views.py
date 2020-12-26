from comentarios.models import Comentario
from .serializer import ComentarioSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



class ComentarioList(APIView):
    """
    List all Comments, or create a new Comment.
    """
    def get(self, request, format=None): #function to list all comments
        comentario = Comentario.objects.all()
        serializer = ComentarioSerializer(comentario, many=True)
        return Response(serializer.data)


    #apermission_classes=(IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)
    def post(self, request, format=None): #function to create a comment
        serializer=ComentarioSerializer(data=request.data)
        if serializer.is_valid():
            Comentario=serializer.save()
            data={}
            data["Response"]="registro salvo com sucesso"
            return Response(data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ComentarioDetail(APIView):
    """
    Retrieve, update or delete a comment instance.
    """
    
    def get_object(self, pk):
        try:
            return Comentario.objects.get(pk=pk)
        except Comentario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None): #fncution to Retrieve a comment instance
        comentario = self.get_object(pk)
        serializer = ComentarioSerializer(comentario)
        return Response(serializer.data)

    #permission_classes=(IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)
    def put(self, request, pk, format=None): #fncution to update a comment instance
        comentario = self.get_object(pk)
        serializer = ComentarioSerializer(comentario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None): #fncution to delete a comment instance
        comentario = self.get_object(pk)
        comentario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
