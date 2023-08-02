from django.contrib import admin
from .models import Menu, MenuItem


# Register Menu model in the admin
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'date')
    # Add any other options you want to customize the admin interface for Menu model

# Register MenuItem model in the admin
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    # Add any other options you want to customize the admin interface for MenuItem model
