from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Product, Category, Options
from basket.models import Basket
from basket.contexts import basket_context

# Create your views here.


def products(request):
    """ A view to show and filter products """

    """ check for a basket cookie """
    context_items = basket_context(request)
    basket_total = context_items['basket_total']

    category = ""
    range = ""
    image = ""

    categories = Category.objects.all()
    products = Product.objects.all()

    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name=category)
            range = "standard"
            image = categories.filter(name=category)
        if 'category_range' in request.GET:
            category_range = request.GET['category_range']
            category_range_list = category_range.split(',')
            category = category_range_list[0]
            range = category_range_list[1]
            image = categories.filter(name=category)

    context = {
            'products': products,
            'category': category,
            'range': range,
            'image': image,
            'basket_total': basket_total
        }

    return render(request, 'products/products.html', context)


def product_detail(request):
    """ A view to show product options """

    """ check for a basket cookie """
    context_items = basket_context(request)
    basket_total = context_items['basket_total']

    category = ""
    products = ""
    selected = ""
    image = ""
    options = ""

    categories = Category.objects.all()
    products = Product.objects.all()
    options = Options.objects.all()

    if request.GET:
        if 'category_product' in request.GET:
            category_product = request.GET['category_product']
            category_product_list = category_product.split(',')
            category = category_product_list[0]
            product = category_product_list[1]
            selected = category_product_list[2]
            products = products.filter(name=product)
            image = categories.filter(name=category)
            options = options.filter(category__in=categories)

            context = {
                    'products': products,
                    'category': category,
                    'product': product,
                    'selected': selected,
                    'image': image,
                    'options': options,
                    'basket_total': basket_total
                }

    return render(request, 'products/product_detail.html', context)


def edit_product(request):
    """ A view to edit basket items """

    """ check for a basket cookie """
    context_items = basket_context(request)
    basket_total = context_items['basket_total']

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
            print(total_price)

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
            'basket_total': basket_total
        }

    return render(request, 'products/edit_product.html', context)
