from django.db.models.signals import post_save
from django.dispatch import receiver

from promocoes.models import Promocao
from eventos.models import Evento

@receiver(post_save, sender=Promocao)
def promotion_notification_created(sender, instance, **kwargs):
    #notificação de promoção criada
    data={}
    data['hotel']=instance.hotel
    data['quartos_em_prom']=instance.quartos_em_prom
    data['new_preco']=instance.new_preco
    data['data']=instance.data
    data['init_data']=instance.init_data
    print("uma promoção foi feita", data)