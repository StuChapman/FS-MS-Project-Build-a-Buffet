from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_sandwiches, name='products_sandwiches'),
]
