from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Car

# Register your models here.
class UserAdmin(UserAdmin):
    list_display = ['id', 'email', 'created_at', 'updated_at']

class CarAdmin(admin.ModelAdmin):
    list_display = ["id", "brand", "model", "color", "year", "created_at", "updated_at"]


admin.site.register(User)
admin.site.register(Car, CarAdmin)


# class CarAdmin(admin.ModelAdmin):
#     list_display = ["id", "brand", "model"]
