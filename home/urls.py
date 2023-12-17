from django.contrib import admin
from django.urls import path
from home import views
from home.views import work, item_detail
urlpatterns = [
    path('register/',views.singup_page , name='register'),
    path('login/',views.login_page , name='login'),
    path('home/',views.login_page , name='home'),
    path('',views.home , name='home'),
    path('home/',views.home , name='home'),
    path('request',views.request , name='request'),
    path('formadded',views.formadded , name='formadded'),
    path('payment',views.payment , name='payment'),
    path('login',views.login , name='login'),
    path('work',views.work , name='work'),
    path('item/<int:item_id>/', item_detail, name='item_detail')
]
