from django.urls import path 
from django.conf.urls.static import static
from django.conf import settings
from .views import GetImgGallery, UploadImg
    
urlpatterns = [
    #path('gallery/<int:pk>/', GetImgGallery.as_view()),
    path('gallery/<int:quarto_id>/', GetImgGallery.as_view()),
    path('upload/gallery', UploadImg.as_view()), 
]