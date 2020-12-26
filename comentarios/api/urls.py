from django.urls import path 
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ComentarioList, ComentarioDetail
    
urlpatterns = [
    path('comentario/', ComentarioList.as_view()),
    path('comentario/<int:pk>/',ComentarioDetail.as_view()),
     
]
urlpatterns = format_suffix_patterns(urlpatterns)
