from django.contrib import admin

from .models import ContatoLGPD, ContatoSimples


@admin.register(ContatoSimples)
class ContatoSimplesAdmin(admin.ModelAdmin):
    list_display = ['nome_remetente', 'email', 'assunto', 'status']


@admin.register(ContatoLGPD)
class ContatoLGPDAdmin(admin.ModelAdmin):
    list_display = ['nome_remetente', 'email', 'assunto', 'status']
