from django.conf.urls import url
from users.views import *

urlpatterns = [
    url('', user_login, name='login')
]
