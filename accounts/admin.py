from django.contrib import admin
from .models import Accounts

# Register your models here.

class AccountsAdmin(admin.ModelAdmin):
    list_display = ('group', 'login', 'password') # Какие поля будут отображаться
    list_display_links = ('login',) # Поля по которым можно редактировать запись
    search_fiels = ('group', 'login') # Поля по которым осущ. поиск

admin.site.register(Accounts, AccountsAdmin)
