from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('product_detail/', views.product_detail, name='product_detail'),
    path('edit_product/', views.edit_product, name='edit_product'),
    path('product_admin/', views.product_admin, name='product_admin'),
    path('update_product/<form_id>', views.update_product, name='update_product'),
    path('refresh_product_admin/<form_id>', views.refresh_product_admin, name='refresh_product_admin'),
    path('next_product/', views.next_product, name='next_product'),
    path('prev_product/', views.prev_product, name='prev_product'),
    path('search_products/', views.search_products, name='search_products'),
]
