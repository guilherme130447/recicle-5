from django.contrib import admin

from .models import Categoria, Post


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'autor', 'status', 'publicacao')
    list_filter = ('status', 'publicacao', 'autor')
    raw_id_fields = ('autor', )
    date_hierarchy = 'publicacao'
    search_fields = ('titulo', 'conteudo')
    prepopulated_fields = {'slug':('titulo',)}
