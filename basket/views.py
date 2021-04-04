from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from django.contrib import messages

from django.utils.safestring import mark_safe
import re

from products.models import Product, Category, Options
from basket.models import Basket
from basket.contexts import basket_context

# Create your views here.


def basket(request):
    """ A view to show the current basket """

    """ check for a basket cookie """
    context_items = basket_context(request)
    cookie = context_items['cookie']

    """ set all the variables to blank """
    category = ""
    selected = ""
    options = ""
    baskets = ""
    servings = ""

    """ fetch the datasets from the models """
    categories = Category.objects.all()
    products = Product.objects.all()
    options = Options.objects.all()

    """ check for a servings variable from the form """
    if request.POST:
        if 'servings' in request.POST:
            servings = request.POST["servings"]
            if not re.match("^[0-9]+$", servings):
                messages.success(request, mark_safe('There was a problem! <br> Please reselect a product and try again.'))
                return redirect(reverse('home'))

    if request.GET:

        """ check for a product_add variable from the template """
        if 'product_add' in request.GET:
            product_add = request.GET['product_add']

            """ split the product_add variable into its components """
            product_add_list = product_add.split(',')
            category = product_add_list[0]
            product = product_add_list[1]
            selected = product_add_list[2]
            productid = product_add_list[3]

            """ filter the datasets on the variables from product_add """
            options = options.filter(category__in=categories)
            """ Credit: http://morozov.ca/tip-how-to-get-a-single-objects-value-with-django-orm.html """
            price = products.get(id_no=productid).price

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
                messages.success(request, 'item quantity increased!')
                existing_basket.delete()

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
                messages.success(request, 'items added to basket!')
            baskets = Basket.objects.filter(cookie=cookie)
            baskets = baskets.order_by('-pk')

        """ check for a product_edit variable from the template """
        if 'product_edit' in request.GET:
            product_edit = request.GET['product_edit']

            """ split the product_add variable into its components """
            product_edit_list = product_edit.split(',')
            updated_selected = product_edit_list[2]
            item_number = product_edit_list[3]
            productid = product_edit_list[4]

            """ check for existing basket(s) with the current cookie value """
            try:
                existing_basket = Basket.objects.get(pk=item_number)
                product = existing_basket.name
                category = existing_basket.category
                price = products.get(id_no=productid).price
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
                messages.success(request, 'basket updated!')
                existing_basket.delete()

            except ObjectDoesNotExist:  # Credit: https://stackoverflow.com/questions/12572741/get-single-record-from-database-django
                return redirect(reverse('basket_success', args=[cookie]))
    basket_key = cookie
    return redirect(reverse('basket_success', args=[basket_key]))


def edit_basket_item(request):
    """ A view to edit basket items """

    """ check for a basket cookie """
    context_items = basket_context(request)
    basket_total = context_items['basket_total']
    cookie_key = context_items['cookie_key']

    menu = Category.objects.all().order_by('id_no')

    category = ""
    products = ""
    product = ""
    selected = ""
    image = ""
    options = ""
    servings = ""
    total_price = ""
    servings_plusten = ""
    edit = "edit"

    """ fetch the datasets from the models """
    categories = Category.objects.all()
    products = Product.objects.all()
    options = Options.objects.all()
    basket = Basket.objects.all()

    if request.GET:
        if 'item_number' in request.GET:
            item_number = request.GET['item_number']
            item_number_list = item_number.split(',')
            item_number = item_number_list[0]
            productid = item_number_list[1]
            category = basket.get(pk=item_number).category
            selected = basket.get(pk=item_number).option
            product = basket.get(pk=item_number).name
            price = products.get(id_no=productid).price
            products = products.filter(name=product)
            image = categories.filter(name=category)
            options = options.filter(category__in=categories)
            servings = basket.get(pk=item_number).servings
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
            'menu': menu,
        }

    return render(request, 'products/edit_product.html', context)


def delete_basket_item(request):
    """ A view to delete an item from the current basket """

    baskets = Basket.objects.all()

    if request.GET:
        """ check for a delete_item variable from the template """
        if 'delete_item' in request.GET:
            item_number = request.GET['delete_item']
            item_number_list = item_number.split(',')
            item_number = item_number_list[0]
            productid = item_number_list[1]
            this_item = baskets.get(pk=item_number)
            this_item.delete()
            messages.success(request, 'items removed from basket!')
            basket_key = this_item.cookie

    return redirect(reverse('basket_success', args=[basket_key]))


def basket_success(request, basket_key):
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

    menu = Category.objects.all().order_by('id_no')

    """ check for a basket cookie """
    context_items = basket_context(request)
    cookie = context_items['cookie']
    cookie_key = context_items['cookie_key']

    """ fetch the datasets from the models """
    products = Product.objects.all()
    options = Options.objects.all()

    """ get the current basket list """
    this_basket = Basket.objects.filter(cookie=basket_key)

    """ if only one basket item, use get_object_or_404 """
    if this_basket.count() == 1:
        this_basket = get_object_or_404(Basket, cookie=basket_key)
        this_product = products.filter(name=this_basket.name)
        selected = this_basket.option
        product = this_basket.name
        category = this_basket.category
        basket_key = this_basket.cookie

    # Credit: https://stackoverflow.com/questions/42132091/using-aggregation-api-django
    basket_total = Basket.objects.filter(cookie=basket_key).aggregate(Sum('total_price'))
    baskets = Basket.objects.filter(cookie=basket_key)
    # Credit: https://stackoverflow.com/questions/8786175/django-order-by-on-queryset-objects
    # Credit: https://stackoverflow.com/questions/9834038/django-order-by-query-set-ascending-and-descending
    baskets = baskets.order_by('-pk')

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
            'menu': menu,
        }

    return render(request, 'basket/basket.html', context)
