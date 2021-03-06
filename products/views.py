from django.shortcuts import render, get_object_or_404

from .models import Product, Category, Options
from basket.models import Basket
from basket.contexts import basket_context
from .forms import ProductAdminForm

# Create your views here.


def products(request):
    """ A view to show and filter products """

    """ check for a basket cookie """
    context_items = basket_context(request)
    basket_total = context_items['basket_total']
    cookie_key = context_items['cookie_key']

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
            'cookie_key': cookie_key,
            'basket_total': basket_total
        }

    return render(request, 'products/products.html', context)


def product_detail(request):
    """ A view to show product options """

    """ check for a basket cookie """
    context_items = basket_context(request)
    basket_total = context_items['basket_total']
    cookie_key = context_items['cookie_key']

    category = ""
    products = ""
    selected = ""
    image = ""
    options = ""
    item_number = ""

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
                    'cookie_key': cookie_key,
                    'basket_total': basket_total,
                }

            return render(request, 'products/product_detail.html', context)

        if 'product_edit' in request.GET:
            product_edit = request.GET['product_edit']
            product_edit_list = product_edit.split(',')
            category = product_edit_list[0]
            product = product_edit_list[1]
            selected = product_edit_list[2]
            item_number = product_edit_list[3]
            servings = product_edit_list[4]
            servings_plusten = float(servings) + 10
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
                    'servings': servings,
                    'item_number': item_number,
                    'servings_plusten': servings_plusten,
                    'cookie_key': cookie_key,
                    'basket_total': basket_total,
                }

            return render(request, 'products/edit_product.html', context)
    return render(request, 'products/product_detail.html', context)


def edit_product(request):
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


def product_admin(request):
    """ A view to manage products, categories and options """

    product_query = get_object_or_404(Product, name='Cheese')


    if request.GET:
        if 'dataset' in request.GET:
            dataset = request.GET['dataset']
            form = ProductAdminForm(instance=product_query)
        else:
            form = ProductAdminForm(instance=product_query)

    context = {
            'dataset': dataset,
            'form': form,
        }

    return render(request, 'products/product_admin.html', context)
