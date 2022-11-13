from django.contrib import admin

from .models import Colaborador, EnderecoModel, Consumidor, ItemModel


@admin.register(ItemModel)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["nome", "descricao"]


@admin.register(Consumidor)
class ConsumidorAdmin(admin.ModelAdmin):
    list_display = [
        "usuario",
    ]


@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = [
        "usuario",
    ]


@admin.register(EnderecoModel)
class ColetorAdmin(admin.ModelAdmin):
    list_display = [
        "empresa",
    ]
