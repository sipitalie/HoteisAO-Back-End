from promocoes.models import Promocao
from .serializer import PromocaoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class PromotionList(APIView):
    """
    List all promotions, or create a new promotion.
    """
    def get(self, request, format=None): #function to list all promotions
        promotions = Promocao.objects.all()
        serializer = PromocaoSerializer(promotions, many=True)
        return Response(serializer.data)


    #apermission_classes=(IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)
    def post(self, request, format=None): #function to create a promotion
        serializer= PromocaoSerializer(data=request.data)
        if serializer.is_valid():
            Promocao=serializer.save()
            data={}
            data["Response"]="registro salvo com sucesso"
            data["data"]=serializer.data
            return Response(data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PromoListHotelPage(APIView):
    """
    List all Promo HotelPage
    """
    def get(self, request,hotel_owner_id,format=None): #function to list all Events
        print(type(hotel_owner_id))
        promo=Promocao.objects.filter(hotel=hotel_owner_id)
        serializer = PromocaoSerializer(promo, many=True)
        return Response(serializer.data)


        
class PromotionDetail(APIView):
    """
    Retrieve, update or delete a promotion instance.
    """
    
    def get_object(self, pk):
        try:
            return Promocao.objects.get(pk=pk)
        except Promocao.DoesNotExist:
            raise Http404
    

    def get(self, request, pk, format=None): #fncution to Retrieve a promotion instance
        promotion = self.get_object(pk)
        serializer = PromocaoSerializer(promotion)
        return Response(serializer.data)

    #permission_classes=(IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)
    def put(self, request, pk, format=None): #fncution to update a promotion instance
       
        promotion = self.get_object(pk)
        serializer = PromocaoSerializer(promotion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None): #fncution to delete a promotion instance
        
        promotion = self.get_object(pk)
        promotion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
