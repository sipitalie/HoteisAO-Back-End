from django.db import models
from django.conf import settings
#from ImagensPerfil.models import Imagens

#tipo
Type=(('Hotel','Hotel'),
    ('Apart-hotel','Apart-hotel'),
    ('Residencial/Pensão','Residencial/Pensão'),
    ('Resort/Lodge','Resort/Lodge'),
    ('Outros', 'Outros')
)
#E quanto às classificações?
estrela=(
    (1, '1 estrela'),
    (2,'2 estrelas'),
    (3,'3 estrelas'),
    (4,'4 estrelas'),
    (5,' 5 estrelas'),
)
def uploud_image(instance, filename):
    return "{}{}".format(instance.nome,filename)
class Alojamento (models.Model):
    owner=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome=models.CharField(max_length=50)
    Type_Alojamento=models.CharField(choices=Type, max_length=20)
    Estrela=models.IntegerField(choices=estrela)
    Aprovado=models.BooleanField(default=True)
    data=models.DateField(auto_now_add=True)
    pais=models.CharField(max_length=50)
    Provincia=models.CharField(max_length=150)
    cidade=models.CharField(max_length=50)
    linha=models.CharField(max_length=150)
    latitude=models.FloatField()
    longitude=models.FloatField()
    foto=models.ImageField(upload_to=uploud_image,null=True, blank=True)
   
    def __str__(self):
        return self.nome



