from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User, Ad


class UserAdmin(DjangoUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['username', 'name', 'user_type']
    fieldsets = DjangoUserAdmin.fieldsets + (
        (None, {'fields': ('name', 'user_type', 'phone')}),
    )


class AdAdmin(admin.ModelAdmin):
    model = Ad


admin.site.register(User, UserAdmin)
admin.site.register(Ad, AdAdmin)
