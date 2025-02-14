from django.urls import path
from .views import adicionar_transacao, lista_transacoes
from . import views

urlpatterns = [
    path('adicionar/', adicionar_transacao, name = 'adicionar_transacao'),
    path('transacoes/' , lista_transacoes, name = 'lista_transacoes'),
    path('register/', views.register, name = 'register')
]