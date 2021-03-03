# Credit: Code-Institute
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order, Order_items
from products.models import Options


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    options = Options.objects.all()
    orders = Order.objects.filter(customer_name=profile)
    items = Order_items.objects.none()

    x = -1
    for order in orders:
        x = x + 1
        # Credit: https://stackoverflow.com/questions/5123839/fastest-way-to-get-the-first-object-from-a-queryset-in-django
        order_number = Order.objects.filter(customer_name=profile)[x].order_number
        order_items = Order_items.objects.filter(order_number=order_number)
        items = items | order_items
    orders = orders.order_by('-date')

    context = {
        'form': form,
        'orders': orders,
        'items': items,
        'options': options,
        'on_profile_page': True
    }

    return render(request, 'profiles/profile.html', context)


def order_history(request, order_number):
    profile = get_object_or_404(UserProfile, user=request.user)
    order = get_object_or_404(Order, customer_name=profile)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, 'checkout/checkout_success.html', context)