from django.urls import path

from controle_financeiro.carteira.views import allocation

app_name = 'carteira'

urlpatterns = [
    path('', allocation, name='allocation'),
]
