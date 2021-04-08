# Credit: Code-Institute
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from django.utils.safestring import mark_safe

import re

from basket.contexts import basket_context
from .models import Questions
from products.models import Category

# Create your views here.


def service(request):
    """ A view to recieve questions from customers """

    """ check for a basket cookie """
    context_items = basket_context(request)
    basket_total = context_items['basket_total']
    cookie_key = context_items['cookie_key']

    menu = Category.objects.all().order_by('id_no')

    """ check for a servings variable from the form """
    if request.POST:

        """ validate the form data """
        validate_name = request.POST['name']
        validate_email = request.POST['email']
        validate_question = request.POST['question']
        if not re.match("^[a-zA-Z ]+$", ''.join(validate_name)):
            messages.success(request, mark_safe('There was a problem with name <br> Please try again.'))
            return redirect(reverse('home'))
        if not re.match(r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$", ''
                        .join(validate_email)):
            messages.success(request, mark_safe('There was a problem with email <br> Please try again.'))
            return redirect(reverse('home'))
        if not re.match("^[a-zA-Z0-9.?* ]+$", ''.join(validate_question)):
            messages.success(request, mark_safe('There was a problem with question <br> Please try again.'))
            return redirect(reverse('home'))

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
        messages.success(request, 'Your question has been sent - we will reply shortly')
        return redirect(reverse('home'))

    context = {
        'basket_total': basket_total,
        'cookie_key': cookie_key,
        'menu': menu,
    }

    return render(request, 'service/service.html', context)
