from django.contrib.auth.models import User
from django.db import models


class Mensagem(models.Model):

    remetente = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='mensagens'
    )

    destinatario = models.ManyToManyField(
        User
    )

    assunto = models.CharField(
        verbose_name='Assunto',
        max_length=255
    )

    mensagem = models.TextField(
        verbose_name='Mensagem'
    )

    class Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'

    def __str__(self):
        return f'{self.assunto}'
