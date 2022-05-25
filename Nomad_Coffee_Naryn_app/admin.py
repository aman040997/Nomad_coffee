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


admin.site.register(CatMenu, CatMenuAdmin)
admin.site.register(BaseMenu, BaseMenuAdmin)
admin.site.register(ContactForm)
admin.site.register(Profile)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Menu_Category, Menu_CategoryAdmin)



