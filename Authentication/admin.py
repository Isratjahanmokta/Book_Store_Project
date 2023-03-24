from django.contrib import admin
from .models import CustomUser
from django.contrib.auth import get_user_model

from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

CustomUser = get_user_model()
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['first_name', 'last_name', 'email', 'is_superuser']

admin.site.register(CustomUser, CustomUserAdmin)