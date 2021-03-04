from django.shortcuts import render

import uuid

from products.models import Product, Category, Options
from basket.models import Basket
from checkout.models import Order_items
from basket.contexts import basket_context
from profiles.models import UserProfile
from .forms import OrderForm

# Create your views here.


def checkout(request):
    """ A view to return the checkout page """

    # Attempt to prefill the form with any info the user maintains in their profile
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'full_name': profile.default_full_name,
                'email': profile.user.email,
                'phone_number': profile.default_phone_number,
                'country': profile.default_country,
                'postcode': profile.default_postcode,
                'town_or_city': profile.default_town_or_city,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'county': profile.default_county,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
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
    order_items = Order_items.objects.all()

    """ check for the customer info from checkout """
    if request.POST:
        form_data = {
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

        """ create a unique order number """
        order_number = uuid.uuid4().hex[:10]

        """ populate the order form """
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.order_number = order_number
            cookie = request.POST.get('basket_number')
            order.cookie = cookie
            order_total = request.POST.get('total_price')
            order.order_total = order_total
            customer_name = request.user
            order.customer_name = customer_name
            order.save()

        """ fetch the basket items to save into order_items """
        baskets = Basket.objects.filter(cookie=cookie)
        for basket in baskets:
            cookie = basket.cookie
            item_number = basket.item_number
            category = basket.category
            name = basket.name
            servings = basket.servings
            option = basket.option
            total_price = basket.total_price

            """ save the basket items into order_items """
            order_basket = Order_items(cookie=cookie,
                                       order_number=order_number,
                                       item_number=item_number,
                                       category=category,
                                       name=name,
                                       servings=servings,
                                       option=option,
                                       total_price=total_price)
            order_basket.save()
            basket.delete()
            basket_total = ""

    context = {
            'cookie_key': cookie_key,
            'basket_total': basket_total,
        }

    return render(request, 'checkout/checkout_success.html', context)