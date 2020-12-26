from django.db import models
from django.conf import settings
from alojamento.models import Alojamento

# Create your models here.

class Reclamacoes(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Hotel=models.ForeignKey(Alojamento, on_delete=models.CASCADE)
    content=models.TextField()
    data=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    