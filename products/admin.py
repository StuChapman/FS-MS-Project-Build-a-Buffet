from django.contrib import admin
from .models import Product, Category, Options

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id_no',
        'name',
        'category',
        'price',
    )

    ordering = ('id_no',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id_no',
        'friendly_name',
        'name',
    )


class OptionsAdmin(admin.ModelAdmin):
    list_display = (
        'id_no',
        'category',
        'option1',
        'option2',
        'option3',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Options, OptionsAdmin)
