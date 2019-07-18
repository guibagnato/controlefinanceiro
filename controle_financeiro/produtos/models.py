from django.db import models


class Acao(models.Model):
    code = models.CharField('Código', max_length=6)
    name = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name_plural = 'ações'
        verbose_name = 'ação'
        ordering = ("code", "name")

    def __str__(self):
        return "{} - {}".format(self.code, self.name)
