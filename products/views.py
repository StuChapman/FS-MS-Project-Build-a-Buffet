from django.shortcuts import render, redirect, reverse, get_object_or_404

from .models import Product, Category

# Create your views here.


def products(request):
    """ A view to show products """

    products = Product.objects.all()

    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category']
            products = products.filter(category__name__in=category)

    context = {
            'products': products,
            'category': category,
        }

    return render(request, 'products/products.html', context)
