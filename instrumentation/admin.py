import logging
from django.contrib import admin
from .models import Category, Product, Platform

logger = logging.getLogger(__name__)

# Mapping of users to their allowed platforms
USER_PLATFORM_MAPPING = {
    'asmp': 'ADDITIVE/SUBTRACTIVE MANUFACTURING AND PROTOTYPING PLATFORM',
    'bio': 'BIO/SUBTRACTIVE MANUFACTURING AND PROTOTYPING PLATFORM',
    'resee': 'RENEWABLE ENERGY, STORAGE AND ENERGY EFFICIENCY',
    'aide': 'AI AND DIGITAL ENGINEERING',
    'sai': 'SENSORS AND INSTRUMENTATION',
    'pce': 'PROCESS ENGINEERING AND CIVIL ENGINEERING',
    'msc': 'Materials, Synthesis, and Characterization Platform',
}

class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user = request.user
        allowed_platform = USER_PLATFORM_MAPPING.get(user.username)
        if allowed_platform:
            qs = qs.filter(name=allowed_platform)
        return qs

    def has_add_permission(self, request):
        # Restrict add permission for users in USER_PLATFORM_MAPPING
        if request.user.username in USER_PLATFORM_MAPPING:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        # Restrict delete permission for users in USER_PLATFORM_MAPPING
        if request.user.username in USER_PLATFORM_MAPPING:
            return False
        return super().has_delete_permission(request, obj)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'platform')
    search_fields = ('name', 'abbreviation', 'platform__name')
    fields = ('name', 'abbreviation', 'platform')
    list_filter = ('platform',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user = request.user
        allowed_platform = USER_PLATFORM_MAPPING.get(user.username)
        if allowed_platform:
            qs = qs.filter(platform__name=allowed_platform)
        return qs

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "platform" and request.user.username in USER_PLATFORM_MAPPING:
            allowed_platform = USER_PLATFORM_MAPPING.get(request.user.username)
            kwargs["queryset"] = Platform.objects.filter(name=allowed_platform)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category')
    search_fields = ('name', 'description')
    list_filter = ('category',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        user = request.user
        allowed_platform = USER_PLATFORM_MAPPING.get(user.username)
        if allowed_platform:
            qs = qs.filter(category__platform__name=allowed_platform)
        return qs

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category" and request.user.username in USER_PLATFORM_MAPPING:
            allowed_platform = USER_PLATFORM_MAPPING.get(request.user.username)
            kwargs["queryset"] = Category.objects.filter(platform__name=allowed_platform)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Platform, PlatformAdmin)
