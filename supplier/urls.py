from django.urls import path
from supplier.views import *

urlpatterns = [
    path('', index_supplier, name='supplier')
]
