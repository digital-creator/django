from django.urls import path
from clients.views import *

urlpatterns = [
    path('', index_client)
]
