from django.shortcuts import render
from django.conf import settings

# Create your views here.


def index(request):
    """ A view to return the index page """

    cookie_key = settings.COOKIE_KEY
    context = {
            'cookie_key': cookie_key,
        }
    return render(request, 'home/index.html', context)
