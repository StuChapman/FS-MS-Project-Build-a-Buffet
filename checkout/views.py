from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings

from django.core.mail import send_mail
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string

import uuid

from products.models import Product, Category, Options
from basket.models import Basket
from checkout.models import Order, Order_items
from basket.contexts import basket_context
from profiles.models import UserProfile
from .forms import OrderForm

import stripe

# Create your views here.


def checkout(request):
    """ A view to return the checkout page """

    """ check for a basket cookie """
    context_items = basket_context(request)
    cookie = context_items['cookie']
    basket_total = context_items['basket_total']
    cookie_key = context_items['cookie_key']

    baskets = ""

    """ fetch the datasets from the models """
    basket = Basket.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()
    options = Options.objects.all()

    # Attempt to prefill the form with any info the user maintains in their profile
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'full_name': profile.default_full_name,
                'email': profile.user.email,
                'phone_number': profile.default_phone_number,
                'country': profile.default_country,
                'postcode': profile.default_postcode,
                'town_or_city': profile.default_town_or_city,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'county': profile.default_county,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()

    """ fetch the Stripe keys """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if basket_total:
        """ create the Stripe payment intent """
        stripe_total = round(float(basket_total['total_price__sum']) * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        client_secret = intent.client_secret
    else:
        client_secret = ""

    if request.GET:
        if 'basket_number' in request.GET:
            basket_number = request.GET['basket_number']
            baskets = basket.filter(cookie=basket_number)
            baskets = baskets.order_by('-pk')

    context = {
            'cookie': cookie,
            'cookie_key': cookie_key,
            'basket_total': basket_total,
            'baskets': baskets,
            'products': products,
            'categories': categories,
            'options': options,
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': client_secret,
        }

    return render(request, 'checkout/checkout.html', context)


def create_order(request):
    """ A view to create an order and make a Stripe payment """

    baskets = ""
    item_number = ""
    category = ""
    name = ""
    servings = ""
    option = ""
    total_price = ""

    """ fetch the datasets from the models """
    basket = Basket.objects.all()

    """ check for the customer info from checkout """
    if request.POST:
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        if request.user.is_authenticated:
            if 'save-info' in request.POST:
                """ save the user info into user profile """
                profile = UserProfile.objects.get(user=request.user)

                profile.default_full_name = request.POST['full_name']
                profile.default_phone_number = request.POST['phone_number']
                profile.default_country = request.POST['country']
                profile.default_postcode = request.POST['postcode']
                profile.default_town_or_city = request.POST['town_or_city']
                profile.default_street_address1 = request.POST['street_address1']
                profile.default_street_address2 = request.POST['street_address2']
                profile.default_county = request.POST['county']
                profile.save()

        """ create a count to ensure only one attempt is made for payment_success """
        success_count = 0

        try:
            payment_success = request.POST.get('paymentSuccess')
            try:
                payment_success = "succeeded"
                success_count = success_count + 1
                """ create a unique order number """
                order_number = uuid.uuid4().hex[:10]
                order_form = OrderForm(form_data)
                if order_form.is_valid() and success_count < 2:
                    order = order_form.save(commit=False)
                    order.order_number = order_number
                    cookie = request.POST.get('basket_number')
                    order.cookie = cookie
                    order_total = request.POST.get('total_price')
                    order.order_total = order_total
                    customer_name = request.user
                    order.customer_name = customer_name
                    order.save()

                    """ fetch the basket items to save into order_items """
                    baskets = Basket.objects.filter(cookie=cookie)
                    for basket in baskets:
                        cookie = basket.cookie
                        item_number = basket.pk
                        category = basket.category
                        name = basket.name
                        servings = basket.servings
                        option = basket.option
                        total_price = basket.total_price

                        """ save the basket items into order_items """
                        order_basket = Order_items(cookie=cookie,
                                                order_number=order_number,
                                                item_number=item_number,
                                                category=category,
                                                name=name,
                                                servings=servings,
                                                option=option,
                                                total_price=total_price)
                        print(order_number)
                        order_basket.save()
                        basket.delete()
                    # Credit: https://stackoverflow.com/questions/53151314/add-new-line-to-admin-action-message
                    messages.success(request, mark_safe(f'Thank you for your order! <br> Your order number is {order_number} <br> A confirmation email will be sent to {order.email}.'))

                    """ compose and send confirmation email """
                    order_date = order.date.strftime("%d/%m/%Y %H:%M:%S")
                    parameters = {
                        'order_number': order_number,
                        'order_date': order_date,
                        'order_total': order.order_total,
                    }
                    # Credit: https://stackoverflow.com/questions/2809547/creating-email-templates-with-django
                    msg_html = render_to_string('checkout/confirmation_email.html',
                                                parameters)
                    send_mail(
                        'Order Confirmation',
                        msg_html,
                        'no-reply@build-a-buffet.com',
                        [order.email],
                        html_message=msg_html,
                    )

                    return redirect(reverse('order_success', args=[order_number]))
                else:
                    messages.success(request, ('Form was not valid'))
                    return redirect(reverse('checkout'))
            except Exception as e:
                return HttpResponse(content=e, status=200)
        except Exception as e:
            messages.success(request, ('No paymentSuccess in request.POST:'))
            return HttpResponse(content=e, status=400)


def order_success(request, order_number):
    """ Handle successful checkouts and show individual orders """

    order = get_object_or_404(Order, order_number=order_number)
    orders = Order.objects.filter(order_number=order_number)
    order_items = Order_items.objects.filter(order_number=order_number)
    products = Product.objects.all()
    options = Options.objects.all()

    """ Check current user is purchaser """
    current_user = str(request.user)
    purchaser = str(order.customer_name)
    if current_user != purchaser:
        return render(request, 'allauth/account/login.html')
    else:
        context = {
            'order': order,
            'orders': orders,
            'order_items': order_items,
            'products': products,
            'options': options,
        }

        return render(request, 'checkout/order_success.html', context)
