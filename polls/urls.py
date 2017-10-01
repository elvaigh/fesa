from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.accueil),
    url(r'^accueil$', views.accueil),
    url(r'^offres$', views.offres),
    url(r'^annonce$', views.annonce),
    url(r'^connexion$', views.connexion),
    url(r'^inscription$', views.inscription),
    url(r'^deconnexion$', views.deconnexion),
]