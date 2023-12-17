from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('register/',views.singup_page , name='register'),
    path('login/',views.login_page , name='login'),
    path('home/',views.home_page , name='home'),
    path('logout/',views.logout_page , name='logout'),
]
