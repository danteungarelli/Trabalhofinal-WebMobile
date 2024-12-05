from django.db import models
from casa.models import Casa
from django.contrib.auth.models import User

class Anuncio (models.Model):
    
 data = models.DateTimeField(auto_now_add=True)
 descricao = models.CharField (max_length=200)
 preco = models.CharField (max_length=200)
 titulo = models.CharField (max_length=50, default='Sem título')
 
 casa = models.ForeignKey(Casa, related_name='anuncios', on_delete=models.CASCADE)
 usuario = models.ForeignKey (User, related_name='anuncios_realizados', on_delete=models.CASCADE)
 
