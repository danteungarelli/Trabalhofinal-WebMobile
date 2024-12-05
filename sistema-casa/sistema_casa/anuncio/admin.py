from django.contrib import admin
from anuncio.models import Anuncio

class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'descricao','preco', 'casa', 'usuario','titulo')

admin.site.register(Anuncio, AnuncioAdmin)
