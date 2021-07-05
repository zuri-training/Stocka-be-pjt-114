from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'business_name', 'profile_pic')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'business_name')
    search_fields = ('email', 'first_name', 'business_name')
    ordering = ('business_name','email',)
