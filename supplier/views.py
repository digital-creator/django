from django.shortcuts import render
from supplier.models import *
# Create your views here.

def index_supplier(request):
    context = {
        'title': 'Личный кабинет поставщика',
        'welcome': 'Добро пожаловать в кабинет поставщика'
    }
    return render(request, "supplier/index.html", context)
