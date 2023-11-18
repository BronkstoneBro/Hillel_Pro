from django.contrib import admin
from .models import Category, Goods, Tag
import admin_thumbnails


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'activate', 'created', 'updated', 'url']
    list_filter =  ['activate']
    search_fields = ['name', 'descriptions']

@admin_thumbnails.thumbnail('image')
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'activate', 'created', 'updated', 'category']
    list_filter = ['activate', 'category']
    search_fields = ['name', 'descriptions']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Tag)

admin.site.site_header = "Bronislav Admin"
admin.site.site_title = "Bronislav Admin Portal"
admin.site.index_title = "Welcome to Bronislav Admin Portal"
