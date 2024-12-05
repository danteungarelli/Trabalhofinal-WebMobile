
from django.conf import settings
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


class Login(View):
    
    def get (self, request):
       contexto = {'mensagem': ''}
       if request.user.is_authenticated:
           return redirect("/casa")
       else:
         return render(request, 'autenticacao.html', contexto)
   
    def post(self, request):
        # obtem as credenciais de autenticacao do formulario
        usuario= request.POST.get('usuario', None)
        senha = request.POST.get ('senha', None)

        #verifica as credenciais de autenticacao fornecidas

        user = authenticate (request, username=usuario, password=senha)
        if user is not None:

            #verifica se o usuario ainda esta ativo no sistema
            if user.is_active:
                login(request, user)
                return redirect("/casa")

            return render (request, 'autenticacao.html', {'mensagem': 'Usuário inativo.'})
        return render (request, 'autenticacao.html', {'mensagem': 'Usuário ou senha inválidos'})
    
class Logout (View):

    def get(self, request):
        logout(request)
        return redirect (" ")
    
class Registro(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/casa")
        return render(request, 'registro.html', {'form': UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Usuário registrado com sucesso!')
            return redirect('/Login')  # Redireciona para a página de login
        else:
            messages.error(request, 'Erro no registro. Por favor, corrija os erros abaixo.')
        return render(request, 'registro.html', {'form': form})


class LoginAPI(ObtainAuthToken):
    
    def post(self,request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={
                'request':request
            }
        )
        
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'id': user.id,
            'nome': user.first_name,
            'email': user.email,
            'token': token.key
        })

