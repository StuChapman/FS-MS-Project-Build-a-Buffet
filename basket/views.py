from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
import urllib
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from django.contrib import messages

from products.models import Product, Category, Options
from basket.models import Basket
from basket.contexts import basket_context

# Create your views here.


def basket(request):
    """ A view to show the current basket """

    """ check for a basket cookie """
    context_items = basket_context(request)
    cookie = context_items['cookie']
    cookie_key = context_items['cookie_key']

    """ set all the variables to blank """
    category = ""
    selected = ""
    options = ""
    this_product = ""
    baskets = ""
    basket_total = ""
    servings = ""

    """ fetch the datasets from the models """
    categories = Category.objects.all()
    products = Product.objects.all()
    options = Options.objects.all()

    """ check for a servings variable from the form """
    if request.POST:
        if 'servings' in request.POST:
            servings = request.POST["servings"]

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

                total_price = float(price) * float(updated_servings)

                """ save the updated basket and delete the existing """
                updated_basket = Basket(cookie=cookie,
                                        category=category,
                                        name=product,
                                        servings=updated_servings,
                                        option=selected,
                                        total_price=total_price)
                updated_basket.save()
                existing_basket.delete()

                messages.success(request, 'basket updated!')

            except ObjectDoesNotExist:  # Credit: https://stackoverflow.com/questions/12572741/get-single-record-from-database-django

                """ if there is no existing basket, create a new one """
                total_price = float(price) * float(servings)
                basket = Basket(cookie=cookie,
                                category=category,
                                name=product,
                                servings=servings,
                                option=selected,
                                total_price=total_price)
                basket.save()
            baskets = Basket.objects.filter(cookie=cookie)
            baskets = baskets.order_by('-item_number')

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
                if servings == "":
                    servings = existing_basket.servings
                    total_price = total_price = float(price) * float(servings)
                else:
                    total_price = total_price = float(price) * float(servings)

                """ filter the datasets on the variables from product_add """
                options = options.filter(category__in=categories)
                # Credit: http://morozov.ca/tip-how-to-get-a-single-objects-value-with-django-orm.html

                """ save the updated basket and delete the existing """
                updated_basket = Basket(cookie=cookie,
                                        category=category,
                                        name=product,
                                        servings=servings,
                                        option=updated_selected,
                                        total_price=total_price)
                updated_basket.save()
                existing_basket.delete()

            except ObjectDoesNotExist:  # Credit: https://stackoverflow.com/questions/12572741/get-single-record-from-database-django
                return redirect(reverse('basket_success', args=[cookie]))

    return redirect(reverse('basket_success', args=[cookie]))


def edit_basket_item(request):
    """ A view to edit basket items """

    """ check for a basket cookie """
    context_items = basket_context(request)
    basket_total = context_items['basket_total']
    cookie_key = context_items['cookie_key']

    category = ""
    products = ""
    product = ""
    selected = ""
    image = ""
    options = ""
    servings = ""
    total_price = ""
    item_number = ""
    servings_plusten = ""
    edit = "edit"

    categories = Category.objects.all()
    products = Product.objects.all()
    options = Options.objects.all()
    basket = Basket.objects.all()

    if request.GET:
        if 'item_number' in request.GET:
            item_number = request.GET['item_number']
            category = basket.get(item_number=item_number).category
            selected = basket.get(item_number=item_number).option
            product = basket.get(item_number=item_number).name
            price = products.get(name=product).price
            products = products.filter(name=product)
            image = categories.filter(name=category)
            options = options.filter(category__in=categories)
            servings = basket.get(item_number=item_number).servings
            servings_plusten = float(servings) + 10
            total_price = float(servings) * float(price)
            # Credit: https://tutorialdeep.com/knowhow/limit-float-to-two-decimal-places-python/
            total_price = format(float(total_price), '.2f')

    context = {
            'products': products,
            'category': category,
            'product': product,
            'selected': selected,
            'image': image,
            'options': options,
            'servings': servings,
            'total_price': total_price,
            'item_number': item_number,
            'servings_plusten': servings_plusten,
            'edit': edit,
            'cookie_key': cookie_key,
            'basket_total': basket_total,
        }

    return render(request, 'products/edit_product.html', context)


def delete_basket_item(request):
    """ A view to delete an item from the current basket """

    """ check for a basket cookie """
    context_items = basket_context(request)
    basket_total = context_items['basket_total']
    cookie = context_items['cookie']
    cookie_key = context_items['cookie_key']

    products = Product.objects.all()
    options = Options.objects.all()
    baskets = Basket.objects.all()

    if request.GET:
        """ check for a delete_item variable from the template """
        if 'delete_item' in request.GET:
            item_number = request.GET['delete_item']
            this_item = baskets.get(item_number=item_number)
            this_item.delete()
            cookie = this_item.cookie

    return redirect(reverse('basket_success', args=[cookie]))


def basket_success(request, cookie):
    """
    A view to avoid resubmitting form on refresh of basket
    """

    """ set all the variables to blank """
    product = ""
    category = ""
    this_product = ""
    selected = ""
    baskets = ""
    cookie_key = ""
    basket_total = ""

    """ check for a basket cookie """
    context_items = basket_context(request)
    cookie_key = context_items['cookie_key']

    products = Product.objects.all()
    options = Options.objects.all()

    this_basket = Basket.objects.filter(cookie=cookie)
    print(this_basket.count())
    if this_basket.count() == 1:
        this_basket = get_object_or_404(Basket, cookie=cookie)
        this_product = products.filter(name=this_basket.name)
        selected = this_basket.option
        product = this_basket.name
        category = this_basket.category
        cookie = this_basket.cookie

    # Credit: https://stackoverflow.com/questions/42132091/using-aggregation-api-django
    basket_total = Basket.objects.filter(cookie=cookie).aggregate(Sum('total_price'))
    baskets = Basket.objects.filter(cookie=cookie)
    # Credit: https://stackoverflow.com/questions/8786175/django-order-by-on-queryset-objects
    # Credit: https://stackoverflow.com/questions/9834038/django-order-by-query-set-ascending-and-descending
    baskets = baskets.order_by('-item_number')

    context = {
            'products': products,
            'product': product,
            'category': category,
            'this_product': this_product,
            'options': options,
            'selected': selected,
            'baskets': baskets,
            'cookie_key': cookie_key,
            'cookie': cookie,
            'basket_total': basket_total,
        }

    return render(request, 'basket/basket.html', context)
