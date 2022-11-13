from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify


class Pagina(models.Model):

    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )

    titulo = models.CharField(
        verbose_name="Título",
        max_length=255
    )

    slug = models.SlugField(
        max_length=255
    )

    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    conteudo_pagina = models.TextField(
        verbose_name="Conteúdo"
    )
  
    data_criacao = models.DateTimeField(
        auto_now_add=True
    )

    data_modificacao = models.DateTimeField(
        auto_now=True
    )

    publicacao = models.DateTimeField(
        default=timezone.now
    )

    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default='rascunho')

    
    class Meta:
        ordering = ['-publicacao']

    def __str__(self):
        return self.titulo


@receiver(post_save, sender=Pagina)
def insert_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.titulo)
        return instance.save()
