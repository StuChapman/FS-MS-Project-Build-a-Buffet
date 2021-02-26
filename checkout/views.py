from django.shortcuts import render

from products.models import Product, Category, Options
from basket.models import Basket
from basket.contexts import basket_context
from .forms import OrderForm

# Create your views here.


def checkout(request):
    """ A view to return the checkout page """

    """ check for a basket cookie """
    context_items = basket_context(request)
    basket_total = context_items['basket_total']
    cookie_key = context_items['cookie_key']

    baskets = ""

    """ fetch the datasets from the models """
    basket = Basket.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()
    options = Options.objects.all()

    if request.GET:
        if 'basket_number' in request.GET:
            basket_number = request.GET['basket_number']
            baskets = basket.filter(cookie=basket_number)
            baskets = baskets.order_by('-item_number')

    context = {
            'cookie_key': cookie_key,
            'basket_total': basket_total,
            'baskets': baskets,
            'products': products,
            'categories': categories,
            'options': options,
        }

    return render(request, 'checkout/checkout.html', context)
