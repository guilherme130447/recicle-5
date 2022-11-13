from django.contrib import admin

from .models import Colaborador, Coletor, Consumidor, ItemModel


@admin.register(ItemModel)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']


@admin.register(Consumidor)
class ConsumidorAdmin(admin.ModelAdmin):
    list_display = ['usuario',]


@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ['usuario',]


@admin.register(Coletor)
class ColetorAdmin(admin.ModelAdmin):
    list_display = ['usuario',]
