from django.shortcuts import render
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView
from casa.models import Casa
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from casa.forms import FormularioCasa
from casa.serializer import SerializadorCasa
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView


class CriarCasas (LoginRequiredMixin, CreateView):
    
    model= Casa
    form_class = FormularioCasa
    template_name = 'casa/novo.html'
    success_url = reverse_lazy ('listar-casas')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Associa a casa ao usuário logado
        return super().form_valid(form)


class ListarCasas (LoginRequiredMixin, ListView):

    model = Casa
    context_object_name = 'casas'
    template_name = 'casa/listar.html'
    
    def get_queryset(self):
        return Casa.objects.filter(usuario=self.request.user)  # Filtra pelo usuário logado
    
class FotoCasa( LoginRequiredMixin, View):
    
    def get(self, request, arquivo):
        try:
            casa = Casa.objects.get(foto= 'casa/fotos/{}'. format(arquivo))
            return FileResponse (casa.foto)
        except ObjectDoesNotExist:
            raise Http404( "Foto não encontrada ou acesso não autorizado! ")
        except Exception as exception:
            raise exception
        
class EditarCasas (LoginRequiredMixin, UpdateView):
    model = Casa
    form_class = FormularioCasa
    template_name = 'casa/editar.html'
    success_url = reverse_lazy ('listar-casas')
    
    def get_queryset(self):
        return Casa.objects.filter(usuario=self.request.user)  # Filtra pelo usuário logado

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Garante que o usuário logado permaneça
        return super().form_valid(form)

class DeletarCasas (LoginRequiredMixin, DeleteView):
    model = Casa
    template_name = 'casa/deletar.html'
    success_url = reverse_lazy ('listar-casas')
    
    
    def get_queryset(self):
        return Casa.objects.filter(usuario=self.request.user)  # Filtra pelo usuário logado

class APIListarCasas(ListAPIView):
    
    serializer_class = SerializadorCasa
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def get_queryset(self):
        # Retorna apenas as casas cadastradas pelo usuário autenticado
        return Casa.objects.filter(usuario=self.request.user)
    
    
class APIDeletarCasas(DestroyAPIView):
    """
    View para deletar instâncias de veículos (por meio da API REST)
    """
    serializer_class = SerializadorCasa
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Garante que o usuário só possa deletar suas próprias casas
        return Casa.objects.filter(usuario=self.request.user)


class APICadastrarCasa(CreateAPIView):
    serializer_class = SerializadorCasa
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perfoxxrm_create(self, serializer):
        # Define o usuário autenticado como o dono da casa
        serializer.save(usuario=self.request.user)
        
class APIEditarCasa(UpdateAPIView):
    """
    View para editar uma casa específica via API REST
    """
    serializer_class = SerializadorCasa
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

   
    def get_queryset(self):
        # Garante que o usuário só possa editar suas próprias casas
        return Casa.objects.filter(usuario=self.request.user)

    def perform_update(self, serializer):
        # Garante que o usuário autenticado continua sendo o dono da casa
        serializer.save(usuario=self.request.user)