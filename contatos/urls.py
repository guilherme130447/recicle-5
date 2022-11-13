from django.urls import path

from . import views

app_name = 'contatos'

urlpatterns = [
    path('contato/', views.contato, name='padrao'),
    path('lgpd/', views.lgpd, name='lgpd'),
]
