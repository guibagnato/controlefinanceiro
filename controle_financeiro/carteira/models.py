from django.contrib.auth.models import User
from django.db import models

from controle_financeiro.produtos.models import Acao


class Definicao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    name = models.CharField('nome da carteira', max_length=20)

    class Meta:
        verbose_name_plural = 'Definição'
        verbose_name = 'Definições'
        ordering = ("user__username", "name")

    def __str__(self):
        return "{} - {}".format(self.name, self.user.username)


class Composicao(models.Model):
    definicao = models.ForeignKey(Definicao, on_delete=models.CASCADE, verbose_name='Definição')
    acao = models.ForeignKey(Acao, on_delete=models.CASCADE, verbose_name='Ação')
    weight = models.DecimalField('Peso', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Composição'
        verbose_name = 'Composições'
        ordering = ("definicao__name", "acao__code", "weight")

    def __str__(self):
        return "{} - {} : {}".format(self.definicao.name, self.acao.code, self.weight)
