# Credit: Code-Institute
from django import forms
from .models import Product


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('sku',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_category': 'category',
            'default_sku': 'sku',
            'default_name': 'name',
            'default_description': 'description',
            'default_price': 'price',
            'default_range': 'range',
        }
