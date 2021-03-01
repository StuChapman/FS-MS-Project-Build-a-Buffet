from django.contrib import admin
from .models import Product, Category, Options

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class OptionsAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'option1',
        'option2',
        'option3',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Options, OptionsAdmin)
