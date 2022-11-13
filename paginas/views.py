from django.shortcuts import render

from . import forms


# página inicial
def index(request):
    return render(request, "paginas/index.html")


# página de listagem para descarte
def descartes(request):
    return render(request, "paginas/listagem/descartes.html")


# página de listagem para doações
def doacoes(request):
    return render(request, "paginas/listagem/doacoes.html")


# página de cadastro de coletor
def coletas(request):
    return render(request, "paginas/listagem/coletor_registro.html")


# página sobre
def sobre(request):
    return render(request, "paginas/sobre.html")


# página de termos de uso
def termos_de_uso(request):
    return render(request, "paginas/termos_de_uso.html")


# página de politica de privacidade
def politica_de_privacidade(request):
    return render(request, "paginas/politica_de_privacidade.html")


# página para error 404 (página não encontrada)
def view_404(request, exception):
    return render(request, "not_found.html")


# Simulação de coletores
def coletor1(request):
    return render(request, "paginas/coletores_detalhes/coletor_1.html")


def coletor2(request):
    return render(request, "paginas/coletores_detalhes/coletor_2.html")


def coletor3(request):
    return render(request, "paginas/coletores_detalhes/coletor_3.html")


def coletor4(request):
    return render(request, "paginas/coletores_detalhes/coletor_4.html")


def coletor5(request):
    return render(request, "paginas/coletores_detalhes/coletor_5.html")
