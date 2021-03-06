# Credit: Code-Institute
from django.db import models
from django_countries.fields import CountryField

from profiles.models import UserProfile


class Order(models.Model):
    customer_name = models.CharField(max_length=50, null=False, blank=False)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    cookie = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, 
                                     related_name='orders')

    def __str__(self):
        return self.order_number


class Order_items(models.Model):

    class Meta:
        verbose_name_plural = 'Order_items'

    order_number = models.CharField(max_length=32, null=False, editable=False)
    cookie = models.CharField(max_length=32, null=False, editable=False)
    item_number = models.DecimalField(max_digits=8, decimal_places=0)
    category = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    servings = models.DecimalField(max_digits=3, decimal_places=0)
    option = models.CharField(max_length=254)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name