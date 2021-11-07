from django.shortcuts import render
from player.models import *
# Create your views here.


def index_player(request):
    history = HistoryActions.objects.order_by("id")
    materials_store = PlayersMaterials.objects.order_by('id')
    context = {
        "title": "Личный кабинет игрока",
        "history_actions": history,
        "h_materials": "Сырье на складе",
        "materials_store": materials_store,
        }
    return render(request, "player\player.html", context)
