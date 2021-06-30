from django.contrib import admin

from stocka_api.models import CustomUserManager, User, Inventory, Venture

@admin.register(CustomUserManager)
class CustomUserManagerAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Venture)
class VentureAdmin(admin.ModelAdmin):
    pass
