from django.db import models
from alojamento.models import Alojamento
from quartos.models import Quarto
from django.db.models.signals import post_save

"""
Caract== tipos de quarto por caracterização
"""
Caracterizacao=(
    ("Standard","Standard"),
    ("Master","Master"),
    ("Delux","Delux"),
    ("Outros","Outros")

)
type_quarto=(
    ("Quarto Solteiro","Quarto Solteiro"),
    ("Quarto Duplo","Quarto Duplo"),
    ("Quarto Casal","Quarto Casal"),
    ("Outros","Outros")
)
class Promocao(models.Model):
    hotel=models.ForeignKey(Alojamento, on_delete=models.CASCADE)
    tipo_quarto=models.CharField(choices=type_quarto, max_length=20)
    Caract=models.CharField(choices=Caracterizacao, max_length=20)
    percentagem=models.FloatField()
    data=models.DateField(auto_now_add=True)
    init_data=models.DateField(blank=True, null=True)
    valid_data=models.DateField()

    def __str__(self):
        return f"hotel: {self.hotel.nome}, Quartos em pomoção: {self.tipo_quarto}/{self.Caract}" 
    

