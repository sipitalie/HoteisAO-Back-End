from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
#from ImagensPerfil.models import Imagens

#tipo
Type=(('Hotel','Hotel'),
    ('Apart-hotel','Apart-hotel'),
    ('Residencial','Residencial'),
    ('Pensão','Pensão'),
    ('Lodge','Lodge'),
    ('Resort','Resort'),
    ('Outros', 'Outros')
)
#E quanto às classificações?
estrela=(
    (1, '1 estrela'),
    (2,'2 estrelas'),
    (3,'3 estrelas'),
    (4,'4 estrelas'),
    (5,' 5 estrelas'),
)
def uploud_image(instance, filename):
    return "{}{}".format(instance.nome,filename)
class Alojamento (models.Model):
    owner=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome=models.CharField(max_length=50)
    Type_Alojamento=models.CharField(choices=Type, max_length=20)
    Estrela=models.IntegerField(choices=estrela)
    Aprovado=models.BooleanField(default=True)
    data=models.DateField(auto_now_add=True)
    pais=models.CharField(max_length=50)
    Provincia=models.CharField(max_length=150)
    cidade=models.CharField(max_length=50)
    linha=models.CharField(max_length=150)
    latitude=models.FloatField()
    longitude=models.FloatField()
    foto=models.ImageField(upload_to=uploud_image,null=True, blank=True)
    
   
    def __str__(self):
        return self.nome

class ContactsSchedule(models.Model):#contactos e horarios de serviços
    hotel=models.OneToOneField(Alojamento, on_delete=models.CASCADE)
    phone=models.CharField(max_length=15)
    email=models.EmailField(max_length=254)
    whatsApp=models.CharField(max_length=15, null=True, blank=True)
    LinkedIn=models.CharField(max_length=254, null=True, blank=True)
    rec_in=models.TimeField(auto_now=False, auto_now_add=False)
    rec_out=models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.email

@receiver(post_save, sender=Alojamento)
def save_cantactsSchedule(sender, instance, **kwargs):
    ...


class AlojamentoViewsCount(models.Model):
    hotel=models.ForeignKey(Alojamento, on_delete=models.CASCADE)
    user_view_ip=models.CharField(max_length=20, null=True, blank=True)
    data_view=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.id

    