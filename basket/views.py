from django.shortcuts import render
from django.conf import settings

from products.models import Product, Category, Options
from basket.models import Basket

# Create your views here.


def basket(request):
    """ A view to show the current basket """

    cookie_key = settings.COOKIE_KEY

    """ check for a basket cookie """
    try:
        cookie = request.COOKIES[cookie_key]
        print(cookie)
    except KeyError:
        print('Cookie Not Found')

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
            options = options.filter(category__in=categories)
            # Credit: https://stackoverflow.com/questions/23868958/django-insert-row-into-database
            basket = Basket(cookie=cookie,
                            category=category,
                            name=product,
                            price='0.00',
                            servings=servings,
                            option=selected)
            basket.save()

    context = {
            'products': products,
            'category': category,
            'product': product,
            'selected': selected,
            'options': options,
            'servings': servings,
        }

    return render(request, 'basket/basket.html', context)
