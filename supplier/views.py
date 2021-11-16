from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from supplier.models import *
# Create your views here.

def index_supplier(request):
    if request.user.is_supplier:
        context = {
            'title': 'Личный кабинет поставщика',
            'welcome': 'Добро пожаловать в кабинет поставщика'
        }
        return render(request, "supplier/index.html", context)
    else:
        return HttpResponseRedirect(reverse('login'))
