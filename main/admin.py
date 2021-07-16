from django.contrib import admin
from .models import *


class NotebookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'price', 'in_stock')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('in_stock',)
    list_filter = ('in_stock', 'price')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Category, CategoryAdmin)
