from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import SiteUser, Car

# Register your models here.
class UserAdmin(UserAdmin):
    list_display = ['id', 'email', 'created_at', 'updated_at']

class CarAdmin(admin.ModelAdmin):
    list_display = ["id", "brand", "model", "color", "year", "created_at", "updated_at"]

class SiteUserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email", "age", "is_superuser", "created_at", "updated_at"]


admin.site.register(SiteUser, SiteUserAdmin)
admin.site.register(Car, CarAdmin)


# class CarAdmin(admin.ModelAdmin):
#     list_display = ["id", "brand", "model"]
