from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('product_detail/', views.product_detail, name='product_detail'),
    path('edit_product/', views.edit_product, name='edit_product'),
    path('product_admin/', views.product_admin, name='product_admin'),
    path('update_product/', views.update_product, name='update_product'),
]
