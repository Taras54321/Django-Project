from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class NotebookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo', 'price', 'in_stock')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('in_stock',)
    list_filter = ('in_stock', 'price')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'cat', 'content', 'get_html_photo', 'photo', 'in_stock')
    readonly_fields = ('get_html_photo', )
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=50>')

    get_html_photo.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Cайт о ноутах'
admin.site.site_header = 'Cайт о ноутбуках'
