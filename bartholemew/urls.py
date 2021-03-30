from django.urls import path
from . import views

urlpatterns = [
    path('bartholemew/', views.bartholemew, name='bartholemew')
]