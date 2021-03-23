from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_success/<order_number>', views.order_success, name='order_success'),
    path('wh/', webhook, name='webhook'),
]
