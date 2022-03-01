from django.contrib import admin
from .models import Produtos


class ListandoProdutos(admin.ModelAdmin):
    list_display = ('id', 'nomeproduto', 'precoproduto',
                    'descricaoproduto', 'publicado')
    list_display_links = ('id', 'nomeproduto')
    search_fields = ('nomeproduto',)
    list_editable = ('publicado',)
    list_per_page = 5


admin.site.register(Produtos, ListandoProdutos)
