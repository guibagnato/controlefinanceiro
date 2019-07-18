from django.contrib.auth.models import User
from django.test import TestCase

from controle_financeiro.carteira.models import Definicao, Composicao
from controle_financeiro.produtos.models import Acao


class DefinicaoModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='johndoe', password='teste@123', email='john@doe.com')
        self.definicao = Definicao(user=user, name='Carteira Teste')
        self.definicao.save()

    def test_create(self):
        """Check if definicao was created"""
        self.assertTrue(Definicao.objects.exists())

    def test_str(self):
        """Check str for Definicao"""
        self.assertEqual('Carteira Teste - johndoe', str(self.definicao))


class ComposicaoModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='johndoe', password='teste@123', email='john@doe.com')
        itub3 = Acao.objects.create(code='ITUB3', name='Itaú Unibanco')
        definicao = Definicao.objects.create(user=user, name='Carteira Teste')

        self.composicao = Composicao(definicao=definicao, acao=itub3, weight=1.0)
        self.composicao.save()

    def test_create(self):
        """Check if Composicao was created"""
        self.assertTrue(Composicao.objects.exists())

    def test_str(self):
        """Check str for Composicao"""
        self.assertEqual('Carteira Teste - ITUB3 : 1.0', str(self.composicao))