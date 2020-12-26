from django.urls import path 
from .views import AvaliacaoListtHotelPage, AvaliacaoCreate
    
urlpatterns = [
    #path('avaliacao',  AvaliacaoList.as_view()),
    path('avaliacao/hotelpage/<int:hotel_owner_id>/', AvaliacaoListtHotelPage.as_view()),
    path('avaliacao/register', AvaliacaoCreate.as_view(), name="register"),      
]