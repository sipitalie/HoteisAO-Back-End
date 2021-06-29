from django.urls import path 
from django.conf.urls.static import static
from django.conf import settings
#from rest_framework.urlpatterns import format_suffix_patterns
from .views import(
    alojamentos,
    alojamento_views_create,
    alojamentos_owner_get,
    AlojamentoCreate,
    AlojamentoDetail,
    AlojamentoListView,
    AlojamentoViewsContactsSchedule
   )
    
urlpatterns = [
    path('alojamentos/',  alojamentos),
    path('treading/<int:pk>/',  alojamento_views_create),
    path('alojamentosOwner/<int:pk>/',  alojamentos_owner_get),
    
    path('alojamentos/<int:pk>/',AlojamentoDetail.as_view()),
    path('alojamentos/register', AlojamentoCreate.as_view(), name="register"),
    path('filter', AlojamentoListView.as_view()) ,
    path('contactos/<int:idhotel>/', AlojamentoViewsContactsSchedule.as_view()) ,
    path('contactos/', AlojamentoViewsContactsSchedule.as_view()) ,
    
]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns = format_suffix_patterns(urlpatterns)


