from django.db import models
from django.conf import settings
from alojamento.models import Alojamento

# Create your models here.
class Comentario(models.Model):
    owner=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hotel=models.ForeignKey(Alojamento,on_delete=models.CASCADE)
    content=models.TextField()
    data=models.DateTimeField(auto_now_add=True)
    aprovado=models.BooleanField(default=True)

    def __str__(self):
        return self.owner.username