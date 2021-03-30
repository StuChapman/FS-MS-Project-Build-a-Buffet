from django.shortcuts import render

from basket.contexts import basket_context

# Create your views here.


def bartholemew(request):
    """ A view to return the bartholemew page """

    """ check for a basket cookie """
    context_items = basket_context(request)
    basket_total = context_items['basket_total']
    cookie_key = context_items['cookie_key']

    context = {
            'cookie_key': cookie_key,
            'basket_total': basket_total,
        }

    return render(request, 'bartholemew/bartholemew.html', context)
