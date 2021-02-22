from django.shortcuts import render
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum

from basket.models import Basket

# Create your views here.


def index(request):
    """ A view to return the index page """

    cookie_key = settings.COOKIE_KEY

    """ check for a basket cookie """
    try:
        cookie = request.COOKIES[cookie_key]
    except KeyError:
        basket_total = ""

        context = {
                'cookie_key': cookie_key,
                'basket_total': basket_total
            }

        return render(request, 'home/index.html', context)

    # Credit: https://stackoverflow.com/questions/42132091/using-aggregation-api-django
    basket_total = Basket.objects.filter(cookie=cookie).aggregate(Sum('total_price'))

    context = {
            'cookie_key': cookie_key,
            'basket_total': basket_total
        }

    return render(request, 'home/index.html', context)
