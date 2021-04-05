from django.urls import path
from . import views

urlpatterns = [
    path('', views.basket, name='basket'),
    path('edit_basket_item/', views.edit_basket_item, name='edit_basket_item'),
    path('delete_basket_item/', views.delete_basket_item, name='delete_basket_item'),
    path('basket_success/<basket_key>', views.basket_success, name='basket_success'),
    path('empty_basket/', views.empty_basket, name='empty_basket'),
]
