from django.urls import path
from .views import *

urlpatterns = [
    path('cadastrar_aluguel/', cadastrar_aluguel, name='cadastrar_aluguel'),
    path('lista_alugueis/', lista_alugueis, name='lista_alugueis'),
    path('cadastrar_mesas_cadeiras_disponiveis/', cadastrar_mesas_cadeiras_disponiveis, name='cadastrar_mesas_cadeiras_disponiveis'),
]