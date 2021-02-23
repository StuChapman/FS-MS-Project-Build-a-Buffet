from django.shortcuts import render, redirect
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
    except KeyError:
        return render(request, 'basket/basket.html')

    """ set all the variables to blank """
    category = ""
    selected = ""
    options = ""
    this_product = ""
    baskets = ""
    basket_total = ""

    """ fetch the datasets from the models """
    categories = Category.objects.all()
    products = Product.objects.all()
    options = Options.objects.all()

    """ check for a servings variable from the form """
    if request.POST:
        if 'servings' in request.POST:
            servings = request.POST["servings"]
            """ generate the discount variable """
            if float(servings) == 1:
                discount = 1
            else:
                discount = 1 - ((float(servings) * 2) / 100)

    if request.GET:

        """ check for a product_add variable from the template """
        if 'product_add' in request.GET:
            product_add = request.GET['product_add']

            """ split the product_add variable into its components """
            product_add_list = product_add.split(',')
            category = product_add_list[0]
            product = product_add_list[1]
            selected = product_add_list[2]

            """ filter the datasets on the variables from product_add """
            this_product = products.filter(name=product)
            options = options.filter(category__in=categories)
            """ Credit: http://morozov.ca/tip-how-to-get-a-single-objects-value-with-django-orm.html """
            price = products.get(name=product).price

            """ check for existing basket(s) with the current cookie value """
            try:
                existing_basket = Basket.objects.get(cookie=cookie,
                                                     category=category,
                                                     name=product,
                                                     option=selected)
                existing_servings = existing_basket.servings

                """ add the new servings variable to the existing """
                updated_servings = existing_servings + int(servings)

                """ generate the discount variable """
                if float(updated_servings) == 1:
                    updated_discount = 1
                else:
                    updated_discount = 1 - ((float(updated_servings) * 2) / 100)
                total_price = float(price) * float(updated_servings) * float(updated_discount)

                """ save the updated basket and delete the existing """
                updated_basket = Basket(cookie=cookie,
                                        category=category,
                                        name=product,
                                        servings=updated_servings,
                                        option=selected,
                                        total_price=total_price)
                updated_basket.save()
                existing_basket.delete()

            except ObjectDoesNotExist:  # Credit: https://stackoverflow.com/questions/12572741/get-single-record-from-database-django

                """ if there is no existing basket, create a new one """
                total_price = float(price) * float(servings) * float(discount)
                basket = Basket(cookie=cookie,
                                category=category,
                                name=product,
                                servings=servings,
                                option=selected,
                                total_price=total_price)
                basket.save()
            baskets = Basket.objects.filter(cookie=cookie)

        """ check for a product_edit variable from the template """
        if 'product_edit' in request.GET:
            product_edit = request.GET['product_edit']

            """ split the product_add variable into its components """
            product_edit_list = product_edit.split(',')
            updated_selected = product_edit_list[2]
            item_number = product_edit_list[3]

            """ check for existing basket(s) with the current cookie value """
            try:
                existing_basket = Basket.objects.get(item_number=item_number)
                product = existing_basket.name
                category = existing_basket.category
                price = products.get(name=product).price
                total_price = total_price = float(price) * float(servings) * float(discount)

                """ filter the datasets on the variables from product_add """
                this_product = products.filter(name=product)
                options = options.filter(category__in=categories)
                """ Credit: http://morozov.ca/tip-how-to-get-a-single-objects-value-with-django-orm.html """

                """ save the updated basket and delete the existing """
                updated_basket = Basket(cookie=cookie,
                                        item_number=item_number,
                                        category=category,
                                        name=product,
                                        servings=servings,
                                        option=updated_selected,
                                        total_price=total_price)
                updated_basket.save()
                existing_basket.delete()

            except ObjectDoesNotExist:  # Credit: https://stackoverflow.com/questions/12572741/get-single-record-from-database-django
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
