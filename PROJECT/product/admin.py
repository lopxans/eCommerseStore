from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'description', 'category']
