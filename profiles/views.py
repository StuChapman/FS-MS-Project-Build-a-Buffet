# Credit: Code-Institute
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from django.utils.safestring import mark_safe

import re

from checkout.models import Order, Order_items
from products.models import Options
from products.models import Category


@login_required
def profile(request):

    menu = Category.objects.all().order_by('id_no')

    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':

        """ validate the form data """
        validate_default_full_name = request.POST['default_full_name']
        validate_default_phone_number = request.POST['default_phone_number']
        validate_default_country = request.POST['default_country']
        validate_default_postcode = request.POST['default_postcode']
        validate_default_town_or_city = request.POST['default_town_or_city']
        validate_default_street_address1 = request.POST['default_street_address1']
        validate_default_street_address2 = request.POST['default_street_address2']
        validate_default_county = request.POST['default_county']
        if not re.match("^[a-zA-Z ]+$", ''.join(validate_default_full_name)):
            messages.success(request, mark_safe('There was a problem with  default_full_name <br> Please try again.'))
            return redirect(reverse('home'))
        if not re.match("^[0-9]+$", ''.join(validate_default_phone_number)):
            messages.success(request, mark_safe('There was a problem with  default_phone_number <br> Please try again.'))
            return redirect(reverse('home'))
        if not re.match("^[a-zA-Z ]+$", ''.join(validate_default_country) + "a"):
            messages.success(request, mark_safe('There was a problem with  default_country <br> Please try again.'))
            return redirect(reverse('home'))
        if not re.match("^[a-zA-Z0-9 ]+$", ''.join(validate_default_postcode)):
            messages.success(request, mark_safe('There was a problem with  default_postcode <br> Please try again.'))
            return redirect(reverse('home'))
        if not re.match("^[a-zA-Z ]+$",  ''
                        .join(validate_default_town_or_city)):
            messages.success(request, mark_safe('There was a problem with  default_town_or_city<br> Please try again.'))
            return redirect(reverse('home'))
        if not re.match("^[a-zA-Z0-9 ]+$", ''
                        .join(validate_default_street_address1)):
            messages.success(request, mark_safe('There was a problem with  default_street_address1 <br> Please try again.'))
            return redirect(reverse('home'))
        if not re.match("^[a-zA-Z0-9 ]+$", ''
                        .join(validate_default_street_address2) + "a"):
            messages.success(request, mark_safe('There was a problem with  default_street_address2 <br> Please try again.'))
            return redirect(reverse('home'))
        if not re.match("^[a-zA-Z ]+$", ''
                        .join(validate_default_county) + "a"):
            messages.success(request, mark_safe('There was a problem with  default_county <br> Please try again.'))
            return redirect(reverse('home'))

        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.success(request, 'There was an error updating your profile - please try again')
    else:
        form = UserProfileForm(instance=profile)

    options = Options.objects.all()
    orders = Order.objects.filter(customer_name=profile)
    items = Order_items.objects.none()

    x = -1
    for order in orders:
        x = x + 1
        # Credit: https://stackoverflow.com/questions/5123839/
        # fastest-way-to-get-the-first-object-from-a-queryset-in-django
        order_number = (Order.objects.filter(customer_name=profile)[x]
                        .order_number)
        order_items = Order_items.objects.filter(order_number=order_number)
        items = items | order_items
    orders = orders.order_by('-date')

    context = {
        'form': form,
        'orders': orders,
        'items': items,
        'options': options,
        'menu': menu,
        'on_profile_page': True
    }

    return render(request, 'profiles/profile.html', context)


def order_history(request, order_number):

    menu = Category.objects.all().order_by('id_no')

    profile = get_object_or_404(UserProfile, user=request.user)
    order = get_object_or_404(Order, customer_name=profile)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
    ))

    context = {
        'order': order,
        'menu': menu,
        'from_profile': True,
    }

    return render(request, 'checkout/checkout_success.html', context)
