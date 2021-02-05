from django.db import models
from alojamento.models import Alojamento
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
status_quarto=(
    ("Ocupado","Ocupado"),
    ("Disponivel","Disponivel"),
    ("Outros","Outros")
)

class Quarto(models.Model):
    hotel_owner=models.ForeignKey(Alojamento, on_delete=models.CASCADE)
    Numero_do_quarto=models.IntegerField()
    Status=models.CharField(choices=status_quarto, max_length=10)
    Caract_bedroom=models.CharField(choices=Caracterizacao, max_length=10)
    type_bedroom= models.CharField(choices=type_quarto, max_length=20)
    data_de_criacao=models.DateField(auto_now_add=True)
    preco=models.FloatField()
   

    def __str__(self):
        return "Nome do Hotel: {},Quarto número: {}, Status: {}".format(
            self.hotel_owner.nome,self.Numero_do_quarto, self.Status,)
        #return self.Caract_bedroom