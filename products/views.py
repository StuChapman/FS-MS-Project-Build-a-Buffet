from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Product, Category, Options

# Create your views here.


def products(request):
    """ A view to show and filter products """

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
        }

    return render(request, 'products/products.html', context)


def product_detail(request):
    """ A view to show product options """

    category = ""
    image = ""
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
        }

    return render(request, 'products/product_detail.html', context)