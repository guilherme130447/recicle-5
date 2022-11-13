from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('o-que-e-o-lixo-eletronico', views.post1, name='post-1'),
    path('10-razoes-para-reciclar-o-lixo-eletronico', views.post2, name='post-2'),
    path('como-descartar-o-lixo-eletronico', views.post3, name='post-3'),
]
