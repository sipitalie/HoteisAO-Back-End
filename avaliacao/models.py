from django.db import models
from django.conf import settings
from alojamento.models import Alojamento
# Create your models here.

class Avaliacao (models.Model):
    User=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nota=models.FloatField()
    hotel=models.ForeignKey(Alojamento, on_delete=models.CASCADE)
    data=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.User.username
