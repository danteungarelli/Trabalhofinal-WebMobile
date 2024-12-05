from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from sistema_casa.views import Login, Logout,Registro, LoginAPI


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' ,Login.as_view(), name='Login'),
    path('logout/' ,Logout.as_view(), name='Logout'),
    path('casa/', include('casa.urls'), name='casa'),
    path ('registro/', Registro.as_view(), name = 'Registro'),
    path('anuncio/', include('anuncio.urls'), name='anuncio'),
    path('autenticacao-api/', LoginAPI.as_view())
] 
