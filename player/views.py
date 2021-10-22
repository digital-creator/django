from django.shortcuts import render
from player.models import *
# Create your views here.


def index_player(request):
    history = HistoryActions.objects.order_by("-id")
    context = {
        "title": "Личный кабинет игрока",
        "history_actions": history,
        }
    return render(request, "player/history_actions.html", context)
