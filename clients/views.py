from django.shortcuts import render
from clients.models import *
# Create your views here.

def index_client(request):
    context = {
        'title': 'Личный кабинет клиента',
        'welcome': 'Добро пожаловать в личный кабинет'
    }

    return render(request, "clients/index.html", context)
