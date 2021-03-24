# Credit: Code-Institute
from django.http import HttpResponse
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

class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping

        """ create_webhook_order """

        """ create a unique order number """
        order_number = uuid.uuid4().hex[:10]

        """ check for any unordered baskets """
        cookie = billing_details.phone
        baskets = Basket.objects.filter(cookie=cookie)

        if baskets:
            pid = intent.id
            order_total = round(intent.charges.data[0].amount / 100, 2)
            full_name = shipping_details.name
            customer_name = billing_details.name

            webhook_order = Order(order_number=order_number,
                                cookie=cookie,
                                order_total=order_total,
                                full_name=full_name,
                                customer_name=customer_name,
                                stripe_pid=pid)
            webhook_order.save()

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
                order_basket.save()
                basket.delete()
            baskets = Basket.objects.filter(cookie=cookie)

        """ webhook order created """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
