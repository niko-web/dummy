from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import SiteUser, Car


class CarAdmin(admin.ModelAdmin):
    list_display = ["id", "brand", "model", "color", "year", "created_at", "updated_at"]

class SiteUserAdmin(UserAdmin):
    pass


admin.site.register(SiteUser, SiteUserAdmin)
admin.site.register(Car, CarAdmin)

