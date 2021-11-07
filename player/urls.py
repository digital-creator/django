from django.urls import path
from player.views import *

urlpatterns = [
    path('', index_player, name="player")
]
