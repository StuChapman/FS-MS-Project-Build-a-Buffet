from django.urls import path
from . import views

urlpatterns = [
    path('bartholemew/', views.bartholemew, name='bartholemew'),
    path('bartholemew_basket/', views.bartholemew_basket, name='bartholemew_basket')
]