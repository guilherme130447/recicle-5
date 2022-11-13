from django.urls import path

from . import views

app_name = "paginas"

urlpatterns = [
    path("", views.index, name="index"),
    path("descartar/", views.descartes, name="lista_descartar"),
    path(
        "coletar/",
        views.coletas,
        name="lista_coletar",
    ),
    path("doar/", views.doacoes, name="lista_doar"),
    path("sobre/", views.sobre, name="sobre"),
    path("termos-de-uso/", views.termos_de_uso, name="termos_de_uso"),
    path(
        "politica-de-privacidade/",
        views.politica_de_privacidade,
        name="politica_de_privacidade",
    ),
    # Simula coletores
    path("coletores/sucata-digital", views.coletor1, name="coletor_1"),
    path("coletores/e-mile", views.coletor2, name="coletor_2"),
    path("coletores/bh-recicla", views.coletor3, name="coletor_3"),
    path("coletores/reciclo-inteligencia-ambiental", views.coletor4, name="coletor_4"),
    path("coletores/mg-recicla", views.coletor5, name="coletor_5"),
]
