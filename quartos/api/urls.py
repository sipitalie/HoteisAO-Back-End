from django.urls import path 
from rest_framework.urlpatterns import format_suffix_patterns
from .views import QuartoCreate, QuartoDetail, QuartoList
    
urlpatterns = [
    #path('quarto/', QuartoList.as_view()),
    path('quarto/hotelpage/<int:hotel_owner_id>/', QuartoList.as_view()),
    path('quarto/<int:pk>/',QuartoDetail.as_view()),
    path('quarto/register',QuartoCreate.as_view()),
     
]
urlpatterns = format_suffix_patterns(urlpatterns)