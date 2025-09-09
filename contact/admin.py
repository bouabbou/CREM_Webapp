from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'truncated_message')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
    
    def truncated_message(self, obj):
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    truncated_message.short_description = 'Message Preview'
