from django.contrib.auth.models import User
from django.db import models


class ContatoSimples(models.Model):

    nome_remetente = models.CharField(
        verbose_name='Nome', max_length=50
    )

    email = models.EmailField(
        verbose_name='E-mail'
    )

    assunto = models.CharField(
        verbose_name='Assunto',
        max_length=255
    )

    mensagem = models.TextField(
        verbose_name='Mensagem'
    )

    status = models.BooleanField(
        verbose_name='Status (contato aberto/contato não aberto)',
        default=False
    )

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return f'{self.nome_remetente}, {self.assunto}'


class ContatoLGPD(models.Model):

    nome_remetente = models.CharField(
        verbose_name='Nome', max_length=50
    )

    email = models.EmailField(
        verbose_name='E-mail'
    )

    assunto = models.CharField(
        verbose_name='Assunto',
        max_length=255
    )

    mensagem = models.TextField(
        verbose_name='Mensagem'
    )

    status = models.BooleanField(
        verbose_name='Contato aberto',
        default=False
    )

    class Meta:
        verbose_name = 'LPGD'
        verbose_name_plural = 'LGPD'

    def __str__(self):
        return f'{self.nome_remetente}, {self.assunto}'
