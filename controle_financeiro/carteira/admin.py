from django.contrib import admin

from controle_financeiro.carteira.models import Definicao, Composicao


class DefinicaoModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('user',)


class ComposicaoModelAdmin(admin.ModelAdmin):
    list_display = ('definicao', 'acao', 'weight')
    search_fields = ('definicao', 'acao')


admin.site.register(Definicao, DefinicaoModelAdmin)
admin.site.register(Composicao, ComposicaoModelAdmin)
