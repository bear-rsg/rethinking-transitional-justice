from django.contrib import admin
from . import models

# Set the title of the dashboard
admin.site.site_header = 'Rethinking Transitional Justice: Admin Dashboard'


@admin.register(models.SoundUploadCode)
class SoundAdminView(admin.ModelAdmin):
    list_display = ('id', 'code', 'assigned_to', 'sounds_count')
    search_fields = ('code', 'assigned_to')
    ordering = ('-id',)


@admin.register(models.Sound)
class SoundAdminView(admin.ModelAdmin):
    list_display = ('id', 'sound', 'location', 'description', 'created', 'admin_approved')
    search_fields = ('description', 'location', 'sound', 'admin_notes')
    list_filter = ('sound_upload_code',)
    ordering = ('-created',)
    readonly_fields = ('created', 'sound_upload_code')
