from django.urls import path
from casa.views import CriarCasas, ListarCasas, FotoCasa, EditarCasas, DeletarCasas,APIListarCasas, APIDeletarCasas, APICadastrarCasa, APIEditarCasa

urlpatterns = [
    path('', ListarCasas.as_view(), name='listar-casas'),
    path ('novo/',CriarCasas.as_view(), name = 'criar-casas'),
    path('fotos/<str:arquivo>/', FotoCasa.as_view(), name= 'foto-casa' ),
    path('<int:pk>/', EditarCasas.as_view(), name = 'editar-casas'),
    path('deletar/<int:pk>/', DeletarCasas.as_view(), name = 'deletar-casas'),
    path ('api/', APIListarCasas.as_view(), name = 'api-listar-casas'),
    path('api/<int:pk>/', APIDeletarCasas.as_view(), name='api-deletar-casas'),
    path('api/cadastrar/',APICadastrarCasa.as_view(),name = 'api-cadastrar-casas'),
    path('api/editar/<int:pk>/', APIEditarCasa.as_view(), name='api-editar-casas'),  
]