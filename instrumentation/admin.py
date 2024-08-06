from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    # Define which fields to display in the list view
    list_display = ('name', 'abbreviation')
    # Define which fields can be searched in the search bar
    search_fields = ('name', 'abbreviation')
    # Define which fields can be edited in the admin form
    fields = ('name', 'abbreviation')
    # Optional: Define how to filter categories in the admin interface
    list_filter = ('name',)

# Register the Category model with the custom CategoryAdmin class
admin.site.register(Category, CategoryAdmin)

# Register the Product model with default admin interface
admin.site.register(Product)
