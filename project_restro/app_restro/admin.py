from django.contrib import admin
from .models import Category, Menu

# Register your models here.
class AdminMenu(admin.ModelAdmin):
    list_display = ("menu_title", "category_id", "menu_desc", "menu_price", "menu_img")
    search_fields = ("menu_title",)
    list_filter = ("menu_title", "category_id")

class AdminCategory(admin.ModelAdmin):
    list_display = ("category_name",)

admin.site.register(Category, AdminCategory)
admin.site.register(Menu, AdminMenu)

admin.site.index_title = "Admin Panel"
admin.site.site_header = "MINDRISER"
admin.site.site_title = "MindRisers"