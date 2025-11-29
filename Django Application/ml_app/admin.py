from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, VideoUploadHistory

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'user_type', 'is_staff', 'date_joined')
    list_filter = ('user_type', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('User Type', {'fields': ('user_type',)}),
    )
    
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('User Type', {'fields': ('user_type',)}),
    )

@admin.register(VideoUploadHistory)
class VideoUploadHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'video_name', 'prediction_result', 'confidence', 'upload_date')
    list_filter = ('prediction_result', 'upload_date')
    search_fields = ('user__username', 'video_name')
    ordering = ('-upload_date',)
    readonly_fields = ('upload_date',)
