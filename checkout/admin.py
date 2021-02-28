from django.contrib import admin
from .models import Order, Order_items


class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total')
                    #    , 'original_bag',
                    #    'stripe_pid')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total')
            #  'user_profile',
            #   , 'original_bag',
            #   'stripe_pid')

    list_display = ('customer_number', 'order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


class Order_itemsAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'cookie',
        'item_number',
        'category',
        'name',
        'servings',
        'option',
    )


admin.site.register(Order, OrderAdmin)
admin.site.register(Order_items, Order_itemsAdmin)
