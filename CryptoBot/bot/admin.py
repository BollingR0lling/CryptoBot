from django.contrib import admin
from .models import TgProfile, MenuItem


@admin.register(TgProfile)
class TgProfileAdmin(admin.ModelAdmin):
    list_display = ('creation_time', 'tg_id', 'username', 'first_name', 'second_name')


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
