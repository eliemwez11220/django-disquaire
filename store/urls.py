from django.urls import path, re_path #Importation des routes relies au projet
from . import views #Importation de la vue ayant les elements a afficher
app_name = "store"
urlpatterns = [
   
    re_path(r'^$', views.index, name="index"), #Afficher le contenu de la vue avec la fonction index
    re_path(r'^page/$', views.page, name="page"), #Afficher le contenu de la vue avec la fonction index

    re_path(r'^listing/$', views.listing, name="listing"), #Afficher le contenu listiing albums de la vue avec la fonction listing
    re_path(r'^artists/$', views.albumsartists, name="artists"), #Afficher le contenu de la vue listing artists avec la fonction artists
    re_path(r'^(?P<album_id>[0-9])/$', views.detail, name="detail"), #Afficher details d'un album par id
    re_path(r'^albumsartist/(?P<artist_id>[0-9])/$', views.artist, name="albums-artist"), #Afficher listing albums d'un artist par id artist
    re_path(r'^search/$', views.search, name="search"), #Afficher details d'un album par suivant le critere de recherche
    re_path(r'^contact', views.contact, name="contact"), #Page de contact
    re_path(r'^about', views.about, name="about"), #Page de contact
]