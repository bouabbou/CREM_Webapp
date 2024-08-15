from django.contrib import admin
from .models import Category, Product, Platform

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'platform')
    search_fields = ('name', 'abbreviation', 'platform__name')
    fields = ('name', 'abbreviation', 'platform')
    list_filter = ('platform',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(Platform)