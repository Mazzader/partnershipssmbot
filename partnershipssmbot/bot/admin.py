from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'external_id',
                    'name',
                    'invite_from',
                    'invited_users',)
