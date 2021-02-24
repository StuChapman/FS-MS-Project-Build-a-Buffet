from django.urls import path
from . import views

urlpatterns = [
    path('', views.basket, name='basket'),
    path('delete_basket_item/', views.delete_basket_item, name='delete_basket_item'),
]
