from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'create_at', 'update_at']

