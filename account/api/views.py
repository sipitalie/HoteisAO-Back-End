from account.models import Account
from alojamento.models import Alojamento
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializer import (UserSrializer,
     RegisterSerializer, 
     AccountPropertiesSerializer, 
     ChangePasswordSerializer, 
     PasswordResetSerializer,
     #PasswordResetConfirmSerializer,
     )          
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.generics import UpdateAPIView
from rest_framework import status
from django.http import Http404
from rest_framework.authentication import TokenAuthentication

@api_view(['GET',])
def listaUser(request):
    
    if request.method == 'GET':
        account = Account.objects.all()
        serializer = UserSrializer(account, many=True)

        return Response(serializer.data)


@api_view(['POST',])
@permission_classes([]) 
@authentication_classes([])
def cadastro_view(request):
    if request.method=='POST':
        data={}
        email=request.data.get('email','0')
        if validate_email(email) != None:
            data['error_message']='O email já esta a ser utilisado'
            data['response']='Error'
            return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        username=request.data.get('username','0')
      
        if validate_username(username) !=None:
            data['error_message']='O nome ja esta a ser utilizado'
            data['response']='error'
            return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE )
        
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            account=serializer.save()
            data['response']='cadastro feito com sucesso'
            data['id']=account.id
            data['email']=account.email
            data['username']=account.username
            data['token']=Token.objects.get(user=account).key
            return Response(data, status=status.HTTP_201_CREATED)
            
        else:
            data=serializer.errors
            return Response(data,status=status.HTTP_400_BAD_REQUEST)


class login_token_view(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        data ={}
        body= request.data
        email=body['username']
        password=body['password']
        account=authenticate(email=body['username'], password=body['password'])

        if account:
            try:
                token=Token.objects.get(user=account)
            except Token.DoesNotExist:
                token=Token.objects.create(user=account)
    
            data['response']='sucessfully'
            data['id']=account.pk
            data['email']=email
            data['token']=token.key
            data['isAdmin']=Alojamento.objects.filter(owner=account.pk).values('id')
            return Response(data, status=status.HTTP_200_OK)
        else:
            data['response']='Error'
            data['error_mensage']='invalid credential'
            return Response(data,status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST',])
@permission_classes([]) 
@authentication_classes([])
def dos_account_exist_viw(request):
    if request.method == 'GET':
        email=request.GET['email'].lower()
        data={}
        try:
            accont=Account.objects.get(email=email)
            data['response']=email
        except Account.DoesNotExist:
            data['response']="Account dos not exit"
        return Response(data)


class ChangePassword_Views(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    serializer_class = ChangePasswordSerializer
    model = Account
    permission_classes=(IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_object(self, queryst=None):
        obj= self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object=self.get_object()
        serializer= self.get_serializer(data=request.data)
    
        if serializer.is_valid():
            # chek old_password

            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password":["senha incorreta"]},status=status.HTTP_400_BAD_REQUEST)

            # confirmação da nova palavra passe
            new_password= serializer.data.get("new_password")
            confirm_new_password=serializer.data.get("confirm_new_password")
            if new_password != confirm_new_password:
                return Response({"new_password":["novas senhas devem corresponder"]},status=status.HTTP_400_BAD_REQUEST)
   
            #set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({"response":"successfully changed password"},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def account_Propertie_view(request): 
    try:
        account=request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer=AccountPropertiesSerializer(account)
        return Response(serializer.data)

"""
d
"""
@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def update_account_view(request): 
    try:
        account=request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer=AccountPropertiesSerializer(account, data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data['response']='Account update sucess'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST',])
@permission_classes([]) 
@authentication_classes([])
def ResetPassword_view(request):
    if request.method=='POST':
        data={}
        serializer= PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email= serializer.data['email']
            if validate_email(email) == None:
                data['error_message']='O email não faz parte da lista dos nossos usuarios.'
                data['response']='Error'
                return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                data['message']='Mais instruções serão enviadas para o email, verifique sua caixa de entradas.'
                data['response']=email
                return Response(data, status=status.HTTP_200_OK)
        else:
            data['error_message']="digite um email"
            data['response']='error'
            return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)

    #email=request.data
    #serializer = self.get_serializer(data=request.data)
    #serializer=PasswordResetSerializer(data=request.data)
    #return Response({'message': 'ola', 'email':email})
"""
@api_view(['POST',])
@permission_classes([]) 
@authentication_classes([])
def ResetPassword_confirm_view(request):
    if request.method=='POST':
        data={}
        #new_password= serializer.data.get("new_password")
        #confirm_new_password=serializer.data.get("confirm_new_password")
        serializer= PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
        #if new_password != confirm_new_password:
            user.set_password(serializer.validated_data['new_password'])
            user.save()
        #return response.NoContent()
            print(serializer.data)
            data['data']=serializer.data
            return Response(data)
        else:
            return Response(data, status=status.HTTP_406_NOT_ACCEPTABLE)



"""
    
"""
A função validate_email
verifica se ja existe um email cadastrado. 
"""                
def validate_email(email):
    account= None
    try:
        account=Account.objects.get(email=email)
    except Account.DoesNotExist:
        return None
    if account != None:
        return email

"""
A função validate_email
verifica se ja existe um username  cadastrado. 
""" 
def validate_username(username):
    account= None
    try:
        account=Account.objects.get(username=username)
    except Account.DoesNotExist:
        return None
    if account != None:
        return username

"""
serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = user_services.get_user_by_email(serializer.data['email'])
        if user:
            services.send_password_reset_mail(user)
"""