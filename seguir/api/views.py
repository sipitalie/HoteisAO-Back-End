from seguir.models import Seguir
from account.models import Account
from alojamento.models import Alojamento
from .serializer import SeguirSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

#User_id=User_id, hotel_id=hotel_id
class ASeguirDetail(APIView):
    def get_object(self, User_id, hotel_id):
        try:
            return Seguir.objects.filter(User_id=User_id, hotel_id=hotel_id)
        except Seguir.DoesNotExist:
            raise Http404
    def get(self, request, User_id, hotel_id, format=None): 
        a_seguir=self.get_object(User_id,hotel_id)
        serializer = SeguirSerializer(a_seguir,  many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)



class ASeguir(APIView):
    def get_object(self, User_id):
        try:
            return Seguir.objects.filter(User_id=User_id)
        except Seguir.DoesNotExist:
            raise Http404
    def get(self, request, User_id, format=None): 
        a_seguir=self.get_object(User_id)
        serializer = SeguirSerializer(a_seguir,  many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    


class SeguidoresList(APIView):
           
    def get_object(self, hotel_id):
        try:
            return Seguir.objects.filter(hotel_id=hotel_id)
        except Seguir.DoesNotExist:
            raise Http404
    def get(self, request, hotel_id, format=None): 
        data={} 
        a_seguir=self.get_object(hotel_id)
        serializer = SeguirSerializer(a_seguir,  many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class FollowOnFollow(APIView):

    def validate_hotel(self, hotel_id):
        alojamento= None
        try:
            alojamento=Alojamento.objects.get(pk=hotel_id)
        except Alojamento.DoesNotExist:
            return None
        if alojamento != None:
            return True
    def validate_User(self, User_id):
        account= None
        try:
            account=Account.objects.get(pk=User_id)
        except Account.DoesNotExist:
            return None
        if account != None:
            return True
    def validate_to_follow(self, User_id, hotel_id):
        """
        A função validate_to_follow verifica se um determinado usuário
        já segui  um determinado hotel.
        """ 
        a_seguir = None
        data={}
        try:
            a_seguir=Seguir.objects.filter(User_id=User_id, hotel_id=hotel_id)
            #a_seguir=Seguir.objects.filter(User_id=User_id, hotel_id=hotel_id)[:1].get()
        except Seguir.DoesNotExist:
            return None

        print(a_seguir)
        if a_seguir !=None and len( a_seguir)!=0 :
            return a_seguir
    def get_seguidores_hotel(self, hotel):
        try:
            return Alojamento.objects.filter(Hotel=hotel)
        except Seguir.DoesNotExist:
            raise Http404

    

    def post(self, request,format=None):
        User_id=request.data['User_id']
        hotel_id=request.data['hotel_id']
        data={}       
        if self.validate_User(User_id) and self.validate_hotel(hotel_id)!=None:
            serializer=SeguirSerializer(data=request.data)
            if  self.validate_to_follow(User_id, hotel_id)==None:
                if serializer.is_valid():
                    serializer.save()
                    a_seguir=Seguir.objects.filter(User_id=User_id)
                    serializer = SeguirSerializer(a_seguir,  many=True)
                    return Response(serializer.data,status=status.HTTP_201_CREATED)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            else:
                if serializer.is_valid():
                    return Response(status=status.HTTP_204_NO_CONTENT)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                #id_seguir=self.validate_to_follow(User_id, hotel_id)              
                    #Seguir.delete()      
        data["Response"]="error"
        return Response(data,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, User_id,hotel_id,format=None): 
        data={}
        print(User_id,hotel_id,)
        #User_id=request.data['User_id']
        #hotel_id=request.data['hotel_id']
        if self.validate_User(User_id) and self.validate_hotel(hotel_id)!=None:
            if  self.validate_to_follow(User_id, hotel_id)!=None:
                self.validate_to_follow(User_id, hotel_id).delete()
                return Response(status=status.HTTP_204_NO_CONTENT) 
            else:
                data["Response"]="error"
                return Response(data,status=status.HTTP_400_BAD_REQUEST)

"""
class OnFollow(APIView):
    
    def validate_hotel(self, hotel_id):
        alojamento= None
        try:
            alojamento=Alojamento.objects.get(pk=hotel_id)
        except Alojamento.DoesNotExist:
            return None
        if alojamento != None:
            return True
    def validate_User(self, User_id):
        account= None
        try:
            account=Account.objects.get(pk=User_id)
        except Account.DoesNotExist:
            return None
        if account != None:
            return True
    def validate_to_follow(self, User_id, hotel_id):
        
       # A função validate_to_follow verifica se um determinado usuário
        #já segui  um determinado hotel.
         
        a_seguir = None
        data={}
        try:
            a_seguir=Seguir.objects.filter(User_id=User_id, hotel_id=hotel_id)
            #a_seguir=Seguir.objects.filter(User_id=User_id, hotel_id=hotel_id)[:1].get()
        except Seguir.DoesNotExist:
            return None

        print(a_seguir)
        if a_seguir !=None and len( a_seguir)!=0 :
            return a_seguir
    def get_seguidores_hotel(self, hotel):
        try:
            return Alojamento.objects.filter(Hotel=hotel)
        except Seguir.DoesNotExist:
            raise Http404

    

    def post(self, request,format=None):
        User_id=request.data['User_id']
        hotel_id=request.data['hotel_id']
        data={}       
        if self.validate_User(User_id) and self.validate_hotel(hotel_id)!=None:
            serializer=SeguirSerializer(data=request.data)
            if  self.validate_to_follow(User_id, hotel_id)==None:
                if serializer.is_valid():
                    serializer.save()
                    a_seguir=Seguir.objects.filter(User_id=User_id)
                    serializer = SeguirSerializer(a_seguir,  many=True)
                    return Response(serializer.data,status=status.HTTP_201_CREATED)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            else:
                if serializer.is_valid():
                    return Response(status=status.HTTP_204_NO_CONTENT)
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                #id_seguir=self.validate_to_follow(User_id, hotel_id)              
                    #Seguir.delete()      
        data["Response"]="error"
        return Response(data,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, User_id,hotel_id,format=None): 
        data={}
        print(User_id,hotel_id,)
        #User_id=request.data['User_id']
        #hotel_id=request.data['hotel_id']
        if self.validate_User(User_id) and self.validate_hotel(hotel_id)!=None:
            if  self.validate_to_follow(User_id, hotel_id)!=None:
                self.validate_to_follow(User_id, hotel_id).delete()
                return Response(status=status.HTTP_204_NO_CONTENT) 
            else:
                data["Response"]="error"
                return Response(data,status=status.HTTP_400_BAD_REQUEST)
"""
"""
class ReclamacaoDetail(APIView):
    
    #Retrieve, update or delete a comment instance.
    
    
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




        self.cli = {}
        self.id_maquinas = []
        
        for c in dados:
            if c[1] not in self.id_maquinas:
                self.id_maquinas.append(str(c[1]))
        
        for k, v in dados:
            self.cli.setdefault(k, []).append(v)
"""