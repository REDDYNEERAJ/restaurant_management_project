from django.contrib import admin
from .models import MenuCategory

# Register your models here.
@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)