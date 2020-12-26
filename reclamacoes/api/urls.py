from django.urls import path 
from .views import ReclamacaoList,ReclamacaoDetail
    
urlpatterns = [
    path('reclamacoes/', ReclamacaoList.as_view()),
    path('reclamacao/<int:pk>/',ReclamacaoDetail.as_view()),
     
]