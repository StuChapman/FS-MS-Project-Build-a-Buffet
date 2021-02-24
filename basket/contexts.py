from django.conf import settings
from django.db.models import Sum

from basket.models import Basket


def basket_context(request):

    """ check for a basket cookie """
    cookie_key = settings.COOKIE_KEY
    try:
        cookie = request.COOKIES[cookie_key]
        # Credit: https://stackoverflow.com/questions/42132091/using-aggregation-api-django
        basket_total = Basket.objects.filter(cookie=cookie).aggregate(Sum('total_price'))
    except KeyError:
        basket_total = ""

    context = {
            'cookie': cookie,
            'basket_total': basket_total
        }

    return context
