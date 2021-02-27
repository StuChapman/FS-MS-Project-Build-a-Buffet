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
        form_data = {
            'order_number': request.POST['basket_number'],
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order_number = request.POST.get('basket_number')
            order.order_number = order_number
            order.save()

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

    return render(request, 'home/index.html', context)