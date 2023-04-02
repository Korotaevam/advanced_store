from django.contrib import admin
from app_store.admin import BasketAdminInline
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdminInline,)

