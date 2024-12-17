from django.contrib import admin
from . import models

# Set the title of the dashboard
admin.site.site_header = 'Rethinking Transitional Justice: Admin Dashboard'


# Actions


# Remove 'delete' action
admin.site.disable_action('delete_selected')


def approve(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to approved
    """
    queryset.update(admin_approved=True)


approve.short_description = "Approve selected items (will appear on main site)"


def unapprove(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to not approved
    """
    queryset.update(admin_approved=False)


unapprove.short_description = "Unapprove selected items (will not appear on main site)"


# Inlines


class SoundscapeExhibitionCommentInline(admin.TabularInline):
    model = models.SoundscapeExhibitionComment
    fields = ('comment', 'admin_approved')
    extra = 0


# AdminViews


@admin.register(models.SoundUploadCode)
class SoundUploadCodeAdminView(admin.ModelAdmin):
    list_display = ('id', 'code', 'assigned_to', 'sounds_count')
    search_fields = ('code', 'assigned_to')
    ordering = ('-id',)


@admin.register(models.Sound)
class SoundAdminView(admin.ModelAdmin):
    list_display = ('id', 'sound', 'location', 'order_in_soundscape_exhibition', 'description_preview', 'sound_upload_code', 'author', 'created', 'admin_approved')
    search_fields = ('description', 'location', 'sound', 'admin_notes', 'sound_upload_code__code', 'sound_upload_code__assigned_to')
    ordering = ('-created',)
    readonly_fields = ('created', 'sound_upload_code')
    actions = (approve, unapprove)
    inlines = (SoundscapeExhibitionCommentInline,)


@admin.register(models.SoundsRelationship)
class SoundsRelationshipAdminView(admin.ModelAdmin):
    list_display = ('id', 'sound_1', 'sound_2', 'relationship_details')
    search_fields = ('id', 'relationship_details',)
    ordering = ('sound_1', 'sound_2')


@admin.register(models.SoundscapeExhibitionComment)
class SoundscapeExhibitionCommentAdminView(admin.ModelAdmin):
    list_display = ('id', 'sound', 'comment', 'created', 'admin_approved')
    search_fields = ('id', 'comment', 'created')
    ordering = ('-created',)
    readonly_fields = ('created',)
    actions = (approve, unapprove)
