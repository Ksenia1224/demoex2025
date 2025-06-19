from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.views.generic import UpdateView

from users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'full_name', 'email', 'phone')


