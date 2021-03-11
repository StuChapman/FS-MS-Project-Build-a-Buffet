from django.shortcuts import render, get_object_or_404
from .models import UserQuestion
from .forms import UserQuestionForm

from basket.contexts import basket_context

# Create your views here.


def service(request):
    """ A view to return the index page """

    """ check for a basket cookie """
    context_items = basket_context(request)
    basket_total = context_items['basket_total']
    cookie_key = context_items['cookie_key']

    profile = get_object_or_404(UserQuestion, user=request.user)
    form = UserQuestionForm(instance=profile)

    context = {
            'cookie_key': cookie_key,
            'basket_total': basket_total,
            'form': form,
        }

    return render(request, 'service/service.html', context)