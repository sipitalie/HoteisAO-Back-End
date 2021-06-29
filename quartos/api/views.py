from quartos.models import Quarto
from .serializer import QuartoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class QuartoList(APIView):
    """
    List all bedrooms a hotel.
    """
    def get_owner(self, hotel_owner_id):
        try:
            return Quarto.objects.filter(hotel_owner=hotel_owner_id)
        except Quarto.DoesNotExist:
            raise Http404
    def get(self, request,hotel_owner_id, format=None): #function to list all bedrooms a hotel
        #hotel_owner=request.data['hotel_owner']
        bedrooms=self.get_owner(hotel_owner_id)
        serializer = QuartoSerializer(bedrooms, many=True)
        #print(serializer.data)
        return Response(serializer.data)

class QuartoCreate(APIView):
    """
    Class to create a new bedroom.
    """
    permission_classes=(IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def post(self, request, format=None): #function to create a bedroom
        #print(request.data)
        serializer=QuartoSerializer(data=request.data)
        if serializer.is_valid():
            Quarto=serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class QuartoDetail(APIView):
    """
    class to update or delete an bedroom instance.
    """
    permission_classes=(IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def get_object(self, pk):
        try:
            return Quarto.objects.get(pk=pk)
        except Quarto.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None): 
        bedrooms = self.get_object(pk)
        serializer = QuartoSerializer(bedrooms)
        return Response(serializer.data)

    def put(self, request, pk, format=None): #function to update a bedroom instance
        bedroom = self.get_object(pk)
        serializer = QuartoSerializer(bedroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None): #function to delete a bedroom instance
        bedroom = self.get_object(pk)
        bedroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



"""    
class QuartoDetail(APIView):
    "
    classe to Retrieve a bedroom instance
    "
    def get_object(self, pk):
        try:
            return Quarto.objects.get(pk=pk)
        except Quarto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None): 
        bedrooms = self.get_object(pk)
        serializer = QuartoSerializer(bedrooms)
        return Response(serializer.data)
"""