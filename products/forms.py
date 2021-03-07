# Credit: Code-Institute
from django import forms
from .models import Product, Options, Category


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('pk',)

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


class OptionsAdminForm(forms.ModelForm):
    class Meta:
        model = Options
        exclude = ('pk',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_category': 'category',
            'default_option1': 'option1',
            'default_option2': 'option2',
            'default_option3': 'option3',
        }


class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('category',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_name': 'name',
            'default_image': 'image',
        }
