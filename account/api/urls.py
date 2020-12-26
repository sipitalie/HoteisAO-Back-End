from django.urls import path 
from .views import (
    listaUser,
    login_token_view,
    cadastro_view,
    update_account_view,
    account_Propertie_view,
    ChangePassword_Views,
    ResetPassword_view,
    #ResetPassword_confirm_view,
    )
#from rest_framework.authtoken import views

    
urlpatterns = [
    path('',  listaUser),
    path('login/',login_token_view.as_view() , name="login"),
    path('properties/', account_Propertie_view , name="properties"),
    path('properties/update/',update_account_view , name="update"),
    path('change_password/', ChangePassword_Views.as_view() , name="change_password"),
    path('Reset_Password/',  ResetPassword_view, name="Reset_Password"),
    #path('Reset_Password_confirm/',  ResetPassword_confirm_view, name="Reset_Password_confirm"),
    path('register/',cadastro_view, name="register"),
    
      
]