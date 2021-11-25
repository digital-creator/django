from django.contrib import admin
from users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'role')


admin.site.register(User, UserAdmin)
# Register your models here.
