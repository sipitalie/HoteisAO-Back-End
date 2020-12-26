from rest_framework import serializers
from quartos.models import Quarto



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

class QuartoSerializer(serializers.ModelSerializer):
    #Caract_bedroom=models.CharField(choices=Caracterizacao, max_length=10)
    #type_bedroom= models.CharField(choices=type_quarto, max_length=20)
    
    class Meta:
        model = Quarto
        fields ='__all__'

