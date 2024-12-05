from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from anuncio.models import Anuncio
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from anuncio.forms import FormularioAnuncio
from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from anuncio.serializer import SerializadorAnuncio
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

class CriarAnuncio (LoginRequiredMixin, CreateView):
    
    model= Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/novo.html'
    success_url = reverse_lazy ('listar-anuncio')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['usuario'] = self.request.user  # Passa o usuário logado
        return kwargs

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Define o usuário no modelo
        return super().form_valid(form)


class ListarAnuncios (LoginRequiredMixin, ListView):

    model = Anuncio
    context_object_name = 'anuncios'
    template_name = 'anuncio/listar.html'
    



class EditarAnuncio (LoginRequiredMixin, UpdateView):
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/editar.html'
    success_url = reverse_lazy('listar-anuncio')
    
    def get_queryset(self):
        return Anuncio.objects.filter(usuario=self.request.user)  # Restringe a edição

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['usuario'] = self.request.user  # Passa o usuário logado para filtrar casas
        return kwargs
    
    
    
class DeletarAnuncio (LoginRequiredMixin, DeleteView):
    model = Anuncio
    template_name = 'anuncio/deletar.html'
    success_url = reverse_lazy ('listar-anuncio')
    
    def get_queryset(self):
        return Anuncio.objects.filter(usuario=self.request.user)  # Restringe a exclusão


class ListarAnunciosAPI(ListAPIView):
    """
    View para listar os anúncios disponíveis na API
    """
    serializer_class = SerializadorAnuncio
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        #return Anuncio.objects.filter(usuario=self.request.user)
        return Anuncio.objects.all()
    

class APICadastrarAnuncio(CreateAPIView):
    serializer_class = SerializadorAnuncio
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Define o usuário autenticado como dono do anúncio
        serializer.save(usuario=self.request.user)
        
    
class APIDeletarAnuncio(DestroyAPIView):
    """
    View para deletar instâncias de veículos (por meio da API REST)
    """
    serializer_class = SerializadorAnuncio
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        
        return Anuncio.objects.filter(usuario=self.request.user)

       
class APIEditarAnuncio(UpdateAPIView):
    """
    View para editar uma casa específica via API REST
    """
    serializer_class = SerializadorAnuncio
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

   
    def get_queryset(self):
        # Garante que o usuário só possa editar suas próprias casas
        return Anuncio.objects.filter(usuario=self.request.user)

    def perform_update(self, serializer):
        # Garante que o usuário autenticado continua sendo o dono da casa
        serializer.save(usuario=self.request.user)