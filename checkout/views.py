from django.shortcuts import render

from products.models import Product, Category, Options
from basket.models import Basket
from basket.contexts import basket_context
from .forms import OrderForm

# Create your views here.


def checkout(request):
    """ A view to return the checkout page """

    order_form = OrderForm()

    """ check for a basket cookie """
    context_items = basket_context(request)
    cookie = context_items['cookie']
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
            'cookie': cookie,
            'cookie_key': cookie_key,
            'basket_total': basket_total,
            'baskets': baskets,
            'products': products,
            'categories': categories,
            'options': options,
            'order_form': order_form,
        }

    return render(request, 'checkout/checkout.html', context)


def create_order(request):
    """ A view to return the checkout page """

    order_form = OrderForm()

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

    """ check for the basket items from checkout """
    if request.POST:
        print('POST')
        form_data = {
            'basket_number': request.POST['basket_number'],
        }
        print(basket_number)
        if 'basket_number' in request.POST:
            cookie = request.POST['basket_number']
            print(cookie)

    context = {
            'cookie_key': cookie_key,
            'basket_total': basket_total,
            'baskets': baskets,
            'products': products,
            'categories': categories,
            'options': options,
            'order_form': order_form,
        }

    return render(request, 'checkout/checkout.html', context)