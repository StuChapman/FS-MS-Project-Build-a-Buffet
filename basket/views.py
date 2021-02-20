from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from products.models import Product, Category, Options

import requests
import uuid
import datetime

# Create your views here.


def basket(request):
    """ A view to show the current basket """

    cookie_key = settings.COOKIE_KEY

    """ check for a basket cookie """
    try:
        value = request.COOKIES[cookie_key]
        print(value)
    except KeyError:
        print('Cookie Not Found')
        cookie_value = str(uuid.uuid4())
        response = HttpResponse("hello")
        set_cookie(response, cookie_key, cookie_value)
    try:
        value = request.COOKIES['cookie_key']
        print(value)
    except KeyError:
        print('Cookie Not Created')

    category = ""
    selected = ""

    products = Product.objects.all()
    options = Options.objects.all()

    if request.POST:
        if 'servings' in request.POST:
            servings = request.POST["servings"]

    if request.GET:
        if 'product_options' in request.GET:
            product_options = request.GET['product_options']
            product_options_list = product_options.split(',')
            category = product_options_list[0]
            product = product_options_list[1]
            selected = product_options_list[2]
            products = products.filter(name=product)
            options = options.filter(name=category)

    context = {
            'products': products,
            'category': category,
            'product': product,
            'selected': selected,
            'options': options,
            'servings': servings,
            'cookie_key': cookie_key,
        }

    return render(request, 'basket/basket.html', context)


# Credit: https://stackoverflow.com/questions/1622793/django-cookies-how-can-i-set-them
def set_cookie(response, key, value, days_expire=7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
        "%a, %d-%b-%Y %H:%M:%S GMT",
    )
    response.set_cookie(
        key,
        value,
        max_age=max_age,
        expires=expires,
    )
