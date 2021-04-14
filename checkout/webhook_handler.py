# Credit: Code-Institute
from django.http import HttpResponse

from django.core.mail import send_mail
from django.template.loader import render_to_string

import uuid

from basket.models import Basket
from checkout.models import Order, Order_items


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
        order_number = "wh" + uuid.uuid4().hex[:8]

        """ check for any unordered baskets """
        cookie = billing_details.phone
        pid = intent.id
        existing = Order.objects.filter(stripe_pid=pid)

        if not existing:
            order_total = round(intent.charges.data[0].amount / 100, 2)
            full_name = shipping_details.name
            customer_name = billing_details.name
            customer_email = billing_details.email

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


            """ compose and send confirmation email """
            order_date = webhook_order.date.strftime("%d/%m/%Y %H:%M:%S")
            parameters = {
                'order_number': order_number,
                'order_date': order_date,
                'order_total': webhook_order.grand_total,
            }
            # Credit: https://stackoverflow.com/questions/2809547/creating-email-templates-with-django
            msg_html = render_to_string('checkout/confirmation_email.html',
                                        parameters)
            send_mail(
                'Order Confirmation',
                msg_html,
                'no-reply@build-a-buffet.com',
                [customer_email],
                html_message=msg_html,
            )

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
