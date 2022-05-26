from django.contrib import admin
from .models import *


class CatMenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("cat_menu_name",)}

class BaseMenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title_menu",)}

class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class Menu_CategoryAdmin(admin.ModelAdmin):
    list_display = ['product_cat_name', 'slug']
    prepopulated_fields = {"slug": ("product_cat_name",)}

class News_coffeeAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'status', 'created']
    list_filter = ("status", )
    search_fields  = ['title', 'content']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(CatMenu, CatMenuAdmin)
admin.site.register(BaseMenu, BaseMenuAdmin)
admin.site.register(ContactForm)
admin.site.register(Profile)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Menu_Category, Menu_CategoryAdmin)
admin.site.register(News_coffee, News_coffeeAdmin)



