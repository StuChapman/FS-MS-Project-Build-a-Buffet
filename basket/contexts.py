from django.conf import settings
from django.db.models import Sum

from basket.models import Basket


def basket_context(request):

    """ check for a basket cookie """
    cookie_key = settings.COOKIE_KEY
    try:
        cookie = request.COOKIES[cookie_key]
        # Credit: https://stackoverflow.com/questions/42132091/using-aggregation-api-django
        basket_total = 32
    except KeyError:
        basket_total = ""
        cookie = 99999999

    context = {
            'cookie': cookie,
            'cookie_key': cookie_key,
            'basket_total': basket_total,
        }

    return context
