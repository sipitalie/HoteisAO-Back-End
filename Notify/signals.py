from django.core.mail import send_mail, send_mass_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


from promocoes.models import Promocao
from eventos.models import Evento
from seguir.models import Seguir

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

@receiver(post_save, sender=Evento)
def event_notification_created(sender, instance, **kwargs):
    #notificação de Eventos criados 
    data={}
    data['hotel_owner']=instance.hotel_owner.nome
    data['title']=instance.title
    data['content']=instance.content
    data['data']=instance.data
    data['data_do_evento']=instance.data_do_evento
    content=f"{data['content']},data do Evento:{data['data_do_evento']}"
    Assunto=f"{data['title']}"

    Seguidores=Seguir.objects.select_related('User_id').filter(hotel_id=instance.hotel_owner)
    
    listEmais=[]
    listmess=[]

    for seguidor in  Seguidores:
            listEmais.append(seguidor.User_id.email)
            for i in listEmais:
                
                listmess.append((Assunto,content, 'hotel_me@gmail.com',[i]))

    datatuple=tuple(listmess)
   
    send_mass_mail(datatuple, fail_silently=False)
    
    print("um evento foi criado",data)


   

    
    """
    follow = []
    for seguidor in  Seguidores:
        follow.append({'seguidor':{"username":seguidor.User_id.username,"email":seguidor.User_id.email}})
    """