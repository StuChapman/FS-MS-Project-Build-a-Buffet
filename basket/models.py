from django.db import models

# Create your models here.


class Basket(models.Model):
    cookie = models.DecimalField(max_digits=8, decimal_places=0)
    category = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    servings = models.DecimalField(max_digits=2, decimal_places=0)
    option = models.CharField(max_length=254)

    def __str__(self):
        return self.name