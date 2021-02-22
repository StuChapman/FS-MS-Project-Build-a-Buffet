from django.shortcuts import render
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum

from products.models import Product, Category, Options
from basket.models import Basket

# Create your views here.


def basket(request):
    """ A view to show the current basket """

    cookie_key = settings.COOKIE_KEY

    """ check for a basket cookie """
    try:
        cookie = request.COOKIES[cookie_key]
    except ObjectDoesNotExist:
        basket_session(request)
        return

    category = ""
    selected = ""
    options = ""
    this_product = ""
    baskets = ""
    basket_total = ""

    categories = Category.objects.all()
    products = Product.objects.all()
    options = Options.objects.all()

    if request.POST:
        if 'servings' in request.POST:
            servings = request.POST["servings"]
            if float(servings) == 1:
                discount = 1
            else:
                discount = 1 - ((float(servings) * 2) / 100)

    if request.GET:
        if 'product_options' in request.GET:
            product_options = request.GET['product_options']
            product_options_list = product_options.split(',')
            category = product_options_list[0]
            product = product_options_list[1]
            selected = product_options_list[2]
            this_product = products.filter(name=product)
            options = options.filter(category__in=categories)
            # Credit: http://morozov.ca/tip-how-to-get-a-single-objects-value-with-django-orm.html
            price = products.get(name=product).price
            # Credit: https://stackoverflow.com/questions/23868958/django-insert-row-into-database
            try:
                existing_basket = Basket.objects.get(cookie=cookie,
                                                     category=category,
                                                     name=product,
                                                     option=selected)
                existing_servings = existing_basket.servings
                updated_servings = existing_servings + int(servings)
                if float(updated_servings) == 1:
                    updated_discount = 1
                else:
                    updated_discount = 1 - ((float(updated_servings) * 2) / 100)
                total_price = float(price) * float(updated_servings) * float(updated_discount)
                updated_basket = Basket(cookie=cookie,
                                        category=category,
                                        name=product,
                                        servings=updated_servings,
                                        option=selected,
                                        total_price=total_price)
                updated_basket.save()
                existing_basket.delete()
            except ObjectDoesNotExist:  # Credit: https://stackoverflow.com/questions/12572741/get-single-record-from-database-django
                total_price = float(price) * float(servings) * float(discount)
                basket = Basket(cookie=cookie,
                                category=category,
                                name=product,
                                servings=servings,
                                option=selected,
                                total_price=total_price)
                basket.save()
            baskets = Basket.objects.filter(cookie=cookie)
    else:
        baskets = Basket.objects.filter(cookie=cookie)

    # Credit: https://stackoverflow.com/questions/42132091/using-aggregation-api-django
    basket_total = Basket.objects.filter(cookie=cookie).aggregate(Sum('total_price'))

    context = {
            'products': products,
            'this_product': this_product,
            'options': options,
            'selected': selected,
            'baskets': baskets,
            'basket_total': basket_total
        }

    return render(request, 'basket/basket.html', context)


def basket_session(request):
    """ A view to write the basket to session if no cookie found """

    if request.GET:
        if 'product_options' in request.GET:
            product_options = request.GET['product_options']
            print(product_options)

    return render(request, 'basket/basket.html')