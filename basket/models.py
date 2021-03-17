from django.db import models

# Create your models here.


class Basket(models.Model):
    id = models.AutoField(primary_key=True)
    cookie = models.DecimalField(max_digits=8, decimal_places=0)
    item_number = models.DecimalField(max_digits=30, decimal_places=0)
    category = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    servings = models.DecimalField(max_digits=3, decimal_places=0)
    option = models.CharField(max_length=254)
    total_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    # def __str__(self):
    #     return self.name
    def __str__(self):
        return '{} - {}'.format(self.pk, self.name)