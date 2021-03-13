# Credit: Code-Institute
from django.shortcuts import render, redirect, reverse

from basket.contexts import basket_context
from .models import Questions

# Create your views here.


def service(request):
    """ A view to return the index page """

    """ check for a basket cookie """
    context_items = basket_context(request)
    basket_total = context_items['basket_total']
    cookie_key = context_items['cookie_key']

    """ check for a servings variable from the form """
    if request.POST:
        if 'name' in request.POST:
            name = request.POST["name"]
        if 'email' in request.POST:
            email = request.POST["email"]
        if 'question' in request.POST:
            question = request.POST["question"]

        """ save the updated basket and delete the existing """
        new_question = Questions(name=name,
                                 email=email,
                                 question=question)
        new_question.save()
        return redirect(reverse('home'))

    context = {
        'basket_total': basket_total,
        'cookie_key': cookie_key,
    }

    return render(request, 'service/service.html', context)