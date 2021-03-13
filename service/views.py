# Credit: Code-Institute
from django.shortcuts import render


from basket.contexts import basket_context

# Create your views here.


def service(request):
    """ A view to return the index page """

    """ check for a basket cookie """
    context_items = basket_context(request)
    basket_total = context_items['basket_total']
    cookie_key = context_items['cookie_key']

    context = {
        'basket_total': basket_total,
        'cookie_key': cookie_key,
    }

    return render(request, 'service/service.html', context)