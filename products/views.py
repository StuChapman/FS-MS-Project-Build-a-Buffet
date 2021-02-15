from django.shortcuts import render, redirect, reverse, get_object_or_404

# Create your views here.


def products_sandwiches(request):
    """ A view to show just sandwiches """
    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category']

    context = {
            'product': "sandwiches",
        }

    return render(request, 'products/products.html', context)
