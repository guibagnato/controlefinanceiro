from django.contrib.auth.models import User
from django.shortcuts import render

from controle_financeiro.carteira.models import Composicao


def allocation(request):
    composition = Composicao.objects.filter(definicao__user=request.user)

    context = dict(composition=composition)
    return render(request, 'carteira/allocation.html', {'context': context})
