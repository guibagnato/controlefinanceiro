from django.contrib.auth.models import User
from django.test import TestCase
from django.shortcuts import resolve_url as r

from controle_financeiro.carteira.models import Definicao, Composicao
from controle_financeiro.produtos.models import Acao


class CarteiraNewGet(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='johndoe', password='teste@123', email='john@doe.com')

        definicao = Definicao.objects.create(user=user, name='Carteira Teste')

        itub3 = Acao.objects.create(code='ITUB3', name='Itaú Unibanco')
        egie = Acao.objects.create(code='EGIE', name='ENGIE Brasil Energia S.A.')
        lren3 = Acao.objects.create(code='LREN3', name='LOJAS RENNER SA')

        Composicao.objects.create(definicao=definicao, acao=itub3, weight=0.3)
        Composicao.objects.create(definicao=definicao, acao=egie, weight=0.2)
        Composicao.objects.create(definicao=definicao, acao=lren3, weight=0.5)

        self.client.force_login(user=user)
        self.resp = self.client.get(r('carteira:allocation'))

    def test_get(self):
        """Get /carteira/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_context(self):
        """Get /carteira/ must return composition"""
        composition, weights = self._get_context()
        self.assertEqual(3, len(composition))
        self.assertEqual(1.0, sum(weights))

    def test_template(self):
        """Must use carteira/allocation.html"""
        self.assertTemplateUsed(self.resp, 'carteira/allocation.html')

    def _get_context(self):
        composition = self.resp.context.get('context').get('composition')
        weights = [stock.weight for stock in composition]
        return composition, weights


class CarteiraNewGetEmpty(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='guibagnato', password='teste@123', email='gui@bagnato.com')
        self.client.force_login(user=user)
        self.resp = self.client.get(r('carteira:allocation'))

    def test_context_empty(self):
        """Get /carteira/ must return empty list if composition is empty"""
        composition, weights = self._get_context()
        self.assertEqual(0, len(composition))
        self.assertEqual(0, sum(weights))

    def _get_context(self):
        composition = self.resp.context.get('context').get('composition')
        weights = [stock.weight for stock in composition]
        return composition, weights
