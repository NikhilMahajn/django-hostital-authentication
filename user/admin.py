from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Users

# Register your models here.
class UserAdmin(UserAdmin):
    model = Users
    list_display = ('email', 'username', 'is_staff', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(Users, UserAdmin)

