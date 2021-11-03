from django.shortcuts import render
from client.models import *
# Create your views here.

def index_client(request):
    context = {
        'title': 'Личный кабинет клиента',
        'welcome': 'Добро пожаловать в личный кабинет'
    }

    return render(request, "client/index.html", context)
