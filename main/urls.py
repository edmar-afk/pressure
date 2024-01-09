from django.urls import path, include
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('first', views.first, name='firstyear'),
    path('secondyear', views.second, name='secondyear'),
    path('thirdyear', views.third, name='thirdyear'),
    path('fourthyear', views.fourth, name='fourthyear'),
]