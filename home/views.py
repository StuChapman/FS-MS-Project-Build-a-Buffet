from django.shortcuts import render

from basket.contexts import basket_context

# Create your views here.


def index(request):
    """ A view to return the index page """



    return render(request, 'home/index.html')
