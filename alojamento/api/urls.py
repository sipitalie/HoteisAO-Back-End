from django.urls import path 
from django.conf.urls.static import static
from django.conf import settings
#from rest_framework.urlpatterns import format_suffix_patterns
from .views import alojamentos, AlojamentoCreate, AlojamentoDetail, AlojamentoListView
    
urlpatterns = [
    path('alojamentos/',  alojamentos),
    path('alojamentos/<int:pk>/',AlojamentoDetail.as_view()),
    path('alojamentos/register', AlojamentoCreate.as_view(), name="register"),
    path('filter', AlojamentoListView.as_view()) ,
    
]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns = format_suffix_patterns(urlpatterns)


