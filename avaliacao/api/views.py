from avaliacao.models import Avaliacao
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializer import AvaliacaoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.generics import UpdateAPIView
from rest_framework import status
#from rest_framework.authtoken.models import Token

class AvaliacaoListtHotelPage(APIView):
    """
    List all evaluations HotelPage
    """
    def get_object(self, hotel_owner_id):
        try:
            return Avaliacao.objects.filter(hotel=hotel_owner_id)
        except Avaliacao.DoesNotExist:
            raise Http404

    def get(self,request, hotel_owner_id, format=None): #function to list all evaluetions
        print(type(hotel_owner_id))
        dados={}
        avaliacao = self.get_object(hotel_owner_id)
        serializer = AvaliacaoSerializer(avaliacao, many=True)
        dados=serializer.data
        #dados['id']=serializer.data['id']
        #dados['nota']=serializer.data['nota']
        #dados['data']=serializer.data['data']
        #dados['User']=serializer.data['User']
        #print(dados, type(dados))
        #dados['Nome']="ola"
        return Response(dados)

class AvaliacaoCreate(APIView):
    """
    Classe para avaliar um Hotel.
    """
    def validate_to_rank(self, User, hotel):
        """
        pt:
        A função validate_to_rank verifica se um determinado usuário
        já classificou um determinado hotel.
        """ 
        avaliacao = None
        data={}
        try:
            avaliacao=Avaliacao.objects.filter(User=User, hotel=hotel)
        except Avaliacao.DoesNotExist:
            return None
        if len(avaliacao) != 0:
            data["Error"]="Hotel ja classificado"
            return data
    def post(self, request):
        
        serializer=AvaliacaoSerializer(data=request.data)
    
        User=serializer.initial_data['User']
        hotel=serializer.initial_data['hotel']
        validate_user_hotel=self.validate_to_rank(User, hotel)
    
        if validate_user_hotel==None:
            if serializer.is_valid():
                Avaliacao=serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                data=serializer.errors
                return Response(data,status=status.HTTP_400_BAD_REQUEST)
        else:
            data=validate_user_hotel
            return Response(data, status=status.HTTP_405_METHOD_NOT_ALLOWED )

"""
def validate_to_rank(User, hotel):
    ""
    pt:
    A função validate_to_rank verifica se um determinado usuário
    já classificou um determinado hotel.

    en: 
    The validate_to_rank function checks whether a given
    user has already rated a given hotel.
    "" 
    avaliacao = None
    data={}
    try:
        avaliacao=Avaliacao.objects.filter(User=User, hotel=hotel)
    except Avaliacao.DoesNotExist:
        return None
    if len(avaliacao) != 0:
        data["Error"]="Hotel ja classificado"
        return data
    


#avaliacao=Avaliacao.objects.filter(User=User)
#avaliacao1=Avaliacao.objects.filter(hotel=hotel)
#print(avaliacao.query)
#print(len(avaliacao))
#print(avaliacao1.query)"

class AvaliacaoList(APIView):
    
    def get_evaluation_hotel(self, hotel):
        try:
            return  Avaliacao.objects.filter(hotel=hotel)
        except Avaliacao.DoesNotExist:
            raise Http404

    def get(self, request, format=None): 
        hotel=request.data['hotel']
        print(hotel)
        avaliacao = self.get_evaluation_hotel(hotel)
        serializer = AvaliacaoSerializer(avaliacao, many=True)
        return Response(serializer.data)
"""