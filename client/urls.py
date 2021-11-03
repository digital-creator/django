from django.urls import path
from client.views import *

urlpatterns = [
    path('', index_client, name='client')
]
