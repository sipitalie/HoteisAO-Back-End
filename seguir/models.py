from django.db import models
from django.conf import settings
from alojamento.models import Alojamento

# Create your models here.
class Seguir (models.Model):
    User_id=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hotel_id=models.ForeignKey(Alojamento, on_delete=models.CASCADE)
    data=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)


    #def get_seguir(self):
    #    return (self.User_id.username, self.hotel_id, self.id)

