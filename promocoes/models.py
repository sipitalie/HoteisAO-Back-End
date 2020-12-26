from django.db import models
from alojamento.models import Alojamento
from quartos.models import Quarto
from django.db.models.signals import post_save


class Promocao(models.Model):
    hotel=models.ForeignKey(Alojamento, on_delete=models.CASCADE)
    quartos_em_prom=models.ManyToManyField(Quarto)
    new_preco=models.FloatField()
    data=models.DateField(auto_now_add=True)
    init_data=models.DateField(blank=True, null=True)
    valid_data=models.DateField()

    def __str__(self):
        return self.hotel.nome
    

