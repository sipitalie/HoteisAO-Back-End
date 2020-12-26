from django.urls import path 
from .views import FollowOnFollow,ASeguir,SeguidoresList, ASeguirDetail
    
urlpatterns = [
    path('follow/',FollowOnFollow.as_view()),
    path('follow/user/<int:User_id>',ASeguir.as_view()), 
    path('follow/user/<int:User_id>/<int:hotel_id>/',ASeguirDetail.as_view()), 
    path('followers/<int:hotel_id>', SeguidoresList.as_view()),
    path('onfollow/<int:User_id>/<int:hotel_id>/',FollowOnFollow.as_view()),      
]