from django.test import TestCase

from controle_financeiro.produtos.models import Acao


class AcoesModelTest(TestCase):
    def setUp(self):
        self.acao = Acao(code='ITUB3', name='Itaú Unibanco')
        self.acao.save()

    def test_create(self):
        """Check if acao was created"""
        self.assertTrue(Acao.objects.exists())

    def test_str(self):
        """Check str for Acoes"""
        self.assertEqual('ITUB3 - Itaú Unibanco', str(self.acao))
