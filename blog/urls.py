from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='nanantsa'),
    #Ce pattern va donc indiquer à Django d'afficher la vue views.post_list à un utilisateur de votre site web qui se rendrait à l'adresse "http://127.0.0.1:8000/".
]