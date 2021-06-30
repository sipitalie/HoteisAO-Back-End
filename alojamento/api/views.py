from account.models import Account
from alojamento.models import Alojamento, ContactsSchedule, AlojamentoViewsCount
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializer import AlojamentoSerializer, AlojamentoContactsScheduleSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth import authenticate
from django.http import Http404
from rest_framework import filters
#from rest_framework.authtoken.models import Token
from rest_framework.generics import UpdateAPIView,ListAPIView
from rest_framework import status





class AlojamentoViewsContactsSchedule(APIView):
   
    def get_object(self, idhotel):
        try:
            return ContactsSchedule.objects.get(hotel=idhotel)
        except ContactsSchedule.DoesNotExist:
            raise Http404         

    def get(self, request, idhotel, format=None): 
        data={}
        contactos = self.get_object(idhotel)
        serializer =  AlojamentoContactsScheduleSerializer(contactos)
        return Response(serializer.data)

    def post(self, request):
        data ={}
        body= request.data
        serializer= AlojamentoContactsScheduleSerializer(data=request.data)
        if serializer.is_valid():
            Alojamento=serializer.save()
            data['response']='cadastro feito com sucesso'
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data=serializer.errors
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, idhotel, format=None): #function to update a bedroom instance
        contactos = self.get_object(idhotel)
        serializer =  AlojamentoContactsScheduleSerializer(contactos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, idhotel, format=None): #function to delete a bedroom instance
        contactos = self.get_object(idhotel)
        contactos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET',])
def alojamentos(request):
    """
    função para listar todos os hotel
    """
    if request.method == 'GET':
        alojamentos = Alojamento.objects.all()
        serializer = AlojamentoSerializer(alojamentos,many=True)
        return Response(serializer.data)



@api_view(['GET',])
def alojamentos_owner_get(request,pk):
    """
    função para listar todos os hotel de um utilizador
    """
    if request.method == 'GET':
        alojamentos = Alojamento.objects.filter(owner=pk)
        
        serializer = AlojamentoSerializer(alojamentos,many=True)
        return Response(serializer.data)

@api_view(['GET',])
def alojamento_views_create(request,pk):
 
    if request.method == 'GET':
        data={
            'hotel':pk,
            'user_view_ip':request.META['REMOTE_ADDR'],
        }
        print(data)
    
        #serializer=AlojamentoViewsCountSerializer(data=data)
        #serializer2=AlojamentoViewsCount(hotel=pk, user_view_ip=request.META['REMOTE_ADDR'])
        #print(serializer2, serializer,serializer.is_valid())
        #serializer2=AlojamentoViewsCount(hotel=pk, user_view_ip=request.META['REMOTE_ADDR'],)
        #serializer.save()
        #if serializer.is_valid():
        #    print(serializer)
            #AlojamentoViewsCount=serializer.save()
        #    data['response']='cadastro feito com sucesso'
        #    return Response(data, status=status.HTTP_201_CREATED)
        return Response({'data':'ola'})
        #return Response(serializer.data)

class AlojamentoListView(ListAPIView):
    queryset = Alojamento.objects.all()
    serializer_class = AlojamentoSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['nome', 'Type_Alojamento','cidade']
    #ordering = ['nome']

class AlojamentoCreate(APIView):

    def post(self, request):
        data ={}
        body= request.data
        
        serializer=AlojamentoSerializer(data=request.data)
       
        if serializer.is_valid():
            Alojamento=serializer.save()
            data['response']='cadastro feito com sucesso'
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data=serializer.errors
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
    
    
class AlojamentoDetail(APIView):
    def get_object(self, pk):
        try:
            return Alojamento.objects.get(pk=pk)
        except Alojamento.DoesNotExist:
            raise Http404         

    def get(self, request, pk, format=None): 
        data={}
        alojamento = self.get_object(pk)
        serializer = AlojamentoSerializer(alojamento)
        return Response(serializer.data)

    def post(self, request):
        data ={}
        body= request.data
        serializer=AlojamentoSerializer(data=request.data)
        if serializer.is_valid():
            Alojamento=serializer.save()
            data['response']='cadastro feito com sucesso'
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data=serializer.errors
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None): #function to update a bedroom instance
        alojamento = self.get_object(pk)
        serializer = AlojamentoSerializer(alojamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, pk, format=None): #function to delete a bedroom instance
        alojamento = self.get_object(pk)
        alojamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)