from django.db import models
from casa.consts import *
from django.contrib.auth.models import User


class Casa (models.Model):
    
    titulo = models.CharField (max_length=100)
    num_quartos = models.SmallIntegerField(choices=OPCOES_NUM_QUARTOS)
    num_banheiros= models.SmallIntegerField(choices=OPCOES_NUM_BANHEIROS)
    tipo = models.SmallIntegerField(choices=OPCOES_TIPO)
    area = models.CharField (max_length=100)
    status = models.SmallIntegerField(choices=OPCOES_STATUS)
    foto =  models.ImageField(blank=True, null=True, upload_to='casa/fotos')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  
    
    def __str__(self):
        return self.titulo 

  
