"""
URL configuration for disquaires project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings #import all settings parameters
from django.urls import include, path, re_path #import url and included
from django.contrib import admin
from store import views

urlpatterns = [
    re_path(r'^$', views.index), #Afficher le contenu de la vue avec la fonction index
    re_path(r'^store/', include('store.urls', namespace="store")), #Definir la route pour l'application store
    path('webadmin/', admin.site.urls),
]
#AJOUT DES URLS DE LA BOITE A OUTILS
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns