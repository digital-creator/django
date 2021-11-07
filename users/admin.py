from django.contrib import admin
from users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'is_client', 'is_player', 'is_supplier')


admin.site.register(User, UserAdmin)
# Register your models here.
