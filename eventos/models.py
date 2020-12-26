from django.db import models
from alojamento.models import Alojamento
from django.conf import settings


class Evento(models.Model):
    owner=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hotel_owner=models.ForeignKey(Alojamento, on_delete=models.CASCADE)
    title=models.CharField(max_length=50, blank=True, default='')
    content=models.TextField(max_length=1000)
    data=models.DateField(auto_now_add=True)
    data_do_evento=models.DateField(auto_now_add=False)
    #imegen=models.ImageField()

    def __str__(self):
        return self.title


class Eventolembret(models.Model):
    """
    model para guardar o email de todos os usuario que clicarem em lembret no evento 
    """
    evento=models.ForeignKey(Evento, on_delete=models.CASCADE)
    data=models.DateField(auto_now_add=True)
    UserLembrete = models.ManyToManyField(settings.AUTH_USER_MODEL)
    
    def __str__(self):
        return self.evento.title
