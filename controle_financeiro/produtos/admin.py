from django.contrib import admin

from controle_financeiro.produtos.models import Acao


class AcaoModelAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code',)


admin.site.register(Acao, AcaoModelAdmin)
