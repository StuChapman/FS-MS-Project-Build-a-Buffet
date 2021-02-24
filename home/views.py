from django.shortcuts import render

from basket.contexts import basket_context

# Create your views here.


def index(request):
    """ A view to return the index page """

    """ check for a basket cookie """
    context_items = basket_context(request)
    basket_total = context_items['basket_total']

    context = {
            'basket_total': basket_total,       
        }

    return render(request, 'home/index.html', context)
