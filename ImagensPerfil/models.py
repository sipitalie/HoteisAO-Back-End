from django.db import models
from django.conf import settings
from alojamento.models import Alojamento
from quartos.models import Quarto


def uploud_image(instance, filename):
    return "{}{}".format(instance.id,filename)

class Gallery(models.Model):
    #bedroom photo gallery
    quarto=models.ForeignKey(Quarto, on_delete=models.CASCADE)
    file=models.ImageField(upload_to=uploud_image)
    def __str__(self):
        return  str(self.file)#self.img.url

    