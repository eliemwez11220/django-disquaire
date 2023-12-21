from django.urls import path, re_path #Importation des routes relies au projet
from . import views #Importation de la vue ayant les elements a afficher
app_name = "store"
urlpatterns = [
   
    re_path(r'^$', views.index, name="index"), #Afficher le contenu de la vue avec la fonction index

    re_path(r'^listing/$', views.listing, name="listing"), #Afficher le contenu de la vue avec la fonction index
    re_path(r'^(?P<album_id>[0-9])/$', views.detail, name="detail"), #Afficher details d'un album par id
    re_path(r'^search/$', views.search, name="search"), #Afficher details d'un album par suivant le critere de recherche
]