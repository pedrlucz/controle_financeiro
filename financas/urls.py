from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('controle.urls')), 
    path('adicionar/', include('controle.urls')),
    path('accounts/', include('django.contrib.auth.urls')), # adiciona as urls de autenticação
]
