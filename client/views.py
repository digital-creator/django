from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from client.models import *
# Create your views here.

def index_client(request):
    if request.user.is_client:
        context = {
            'title': 'Личный кабинет клиента',
            'welcome': 'Добро пожаловать в личный кабинет'
        }

        return render(request, "client/index.html", context)
    else:
        return HttpResponseRedirect(reverse('login'))
