from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("dashboard", dashboard, name="dashboard"),
    path("carte_agences_tde", carte_agences_tde, name="carte_agences_tde"),
    path("carte_bornes_fontaines", carte_bornes_fontaines, name="carte_bornes_fontaines"),
    path("carte_poste_eau", carte_poste_eau, name="carte_poste_eau"),
    path("graphe_tde", graphe_tde, name="graphe_tde"),
    path("graphe_toilettes", graphe_toilette, name="graphe_toilette"),
    path("graphe_etablissement", graphe_etablissement, name="graphe_etablissement")
]