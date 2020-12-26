from reclamacoes.models import Reclamacoes
from .serializer import ReclamacaoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



class ReclamacaoList(APIView):

    def get_hotel_claims(self, hotel):
        try:
            return Reclamacoes.objects.filter(Hotel=hotel)
        except Reclamacoes.DoesNotExist:
            raise Http404

    def get(self, request, format=None): #function to list all comments
        hotel=request.data['Hotel']
        reclamacao = self.get_hotel_claims(hotel)
        serializer = ReclamacaoSerializer(reclamacao, many=True)
        return Response(serializer.data)

    def post(self, request, format=None): #function to create a comment
        serializer=ReclamacaoSerializer(data=request.data)
        if serializer.is_valid():
            Comentario=serializer.save()
            data={}
            data["Response"]="registro salvo com sucesso"
            return Response(data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ReclamacaoDetail(APIView):
    """
    Retrieve, update or delete a comment instance.
    """
    
    def get_object(self, pk):
        try:
            return Reclamacoes.objects.get(pk=pk)
        except Reclamacoes.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None): #fncution to Retrieve a comment instance
        reclamacao = self.get_object(pk)
        serializer = ReclamacaoSerializer(reclamacao)
        return Response(serializer.data)

    #permission_classes=(IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)
    def put(self, request, pk, format=None): #fncution to update a comment instance
        reclamacao = self.get_object(pk)
        serializer = ReclamacaoSerializer(reclamacao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None): #fncution to delete a comment instance
        reclamacao = self.get_object(pk)
        reclamacao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
