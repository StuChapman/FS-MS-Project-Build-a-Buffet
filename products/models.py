# Credit: Code-Institute
from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True)
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    range = models.CharField(max_length=254, null=True)

    def __str__(self):
        return self.name


class Options(models.Model):

    class Meta:
        verbose_name_plural = 'Options'

    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    option1 = models.CharField(max_length=24)
    option2 = models.CharField(max_length=24)
    option3 = models.CharField(max_length=24)

    def __str__(self):
        return self.category
