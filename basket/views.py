from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from products.models import Product, Category, Options

import requests
import uuid

# Create your views here.


def basket(request):
    """ A view to show the current basket """

    """ check for a basket cookie """
    cookie_key = settings.COOKIE_KEY
    try:
        value = request.COOKIES[settings.COOKIE_KEY]
        print(value)
    except:
        print('Cookie Not Found')
        cookie_value = str(uuid.uuid4())
        request.COOKIES[cookie_key] = cookie_value
        try:
            response = HttpResponse('/basket.html')
            response.set_cookie(cookie_key, cookie_value, expires=7)
        except KeyError:
            print('Cookie Not Set')
    try:
        value = request.COOKIES[cookie_key]
        print('Found Cookie')
    except KeyError:
        print('Cant find Cookie')

    category = ""
    selected = ""
    options = ""

    categories = Category.objects.all()
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
        }

    return render(request, 'basket/basket.html', context)
