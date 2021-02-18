from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Product, Category

# Create your views here.


def products(request):
    """ A view to show and filter products """

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