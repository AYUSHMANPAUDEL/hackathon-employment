from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.home , name='home'),
    path('home',views.home , name='home'),
    path('request',views.request , name='request'),
    path('formadded',views.formadded , name='formadded'),
    path('payment',views.payment , name='payment'),
    path('login',views.login , name='login'),
]
