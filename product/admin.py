from django.contrib import admin
from product.models import *


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'product_slug':('product_name',),}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'category_slug':('category_name',),}

class CraftAdmin(admin.ModelAdmin):
    prepopulated_fields = {'craft_slug':('craft_name',),}

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Craft, CraftAdmin)
