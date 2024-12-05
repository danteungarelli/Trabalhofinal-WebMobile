from django.urls import path
from anuncio.views import CriarAnuncio, ListarAnuncios, EditarAnuncio, DeletarAnuncio, ListarAnunciosAPI, APICadastrarAnuncio, APIDeletarAnuncio, APIEditarAnuncio

urlpatterns = [
    path('', ListarAnuncios.as_view(), name='listar-anuncio'),
    path ('novo/', CriarAnuncio.as_view(), name = 'criar-anuncio'),
    path('<int:pk>/', EditarAnuncio.as_view(), name = 'editar-anuncio'),
    path('deletar/<int:pk>/', DeletarAnuncio.as_view(), name = 'deletar-anuncio'), 
    path ('api/', ListarAnunciosAPI.as_view(), name = 'listar-api-anuncio'),
    path('api/cadastrar/', APICadastrarAnuncio.as_view(), name='cadastrar-api-anuncio'),
    path('api/<int:pk>/', APIDeletarAnuncio.as_view(), name='api-deletar-anuncios'),
    path('api/editar/<int:pk>/', APIEditarAnuncio.as_view(), name='api-editar-anuncios')
]