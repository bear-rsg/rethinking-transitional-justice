from django.contrib import admin
from . import models

# Set the title of the dashboard
admin.site.site_header = 'Rethinking Transitional Justice: Admin Dashboard'


@admin.register(models.Sound)
class SoundAdminView(admin.ModelAdmin):
    list_display = ('id', 'sound', 'location', 'description', 'created')
    search_fields = ('description', 'location', 'sound')
    ordering = ('-created',)
    readonly_fields = ('created',)
